#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml==6.0.3"]
# ///
"""Report phase gates, gaps, open questions and admin tasks for a deployment.yaml.

Read-only and offline: this script never makes network calls and never writes
files. It implements the phase-gate table and build rules from
``guides/state-schema.md`` and is the same for every customer.

Usage:
    uv run status.py <deployment.yaml> [--json]
    python status.py <deployment.yaml> [--json]    # after: pip install pyyaml==6.0.3

Exit codes:
    0  the file was read and a report was produced (the report is not a linter,
       so unmet gates do not change the exit code)
    2  usage error, unreadable file, or YAML that does not parse to a mapping
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TypedDict

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without PyYAML installed
    print(
        "status.py needs PyYAML: run with 'uv run status.py ...' or 'pip install pyyaml==6.0.3'",
        file=sys.stderr,
    )
    sys.exit(2)

BUILDABLE = frozenset({"stated", "sourced", "confirmed"})
MAX_PROBLEM_LINES = 8
DEFAULT_CONNECTOR_COUNT = 2


class Gate(TypedDict):
    """Result of one phase gate."""

    phase: int
    gate: str
    ok: bool
    problems: list[str]


def load_state(path: str | Path) -> dict[str, Any]:
    """Load a deployment state file.

    Args:
        path: Path to ``deployment.yaml``.

    Returns:
        The parsed top-level mapping (empty dict for an empty file).

    Raises:
        OSError: The file cannot be read.
        yaml.YAMLError: The file is not valid YAML.
        ValueError: The YAML top level is not a mapping.
    """
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError("top level of the state file must be a mapping")
    return data


def _dicts(value: Any) -> list[dict[str, Any]]:
    """Return the dict items of a list-valued key, tolerating null or junk."""
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def _mapping(value: Any) -> dict[str, Any]:
    """Return value if it is a dict, else an empty dict."""
    return value if isinstance(value, dict) else {}


def _in_scope_resources(state: dict[str, Any]) -> list[dict[str, Any]]:
    """Return resources whose ``in_scope`` is true (default true)."""
    return [r for r in _dicts(state.get("resources")) if r.get("in_scope", True)]


def _decided_phases(state: dict[str, Any]) -> set[str]:
    """Return the set of phases (as strings) that have a recorded decision."""
    return {str(d.get("phase")) for d in _dicts(state.get("decisions"))}


def _connector_target(network: dict[str, Any]) -> int:
    """Return the configured connector_count, defaulting to 2."""
    raw = network.get("connector_count", DEFAULT_CONNECTOR_COUNT)
    try:
        return int(raw)
    except (TypeError, ValueError):
        return 0


def _normalise_criteria(meta: dict[str, Any]) -> list[dict[str, str]]:
    """Normalise success criteria: strings become ``status: open`` entries."""
    out: list[dict[str, str]] = []
    raw = meta.get("success_criteria")
    for item in raw if isinstance(raw, list) else []:
        if isinstance(item, str):
            out.append({"text": item, "status": "open", "note": ""})
        elif isinstance(item, dict):
            out.append(
                {
                    "text": str(item.get("text", "")),
                    "status": str(item.get("status") or "open").lower(),
                    "note": str(item.get("note") or ""),
                }
            )
    return out


def _scim_accepted(state: dict[str, Any]) -> bool:
    """True when SCIM is 'yes' or a phase-2 decision mentions SCIM."""
    env = _mapping(state.get("environment"))
    # Unquoted `scim: yes` parses as boolean True under YAML 1.1.
    if env.get("scim") is True or str(env.get("scim", "")).lower() == "yes":
        return True
    return any(
        str(d.get("phase")) == "2" and "scim" in str(d.get("decision", "")).lower()
        for d in _dicts(state.get("decisions"))
    )


def gate_checks(state: dict[str, Any]) -> list[Gate]:
    """Evaluate phase gates 0-9 from ``guides/state-schema.md``.

    Args:
        state: Parsed deployment state.

    Returns:
        One ``Gate`` per phase, in phase order.
    """
    meta = _mapping(state.get("meta"))
    env = _mapping(state.get("environment"))
    networks = _dicts(state.get("remote_networks"))
    resources = _in_scope_resources(state)
    personas = {p.get("id"): p for p in _dicts(state.get("personas"))}
    group_ids = {g.get("name"): g.get("twingate_id") for g in _dicts(state.get("groups"))}
    decided = _decided_phases(state)
    network_names = {n.get("name") for n in networks}
    used_personas = sorted({pid for r in resources for pid in r.get("personas") or []}, key=str)

    gates: list[Gate] = []

    def add(phase: int, label: str, problems: list[str]) -> None:
        gates.append({"phase": phase, "gate": label, "ok": not problems, "problems": problems})

    # 0 Kickoff
    p: list[str] = []
    if not meta.get("tenant"):
        p.append("meta.tenant missing")
    if meta.get("path") not in ("guided", "expert"):
        p.append("meta.path not set (guided|expert)")
    if not meta.get("assist_level"):
        p.append("meta.assist_level missing")
    if not _normalise_criteria(meta):
        p.append("no success_criteria")
    add(0, "Kickoff", p)

    # 1 Discover
    p = []
    if not networks:
        p.append("no remote_networks")
    for r in resources:
        if not r.get("address"):
            p.append(f"{r.get('id')}: no address")
        if r.get("remote_network") not in network_names:
            p.append(f"{r.get('id')}: remote_network '{r.get('remote_network')}' unknown")
    if not personas:
        p.append("no personas")
    add(1, "Discover", p)

    # 2 Tenant & IdP
    p = []
    idp = str(env.get("idp") or "").lower()
    if not idp:
        p.append("environment.idp not set")
    elif idp == "none":
        p.append("environment.idp is 'none'")
    if not env.get("idp_connected"):
        p.append("environment.idp_connected is not true")
    if not _scim_accepted(state):
        p.append("SCIM not 'yes' and no phase-2 decision accepting no SCIM")
    for pid in used_personas:
        groups = _mapping(personas.get(pid)).get("groups") or []
        if not any(group_ids.get(g) for g in groups):
            p.append(f"persona '{pid}': no mapped group with a twingate_id")
    add(2, "Tenant & IdP", p)

    # 3 Confirm resources
    p = [] if resources else ["no in-scope resources"]
    for r in resources:
        if r.get("provenance") not in BUILDABLE:
            p.append(f"{r.get('id')}: provenance '{r.get('provenance')}' (needs confirmation)")
        ports = _mapping(r.get("ports"))
        if not (ports.get("tcp") or ports.get("udp")):
            p.append(f"{r.get('id')}: no tcp or udp ports")
    add(3, "Confirm resources", p)

    # 4 Access model
    p = []
    for r in resources:
        if not r.get("personas"):
            p.append(f"{r.get('id')}: no personas")
    for pid in used_personas:
        if pid not in personas:
            p.append(f"persona '{pid}': not defined")
        elif personas[pid].get("provenance") not in BUILDABLE:
            p.append(f"persona '{pid}': provenance '{personas[pid].get('provenance')}' (needs confirmation)")
    if "4" not in decided:
        p.append("access matrix not approved (no phase-4 decision)")
    add(4, "Access model", p)

    # 5 Remote Networks
    p = [] if networks else ["no remote_networks"]
    for n in networks:
        if n.get("provenance") not in BUILDABLE:
            p.append(f"{n.get('name')}: provenance '{n.get('provenance')}' (needs confirmation)")
        if not n.get("twingate_id"):
            p.append(f"{n.get('name')}: not created (no twingate_id)")
    if "5" not in decided:
        p.append("remote networks not approved (no phase-5 decision)")
    add(5, "Remote Networks", p)

    # 6 Connectors
    p = [] if networks else ["no remote_networks"]
    for n in networks:
        want = _connector_target(n)
        alive = [
            c
            for c in _dicts(n.get("connectors"))
            if str(c.get("state", "")).upper() == "ALIVE"
        ]
        if want < 2:
            p.append(f"{n.get('name')}: connector_count {want} < 2 (no HA)")
        if len(alive) < want:
            p.append(f"{n.get('name')}: {len(alive)}/{want} connectors ALIVE")
    add(6, "Connectors", p)

    # 7 Resources & access
    p = [] if resources else ["no in-scope resources"]
    p += [f"{r.get('id')}: not created (no twingate_id)" for r in resources if not r.get("twingate_id")]
    if "7" not in decided:
        p.append("resources and access not approved (no phase-7 decision)")
    add(7, "Resources & access", p)

    # 8 Pilot
    p = [] if _normalise_criteria(meta) else ["no success_criteria"]
    for c in _normalise_criteria(meta):
        label = c["text"][:60]
        match c["status"]:
            case "met":
                pass
            case "deferred":
                if not c["note"].strip():
                    p.append(f"criterion '{label}': deferred without a note")
            case _:
                p.append(f"criterion '{label}': status {c['status']}")
    add(8, "Pilot", p)

    # 9 Rollout & harden
    p = []
    if "9" not in decided:
        p.append("no phase-9 decision (admin sign-off)")
    add(9, "Rollout & harden", p)

    return gates


def build_rules(state: dict[str, Any], gates: list[Gate]) -> tuple[bool, bool]:
    """Apply the two build rules from the schema.

    Args:
        state: Parsed deployment state.
        gates: Output of ``gate_checks`` for the same state.

    Returns:
        ``(networks_build_allowed, resources_build_allowed)``.
    """
    ok = {g["phase"]: g["ok"] for g in gates}
    networks = _dicts(state.get("remote_networks"))
    networks_ok = ok[0] and ok[1] and all(n.get("provenance") in BUILDABLE for n in networks)
    resources_ok = all(ok[n] for n in (1, 2, 3, 4, 5, 6))
    return networks_ok, resources_ok


def build_report(state: dict[str, Any]) -> dict[str, Any]:
    """Build the full status report.

    Args:
        state: Parsed deployment state.

    Returns:
        A JSON-serialisable (via ``default=str``) report dict.
    """
    meta = _mapping(state.get("meta"))
    gates = gate_checks(state)
    networks_ok, resources_ok = build_rules(state, gates)
    provenance: dict[str, int] = {}
    for r in _in_scope_resources(state):
        key = str(r.get("provenance", "?"))
        provenance[key] = provenance.get(key, 0) + 1
    return {
        "customer": meta.get("customer"),
        "recorded_phase": meta.get("phase"),
        "first_unmet_gate": next((g["phase"] for g in gates if not g["ok"]), None),
        "networks_build_allowed": networks_ok,
        "resources_build_allowed": resources_ok,
        "resource_provenance": provenance,
        "gates": gates,
        "open_questions": [
            q for q in _dicts(state.get("open_questions")) if q.get("status", "open") == "open"
        ],
        "open_tasks": [t for t in _dicts(state.get("tasks")) if t.get("status", "todo") != "done"],
    }


def format_text(report: dict[str, Any]) -> str:
    """Render a report as human-readable text.

    Args:
        report: Output of ``build_report``.

    Returns:
        Multi-line text, capped at 8 problem lines per gate.
    """
    lines = [
        f"Customer: {report['customer']}   recorded phase: {report['recorded_phase']}   "
        f"first unmet gate: {report['first_unmet_gate']}",
        f"Build allowed: networks={report['networks_build_allowed']}   "
        f"resources={report['resources_build_allowed']}",
        f"In-scope resources by provenance: {report['resource_provenance']}",
    ]
    for g in report["gates"]:
        lines.append(f"  {'OK ' if g['ok'] else '-- '}Phase {g['phase']} {g['gate']}")
        lines.extend(f"       - {prob}" for prob in g["problems"][:MAX_PROBLEM_LINES])
        if len(g["problems"]) > MAX_PROBLEM_LINES:
            lines.append(f"       ... {len(g['problems']) - MAX_PROBLEM_LINES} more")
    if report["open_questions"]:
        lines.append("Open questions:")
        lines.extend(
            f"  [{q.get('owner', '?')}] {q.get('id')}: {q.get('question')}"
            for q in report["open_questions"]
        )
    if report["open_tasks"]:
        lines.append("Open tasks:")
        lines.extend(
            f"  [{t.get('owner', '?')}/{t.get('status', 'todo')}] {t.get('id')}: "
            f"{t.get('description')}  -> send back: {t.get('evidence_needed') or '-'}"
            for t in report["open_tasks"]
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    Args:
        argv: Argument list (defaults to ``sys.argv[1:]``).

    Returns:
        0 for a valid file, 2 for usage or parse errors.
    """
    parser = argparse.ArgumentParser(
        prog="status.py", description="Report gate status for a twingate-onboarding deployment.yaml."
    )
    parser.add_argument("state_file", help="path to deployment.yaml")
    parser.add_argument("--json", action="store_true", help="emit the full report as JSON")
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return 0 if exc.code in (0, None) else 2
    try:
        state = load_state(args.state_file)
    except (OSError, yaml.YAMLError, ValueError) as exc:
        print(f"status.py: cannot read {args.state_file}: {exc}", file=sys.stderr)
        return 2
    report = build_report(state)
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfigure):  # keep non-ASCII state content printable on Windows consoles
        reconfigure(encoding="utf-8", errors="replace")
    if args.json:
        print(json.dumps(report, indent=2, default=str, ensure_ascii=False))
    else:
        print(format_text(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
