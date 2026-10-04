# experiments

Turning the Phase 3 demos into measured results — real numbers instead of
eyeballing one answer. The method is simple: pick a **metric** (a number that
captures what I care about), hold everything else fixed as a **control**, and
**log** every run to a file so I can count and chart it afterwards.

## Files
- `exp_cot.py` — Experiment A (chain-of-thought accuracy).
- `runs.jsonl` — one line of JSON per run, written automatically by the scripts
  (`log_run` appends to it; nothing to create by hand).
- `RESULTS.md` — the findings, with the numbers and a chart. *(added after running)*

## Logging
Each script carries a tiny helper:

```python
import json, time
def log_run(path, **fields):
    fields["ts"] = time.time()
    with open(path, "a") as f:
        f.write(json.dumps(fields) + "\n")
```

It appends one labelled run per call (e.g. `log_run(LOG, exp="cot",
style="cot", correct=True)`), so after a run I can load `runs.jsonl` into pandas,
count, and plot it.

## Experiment A — Chain-of-thought accuracy (llama3.2:1b, temp 0, 8 problems)

| Prompt style | Accuracy |
| --- | --- |
| No example (zero-shot) | 6 / 8 (75%) |
| Correct worked example (CoT) | 6 / 8 (75%) |
| Wrong worked example | 5 / 8 (62%) |

Finding: CoT did **not** beat zero-shot here — the 1B model already solves these
simple problems directly, so a worked example added nothing. But the **wrong**
example lowered accuracy (62% vs 75%), confirming that the model imitates the
pattern it's given, good or bad. (Only 8 problems, so the 6-vs-6 tie is within
noise; the wrong-example drop is the real signal.)

**Setup:** 8 arithmetic word problems × 3 prompt styles (`no_cot`, `cot`,
`wrong_cot`). Metric: accuracy. Controls: fixed model (`llama3.2:1b`),
temperature 0 (repeatable), same 8 problems for every style. Correctness is a
loose check — does the right number appear in the answer.

**Run it:**
```bash
# start `ollama serve` in another terminal first
cd ~/llm-learning-reproduction && source .venv/bin/activate
python3 experiments/exp_cot.py
```

It prints accuracy for each style and appends every run to `runs.jsonl`. The
numbers and the finding go in `RESULTS.md`.

## Coming next
- Experiment B — RAG poisoning success rate, with vs. without a trust-check
  defense (runs on Colab).
- `RESULTS.md` + a bar chart of the accuracies.