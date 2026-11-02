"""Tests for skills/twingate-onboarding/scripts/status.py."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO_ROOT / "skills" / "twingate-onboarding"
STATUS_PATH = SKILL_DIR / "scripts" / "status.py"
EXAMPLES = SKILL_DIR / "examples"
TEMPLATE = SKILL_DIR / "assets" / "deployment.template.yaml"

_spec = importlib.util.spec_from_file_location("onboarding_status", STATUS_PATH)
assert _spec is not None and _spec.loader is not None
status = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(status)


def load(path: Path) -> dict[str, Any]:
    """Load a state file through the module under test."""
    return status.load_state(path)


def gate_map(state: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """Return gates keyed by phase."""
    return {g["phase"]: g for g in status.gate_checks(state)}


@pytest.fixture
def guided() -> dict[str, Any]:
    return load(EXAMPLES / "guided-mid-discovery.yaml")


@pytest.fixture
def expert() -> dict[str, Any]:
    return load(EXAMPLES / "expert-path.yaml")


@pytest.fixture
def resume() -> dict[str, Any]:
    return load(EXAMPLES / "resume-mid-build.yaml")


def passing_state() -> dict[str, Any]:
    """A minimal state that passes gates 0-6 (built from the resume example)."""
    state = load(EXAMPLES / "resume-mid-build.yaml")
    state["remote_networks"][1]["connectors"][1]["state"] = "ALIVE"
    return state


def test_template_first_unmet_gate_is_zero_and_builds_blocked() -> None:
    report = status.build_report(load(TEMPLATE))
    assert report["first_unmet_gate"] == 0
    assert report["networks_build_allowed"] is False
    assert report["resources_build_allowed"] is False


def test_guided_gate3_names_exactly_two_resources(guided: dict[str, Any]) -> None:
    gates = gate_map(guided)
    assert gates[0]["ok"] and gates[1]["ok"]
    assert not gates[2]["ok"]
    assert not gates[3]["ok"]
    assert len(gates[3]["problems"]) == 2
    text = "\n".join(gates[3]["problems"])
    assert "res-hr01" in text and "res-fs" in text
    report = status.build_report(guided)
    assert report["resources_build_allowed"] is False
    assert report["networks_build_allowed"] is True
    assert report["resource_provenance"]["inferred"] == 2
    assert report["open_questions"] and report["open_tasks"]


def test_guided_out_of_scope_resource_is_ignored(guided: dict[str, Any]) -> None:
    problems = "\n".join(p for g in status.gate_checks(guided) for p in g["problems"])
    assert "res-label" not in problems


def test_expert_gates_0_to_4_pass_and_5_fails(expert: dict[str, Any]) -> None:
    gates = gate_map(expert)
    for phase in range(5):
        assert gates[phase]["ok"], (phase, gates[phase]["problems"])
    assert not gates[5]["ok"]
    report = status.build_report(expert)
    assert report["first_unmet_gate"] == 5
    assert report["networks_build_allowed"] is True
    assert report["resources_build_allowed"] is False


def test_resume_gate6_names_network_with_one_alive(resume: dict[str, Any]) -> None:
    gates = gate_map(resume)
    for phase in range(6):
        assert gates[phase]["ok"], (phase, gates[phase]["problems"])
    assert not gates[6]["ok"]
    assert gates[6]["problems"] == ["Plant South: 1/2 connectors ALIVE"]
    assert status.build_report(resume)["resources_build_allowed"] is False


def test_resume_flips_when_dead_connector_set_alive(resume: dict[str, Any]) -> None:
    resume["remote_networks"][1]["connectors"][1]["state"] = "alive"
    assert gate_map(resume)[6]["ok"]
    assert status.build_report(resume)["resources_build_allowed"] is True


def test_persona_without_mapped_group_fails_gate2() -> None:
    state = passing_state()
    state["personas"][0]["groups"] = []
    gate = gate_map(state)[2]
    assert not gate["ok"]
    assert any("process-eng" in p for p in gate["problems"])


def test_group_mapped_but_missing_twingate_id_fails_gate2() -> None:
    state = passing_state()
    state["groups"][0]["twingate_id"] = None
    assert not gate_map(state)[2]["ok"]


def test_group_name_not_in_groups_fails_gate2() -> None:
    state = passing_state()
    state["personas"][0]["groups"] = ["Nonexistent"]
    assert not gate_map(state)[2]["ok"]


def test_scim_accepted_by_phase2_decision() -> None:
    state = passing_state()
    state["environment"]["scim"] = "no"
    assert not gate_map(state)[2]["ok"]
    state["decisions"].append({"phase": 2, "decision": "Proceed without Scim for now"})
    assert gate_map(state)[2]["ok"]


def test_scim_decision_in_other_phase_does_not_count() -> None:
    state = passing_state()
    state["environment"]["scim"] = "unknown"
    state["decisions"].append({"phase": 4, "decision": "No SCIM"})
    assert not gate_map(state)[2]["ok"]


def test_connector_count_one_fails_gate6() -> None:
    state = passing_state()
    state["remote_networks"][0]["connector_count"] = 1
    gate = gate_map(state)[6]
    assert not gate["ok"]
    assert any("no HA" in p for p in gate["problems"])


def test_connector_count_defaults_to_two() -> None:
    state = passing_state()
    del state["remote_networks"][0]["connector_count"]
    state["remote_networks"][0]["connectors"].pop()
    assert any("1/2" in p for p in gate_map(state)[6]["problems"])


def test_string_success_criteria_count_as_open() -> None:
    state = passing_state()
    state["meta"]["success_criteria"] = ["DBAs reach db1"]
    gate = gate_map(state)[8]
    assert not gate["ok"]
    assert "open" in gate["problems"][0]
    assert gate_map(state)[0]["ok"]


def test_deferred_without_note_fails_gate8() -> None:
    state = passing_state()
    state["meta"]["success_criteria"] = [
        {"text": "a", "status": "met"},
        {"text": "b", "status": "deferred", "note": "  "},
    ]
    gate = gate_map(state)[8]
    assert not gate["ok"] and len(gate["problems"]) == 1
    state["meta"]["success_criteria"][1]["note"] = "Waiting on vendor"
    assert gate_map(state)[8]["ok"]


def test_out_of_scope_resources_ignored() -> None:
    state = passing_state()
    state["resources"].append(
        {"id": "res-skip", "in_scope": False, "provenance": "inferred", "address": ""}
    )
    assert all("res-skip" not in p for g in status.gate_checks(state) for p in g["problems"])
    assert status.build_report(state)["resource_provenance"] == {"confirmed": 1, "stated": 2}


def test_in_scope_defaults_true() -> None:
    state = passing_state()
    state["resources"].append({"id": "res-new", "provenance": "inferred"})
    assert any("res-new" in p for p in gate_map(state)[3]["problems"])


def test_decision_gates_7_and_9() -> None:
    state = passing_state()
    for r in state["resources"]:
        r["twingate_id"] = "abc"
    assert not gate_map(state)[7]["ok"]
    state["decisions"].append({"phase": 7, "decision": "ok"})
    assert gate_map(state)[7]["ok"]
    assert not gate_map(state)[9]["ok"]
    state["decisions"].append({"phase": 9, "decision": "sign-off"})
    assert gate_map(state)[9]["ok"]


def test_networks_blocked_when_network_provenance_inferred(guided: dict[str, Any]) -> None:
    guided["remote_networks"][0]["provenance"] = "inferred"
    assert status.build_report(guided)["networks_build_allowed"] is False


def test_all_gates_pass_state() -> None:
    state = passing_state()
    for r in state["resources"]:
        r["twingate_id"] = "abc"
    for c in state["meta"]["success_criteria"]:
        c["status"] = "met"
    state["decisions"] += [{"phase": 7, "decision": "x"}, {"phase": 9, "decision": "y"}]
    report = status.build_report(state)
    assert report["first_unmet_gate"] is None
    assert all(g["ok"] for g in report["gates"])


def test_text_output_caps_problem_lines() -> None:
    state = copy.deepcopy(load(TEMPLATE))
    state["resources"] = [{"id": f"r{i}", "provenance": "inferred"} for i in range(12)]
    out = status.format_text(status.build_report(state))
    assert "... " in out and "more" in out


def test_json_output_parses(capsys: pytest.CaptureFixture[str]) -> None:
    rc = status.main([str(EXAMPLES / "resume-mid-build.yaml"), "--json"])
    assert rc == 0
    data = json.loads(capsys.readouterr().out)
    assert data["customer"] == "Ironwood Manufacturing"
    assert len(data["gates"]) == 10
    assert data["resources_build_allowed"] is False


@pytest.mark.parametrize("name", ["guided-mid-discovery", "expert-path", "resume-mid-build"])
def test_text_output_for_examples(name: str, capsys: pytest.CaptureFixture[str]) -> None:
    assert status.main([str(EXAMPLES / f"{name}.yaml")]) == 0
    out = capsys.readouterr().out
    assert "first unmet gate" in out and "Phase 0 Kickoff" in out


def test_utf8_content_loads(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    state = {"meta": {"customer": "Acme", "phase": 0}, "resources": [
        {"id": "r1", "description": "HQ → DC link", "provenance": "inferred"}]}
    path = tmp_path / "d.yaml"
    path.write_text(yaml.safe_dump(state, allow_unicode=True), encoding="utf-8")
    assert "→" in status.load_state(path)["resources"][0]["description"]
    assert status.main([str(path)]) == 0
    assert status.main([str(path), "--json"]) == 0
    capsys.readouterr()


def test_errors_exit_two(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert status.main([]) == 2
    assert status.main([str(tmp_path / "missing.yaml")]) == 2
    bad = tmp_path / "bad.yaml"
    bad.write_text("- just\n- a list\n", encoding="utf-8")
    assert status.main([str(bad)]) == 2
    broken = tmp_path / "broken.yaml"
    broken.write_text("a: [unclosed\n", encoding="utf-8")
    assert status.main([str(broken)]) == 2
    assert "status.py" in capsys.readouterr().err


def test_empty_file_is_valid(tmp_path: Path) -> None:
    empty = tmp_path / "e.yaml"
    empty.write_text("", encoding="utf-8")
    assert status.main([str(empty)]) == 0


def test_empty_catalog_does_not_pass_build_gates() -> None:
    gates = gate_map(load(TEMPLATE))
    for phase in (3, 5, 6, 7, 8):
        assert gates[phase]["ok"] is False, phase


def test_unquoted_scim_yes_boolean_is_accepted() -> None:
    state = passing_state()
    state["environment"]["scim"] = True
    assert gate_map(state)[2]["ok"] is True


def test_resources_build_requires_gate1() -> None:
    state = passing_state()
    assert status.build_report(state)["resources_build_allowed"] is True
    state["resources"][0]["address"] = ""
    assert status.build_report(state)["resources_build_allowed"] is False
