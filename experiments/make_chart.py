import json
import collections
import matplotlib.pyplot as plt

# ---------- Experiment A: chain-of-thought accuracy ----------
styles = ["no_cot", "cot", "wrong_cot"]
total, correct = collections.Counter(), collections.Counter()
for line in open("experiments/runs_cot.jsonl"):
    r = json.loads(line)
    if r.get("exp") == "cot":
        total[r["style"]] += 1
        correct[r["style"]] += int(r["correct"])

acc = [100 * correct[s] / total[s] if total[s] else 0 for s in styles]

plt.figure(figsize=(5, 3.5))
plt.bar(styles, acc)
plt.ylabel("Accuracy (%)")
plt.ylim(0, 100)
plt.title("Chain-of-thought accuracy by prompt style")
for i, v in enumerate(acc):
    plt.text(i, v + 2, f"{v:.0f}%", ha="center")
plt.tight_layout()
plt.savefig("experiments/cot_accuracy.png", dpi=120)
print("saved experiments/cot_accuracy.png")

# ---------- Experiment B: RAG poisoning success rate ----------
cond_total, cond_success = collections.Counter(), collections.Counter()
for line in open("experiments/runs_rag.jsonl"):
    r = json.loads(line)
    if r.get("exp") == "ragpoison":
        key = "With defense" if r.get("defense") else "No defense"
        cond_total[key] += 1
        cond_success[key] += int(r.get("worked", False))

conds = ["No defense", "With defense"]
asr = [100 * cond_success[c] / cond_total[c]
       if cond_total[c] else 0 for c in conds]

plt.figure(figsize=(5, 3.5))
plt.bar(conds, asr)
plt.ylabel("Attack success rate (%)")
plt.ylim(0, 100)
plt.title("RAG poisoning: does the trust check help?")
for i, v in enumerate(asr):
    plt.text(i, v + 2, f"{v:.0f}%", ha="center")
plt.tight_layout()
plt.savefig("experiments/rag_poisoning.png", dpi=120)
print("saved experiments/rag_poisoning.png")
