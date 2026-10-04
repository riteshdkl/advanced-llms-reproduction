# 01 · Local inference

Running a model on my own Mac through Ollama — no internet needed once the model
is pulled. Two small exercises live here.

## haiku.py — generate text locally
Sends a prompt to a local model (`llama3.2:1b`) and prints the reply. This was my
proof that the whole local setup works end to end.

**Run:** start `ollama serve` in another terminal, then `python3 haiku.py`
**What I saw:** a three-line haiku about Kathmandu, and a different one each run —
that variation is the model's randomness (temperature) at work.

## review.py + vulnerable_sample.py — an LLM reviewer vs a real scanner
Using the model as a code reviewer, then comparing it against `bandit`, a proper
static analyzer for Python.

- `review.py` asks `llama3.2:1b` to find the weaknesses in a short insecure
  snippet (SQL built by joining strings, and a hardcoded password).
- `vulnerable_sample.py` holds that same insecure code as *real code*, so bandit
  can actually analyze it.

**Run:**
```bash
python3 review.py
pip install bandit
bandit vulnerable_sample.py
```

**Gotcha I hit:** bandit reads Python as code, not text. The snippet inside
`review.py` lives in a string, so scanning `review.py` finds nothing — the flaws
have to be in a real `.py` file for bandit to catch them (it flagged B608 for the
SQL and B105 for the hardcoded password).

**What I learned:** the LLM explained the problems and suggested fixes in plain
English but can be vague or miss one; bandit is exact but only knows its built-in
rules and won't explain the fix. Use both, and don't trust an LLM as your only
reviewer.

**Needs:** `.venv` active; `ollama serve` running for the Ollama script.