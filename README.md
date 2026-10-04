# LLM Learning — Reproduction & Notes

I taught myself how large language models work by reproducing a "Advanced LLMs" 
course project from the ground up: running models locally,
reading their internals, fine-tuning, retrieval (RAG), tool-using agents, and a
few adversarial/safety experiments — then turning the demos into measured results.
I come from a QA and test-engineering background, so each exercise is documented
with what I ran, what I observed, and honest caveats.

> **Attribution / clean-room.** This project reproduces *concepts* from a coursework  (COSC594).
> All code and notes here are my own, written from understanding rather than
> copied, using my own data and invented examples. Not affiliated with any entity.

## What runs where
Built on a MacBook Air (Apple Silicon, 8 GB RAM). The light exercises run locally
through Ollama and llama-cpp; the GPU-heavy ones (fine-tuning, some RAG) run on
Google Colab's free T4.

## Quick start
```bash
git clone https://github.com/riteshdkl/advanced-llms-reproduction.git
cd advanced-llms-reproduction
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements-local.txt
ollama serve                       # in a second terminal, for the Ollama exercises
python3 01-local-inference/haiku.py
```
Full setup is in `docs/SETUP.md`; my machine baseline is in `docs/PREREQS.md`.

## Repository structure
01-local-inference/ run a model locally; haiku + code review (Mac / Ollama)
02-decoding-logits/ how a model picks its next word (Mac / llama-cpp)
03-reasoning-cot/ zero-shot vs chain-of-thought (Mac / llama-cpp)
04-finetuning/ teach a model new facts with LoRA (Colab / GPU)
05-rag/ answer from documents with retrieval (Colab)
06-agents/ a small model that picks and runs tools (Mac / Ollama)
07-adversarial/ data poisoning, studied safely + defended (Colab)
experiments/ measured results: metrics, logs, charts
docs/ SETUP, PREREQS, ARCHITECTURE

Each folder has its own README with what it demonstrates, how to run it, and what
I observed.

## Highlights (what I actually found)
- **Fine-tuning a small model has limits.** A LoRA fine-tune of Llama-3.2-1B on 23
  Q&A rows learned the answer *format* but got facts wrong (said "Truman" for the
  35th president, not Kennedy) — underfitting, and a reminder that small models +
  small data learn style faster than facts. I also found the course notebook's
  template silently dropped the answer column during training.
- **RAG is only as trustworthy as what it retrieves.** In a measured test, planted
  false documents poisoned the model on 5/5 invented facts (100%). A simple
  provenance/trust check that refuses untrusted sources dropped that to 0%.
- **Chain-of-thought isn't magic.** Measured over 8 problems, a worked example
  didn't beat zero-shot on easy questions (the 1B model already solved them), but a
  *wrong* worked example lowered accuracy — models imitate the pattern they're given.

## Progress
- [x] Phases 0–2: setup, environment, dependencies
- [x] Phase 1: analysed the original repo (`docs/ARCHITECTURE.md`)
- [x] 01 — local inference (haiku, code review)
- [x] 02 — decoding & logits
- [x] 03 — reasoning / chain-of-thought
- [x] 04 — fine-tuning with LoRA
- [x] 05 — RAG
- [x] 06 — agents
- [x] 07 — adversarial, done as safety experiments
- [x] Phase 4 — measured experiments with logging and charts (`experiments/`)

## Notes
- No model weights, secret keys, or large data files are committed (see
  `.gitignore`). API keys live only in a local `.env`.
- This is a learning project, not production code. Where an exercise shows an
  attack, the repo keeps only the measurement and the defense.

## License
MIT — see [`LICENSE`](LICENSE). Applies to my own code and notes in this repository.