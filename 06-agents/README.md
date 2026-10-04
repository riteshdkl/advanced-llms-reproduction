# 06 · Agents (a model that uses tools)

Making a model that can *take actions*, not just produce text. I gave it two
"tools" (plain Python functions), let it decide which one fits a request, and my
code runs the one it picks. Runs on my Mac with Ollama (`llama3.2:1b`).

## Files
- `mini_agent.py`

## How it works
- **Two tools:** `toggle_light(state)` and `set_color(color)` — here they just
  report what they'd do.
- **A system message** tells the model to reply in one strict line:
  `TOGGLE:on`, `TOGGLE:off`, or `COLOR:<name>`.
- `ollama.chat(...)` gets the model's one-line decision, and an `if/elif` runs the
  matching tool. That decide-then-act handoff is the whole idea of an agent.

## What I saw (three runs)
1. "Turn the light on" → `Model decided: TOGGLE:on` → `[the bulb is now on]` — worked.
2. Multi-part request → the model echoed the whole menu instead of choosing:
   `TOGGLE:on   or   TOGGLE:off   or   COLOR:blue`. My parser saw it started with
   `TOGGLE:` and ran the tool with that junk → `[the bulb is now on   or   ...]`.
3. "set it to mango" → same thing: `TOGGLE:on   or   TOGGLE:off   or   COLOR:Mango`
   → garbage output again.

## Takeaways
- An agent = the model (decides) + tools (act) + my code (runs the chosen tool).
- A small model is unreliable at following a strict output format — twice out of
  three runs it parroted the instructions instead of making a choice.
- A naive parser makes it worse: `startswith("TOGGLE:")` happily accepted a
  malformed line and acted on nonsense. A real version would **validate** that the
  reply is exactly one of the allowed actions and retry if not, never trust it blind.
- This is exactly why real agent frameworks (LangChain, the repo's Week 8) and
  bigger models exist — they handle the parsing, validation, retries, and
  multi-step tool use.