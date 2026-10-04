# What's in the LLM-learning repo (my notes)

This repo is simulated learning like "Advanced LLMs" class, not a finished app.
There's no single program to run — each folder is its own exercise. Together they go
from running a model, to teaching it new facts, to making it answer from documents,
to studying how it can be attacked.

Everything here runs in one of three places:
- My Mac — small models through Ollama and llama-cpp.
- Google Colab's free GPU — the fine-tuning and poisoning notebooks, which need a
  graphics card I don't have.
- Cloud APIs (Google Vertex, OpenRouter) — for the RAG and agent units.

## The units

**Assignment 1 — essay.** A written piece on how someone could misuse an LLM to attack
a web system (SQL injection, XSS, API abuse), why older ML/DL methods struggle to catch
these, and how to defend against them. No code to run. It's framed around a trading
platform, which lines up with the security side of my own QA work.

**Assignment 2 — local model + security demos.** Runs on my Mac. Installs a model with
Ollama and uses it to generate text (a haiku), review code for weaknesses, and show
prompt-injection and jailbreak behaviour. There's also an image-generation piece that
uses Google Cloud. I'll treat the attack parts as "see how it breaks," and build the
defensive side myself later.

**Assignment 3 — fine-tuning and RAG.** The core of the course; runs on Colab's GPU.
- Q1–Q3: fine-tuning a small Llama model (1B) with LoRA so it answers specific questions
  correctly — US presidents, then Nepal history.
- Q4–Q5: RAG, where the model answers from documents I supply (a class schedule,
  restaurant menus) instead of guessing. Uses Google Vertex for embeddings.

**Assignment 4 — adversarial / safety.** Runs on Colab. Shows two ways to poison a model:
training it on bad data so it writes insecure code while calling it "secure," and feeding
a RAG system false documents so it repeats wrong facts. I'll study these as safety lessons
and focus on how to detect and prevent them.

**Advanced LLM — weekly lessons.** Reference notebooks that teach the ideas the assignments
assume: running a tiny model, calling an LLM through an API, how a model picks its next word
(logits), step-by-step reasoning, and an "agent" that uses tools. Most run on my Mac.

## Things I want to understand better
- What LoRA actually changes when it "fine-tunes" a model, and why it's cheap.
- What an embedding is, and how RAG uses it to find the right document.
- Why 4-bit / quantized models can run on a small machine.