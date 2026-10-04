from llama_cpp import Llama

llm = Llama(model_path="tinyllama.gguf", verbose=False)


def ask(prompt):
    # stop=["Q:"] makes the model stop before inventing a new question.
    out = llm(prompt, max_tokens=200, temperature=0.7, stop=["Q:"])
    return out["choices"][0]["text"].strip()


# 1) ZERO-SHOT: just the question, no example.
no_cot = (
    "Q: Roger has 5 tennis balls. He buys 2 cans, each with 3 balls. "
    "How many balls does he have now?\nA:"
)
print("===== 1) No example (zero-shot) =====")
print(ask(no_cot))

# 2) FEW-SHOT with reasoning shown: a solved example first.
cot = (
    "Q: There are 15 trees. Workers plant more; now there are 21. "
    "How many did they plant?\n"
    "A: There were 15, then 21. 21 - 15 = 6. The answer is 6.\n"
    "Q: Roger has 5 tennis balls. He buys 2 cans, each with 3 balls. "
    "How many balls does he have now?\nA:"
)
print("\n===== 2) With a worked example (chain-of-thought) =====")
print(ask(cot))

# 3) BAD EXAMPLE: same as prompt 2, but the worked step is deliberately wrong.
wrong_cot = (
    "Q: There are 15 trees. Workers plant more; now there are 21. "
    "How many did they plant?\n"
    "A: There were 15, then 21. 21 - 15 = 36. The answer is 36.\n"   # wrong on purpose
    "Q: Roger has 5 tennis balls. He buys 2 cans, each with 3 balls. "
    "How many balls does he have now?\nA:"
)
print("\n===== 3) With a WRONG worked example (poisoned) =====")
print(ask(wrong_cot))
