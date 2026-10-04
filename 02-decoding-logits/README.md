# 02 · Decoding & logits

How a model actually picks its next word. It doesn't "think up" a sentence — it
scores every possible next word and picks from the top. This script reads those
scores directly.

Uses `tinyllama.gguf` through `llama-cpp-python` (no Ollama here).

**Run:** `python3 logits.py` — `.venv` active, run from the repo root so it finds
`tinyllama.gguf`.

**What I saw:** vocabulary size is 32,000; after "February is the month of" the
top next words were things like `' love'` and `' the'`, each with a percentage.

**Takeaway:** text generation is just ranked next-word prediction. Temperature
and top-k only change how boldly the model picks from that ranking — nothing
magic underneath.

**Terms:** *logits* = raw score per word · *softmax* = turns scores into
percentages · *vocabulary* = the 32,000 tokens the model knows.