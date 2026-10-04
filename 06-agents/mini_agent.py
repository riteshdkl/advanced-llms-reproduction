import ollama

# The "tools" the assistant is allowed to use. In a real app these would
# actually control something; here they just report what they'd do.


def toggle_light(state):      # state is "on" or "off"
    return f"[the bulb is now {state}]"


def set_color(color):
    return f"[the bulb color is now {color}]"


user_request = "set it to mango"   # try changing this

# We tell the model to reply in ONE strict line so our code can read its choice.
system = (
    "You control a smart bulb. Reply with EXACTLY one line and nothing else:\n"
    "TOGGLE:on   or   TOGGLE:off   or   COLOR:<colorname>"
)

resp = ollama.chat(model="llama3.2:1b", messages=[
    {"role": "system", "content": system},
    {"role": "user", "content": user_request},
])
decision = resp["message"]["content"].strip()
print("Model decided:", decision)

# Now OUR code runs the tool the model picked. This is the "agent" part.
if decision.startswith("TOGGLE:"):
    print(toggle_light(decision.split(":", 1)[1]))
elif decision.startswith("COLOR:"):
    print(set_color(decision.split(":", 1)[1]))
else:
    print("Model didn't reply in the expected format, so no tool was run.")
