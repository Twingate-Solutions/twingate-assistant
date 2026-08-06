# Pipeline churn metrics

This directory holds **observation-only** telemetry from the weekly doc
auto-update pipeline (`scripts/update_references.py`). It records how much of
each week's churn is *timestamp noise* versus *real documentation edits*, so we
can decide — with several weeks of data — whether to switch change-detection
from the raw content hash to the normalized ("shadow") hash. Collecting these
metrics changes **no** pipeline behavior: a page re-summarizes if and only if it
did before.

## The signal

Every Twingate doc page renders a relative `Last updated / N months ago`
timestamp inside `<main>`. That string ages on its own (`5 days ago` →
`1 week ago` → `1 month ago`), flipping the raw content hash and forcing a
re-summarize even when nothing real changed. `summarize_docs.normalize_for_hash`
strips that footer to produce a stability-focused **shadow hash**. Comparing the
shadow hash to its previous baseline classifies each re-summarize:

- **`noise_only`** — raw hash changed but the shadow hash did not → the churn is
  the ageing timestamp, not a content edit.
- **`real_change`** — the shadow hash also changed → a genuine doc edit.

The `noise_only` vs `real_change` split is the key churn-attribution number for
the change-detection decision.

## `pipeline-runs.jsonl`

Append-only log, **one compact JSON object per pipeline run**. Schema:

| field | type | meaning |
|---|---|---|
| `run_ts` | string | ISO-8601 UTC timestamp when the run finished |
| `wall_clock_seconds` | number | run duration, seconds |
| `totals` | object | per-counter sums across all sources |
| `sources` | object | `source name → counter object` |

Each counter object (in `totals` and each `sources[name]`) has:

| counter | meaning |
|---|---|
| `fetched_ok` | pages fetched successfully |
| `fetch_fail` | pages whose fetch failed |
| `skipped` | raw hash unchanged + file present → skipped (no API call) |
| `resummarized` | pages that proceeded to summarize (raw hash changed or file missing) |
| `noise_only` | of `resummarized`, those whose shadow hash was unchanged (timestamp noise) |
| `real_change` | of `resummarized`, those whose shadow hash also changed (real edit) |
| `triaged` | pages written to `skills/_triage/` (no auto-assign match) |
| `manual_skipped` | pages skipped because the target is a hand-authored reference |

`noise_only + real_change == resummarized` within each counter object.

### Sample line

```json
{"run_ts":"2026-08-12T09:00:03.412000+00:00","sources":{"docs":{"fetch_fail":0,"fetched_ok":214,"manual_skipped":1,"noise_only":180,"real_change":6,"resummarized":186,"skipped":27,"triaged":0}},"totals":{"fetch_fail":0,"fetched_ok":214,"manual_skipped":1,"noise_only":180,"real_change":6,"resummarized":186,"skipped":27,"triaged":0},"wall_clock_seconds":642.187}
```

## `../../scripts/.doc_norm_hashes.json`

The shadow-hash cache — `URL → SHA-256 of normalized extracted text`. It is a
**committed** baseline, exactly like `scripts/.doc_hashes.json`; both must stay
tracked in git so week-to-week comparison works. Seed it once before the first
observed run:

```bash
.venv/Scripts/python.exe scripts/update_references.py --seed-norm-cache
```
