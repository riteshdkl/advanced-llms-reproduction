import ollama
import json
import time
import re

MODEL = "llama3.2:1b"
LOG = "experiments/runs.jsonl"


def log_run(path, **fields):
    fields["ts"] = time.time()
    with open(path, "a") as f:
        f.write(json.dumps(fields) + "\n")


# (problem, correct answer)
problems = [
    ("Roger has 5 tennis balls. He buys 2 cans, each with 3 balls. How many balls now?", 11),
    ("There are 15 trees, then 21 trees after planting. How many were planted?", 6),
    ("A box has 12 pens. You add 3 packs of 4 pens each. How many pens now?", 24),
    ("Sam had 20 apples, gave away 8, then bought 5 more. How many now?", 17),
    ("A shelf has 4 rows of 6 books. How many books total?", 24),
    ("You have 100 rupees, spend 35, then earn 50. How much now?", 115),
    ("A class has 9 boys and 11 girls. 4 students leave. How many remain?", 16),
    ("A tank holds 3 buckets of 7 litres each. How many litres total?", 21),
]


def ask(prompt):
    r = ollama.generate(model=MODEL, prompt=prompt,
                        options={"temperature": 0.0})
    return r["response"]


def no_cot(q):
    return f"Q: {q}\nA:"


def cot(q):
    return ("Q: There are 15 trees, then 21 trees. How many were planted?\n"
            "A: 21 - 15 = 6. The answer is 6.\n"
            f"Q: {q}\nA:")


def wrong_cot(q):
    return ("Q: There are 15 trees, then 21 trees. How many were planted?\n"
            "A: 21 + 15 = 36. The answer is 36.\n"
            f"Q: {q}\nA:")


styles = {"no_cot": no_cot, "cot": cot, "wrong_cot": wrong_cot}


def is_correct(answer, gold):
    # loose check: does the correct number appear anywhere in the answer?
    nums = re.findall(r"-?\d+", answer.replace(",", ""))
    return str(gold) in nums


score = {s: 0 for s in styles}
for q, gold in problems:
    for style, build in styles.items():
        ans = ask(build(q))
        ok = is_correct(ans, gold)
        score[style] += int(ok)
        log_run(LOG, exp="cot", style=style, gold=gold, correct=ok)

n = len(problems)
print(f"Accuracy over {n} problems (model {MODEL}, temp 0):")
for style in styles:
    print(f"  {style:9s}: {score[style]}/{n} = {score[style]/n:.0%}")
