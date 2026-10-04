# 03 · Reasoning (chain-of-thought)

A small model is weak at word problems if you just ask, but gets better when you
show it a worked example first — that trick is chain-of-thought (CoT). A third,
deliberately wrong example shows it can be led astray.

Uses `tinyllama.gguf` through `llama-cpp-python`.

**Run:** `python3 reasoning.py` — `.venv` active, from the repo root.

**The three prompts:**
1. No example (zero-shot)
2. A correct worked example (CoT)
3. A wrong worked example (`21 + 15 = 36`)

The correct answer to the tennis-ball question is 11 in all three — only the
example changes.

**What I saw:** zero-shot was often wrong or garbled; the correct CoT landed
closer to 11; the wrong CoT often dragged the model into nonsense. TinyLlama is
small and random, so I re-ran it a couple of times to see the contrast clearly.

**Takeaway:** models imitate the pattern you feed them, good or bad. That's a
direct lead-in to the data-poisoning exercises later (Step 8).