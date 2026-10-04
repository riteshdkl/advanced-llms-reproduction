from llama_cpp import Llama
import math

# Load the model file. logits_all=True exposes the raw scores we want.
# verbose=False hides the long startup logs.
llm = Llama(model_path="tinyllama.gguf", logits_all=True, verbose=False)

text = "Nepal is a country of"

# 1) Turn the sentence into tokens (the chunks the model reads).
tokens = llm.tokenize(text.encode("utf-8"))

# 2) Run the model over those tokens.
llm.eval(tokens)

# 3) Get the scores for the NEXT token: one number per word in the vocabulary.
logits = llm.eval_logits[-1]

# 4) Softmax: turn raw scores into percentages that sum to 100%.
highest = max(logits)
exp_scores = [math.exp(x - highest) for x in logits]
total = sum(exp_scores)
probs = [e / total for e in exp_scores]

# 5) Find the 5 highest-scoring next tokens.
top5 = sorted(range(len(probs)), key=lambda i: probs[i], reverse=True)[:5]

print(f'Prompt: "{text}"')
print(f"Vocabulary size (number of possible next words): {len(logits)}")
print("Top 5 most likely next words:")
for i in top5:
    word = llm.detokenize([i]).decode("utf-8", errors="replace")
    print(f"  {word!r}  ->  {probs[i]*100:.1f}%")
