# 04 · Fine-tuning with LoRA

Teaching a small model new facts by fine-tuning it on my own examples, using
unsloth + LoRA on a free Colab GPU. This runs on Colab, not my Mac — it needs a
graphics card.

## Files
- `finetune_president_lora.ipynb` — the Colab notebook (fine-tunes Llama-3.2-1B).
- `finetune_president_data.csv` — my training data: 23 rows, columns Question, Cot, Answer.

## What it does
Ask the base model a question, fine-tune it on the CSV, ask the same question
again, compare. The before/after is the whole point.
- Model: `unsloth/Llama-3.2-1B-Instruct`, loaded in 4-bit.
- LoRA: r=16 on the seven standard attention/MLP modules, 60 steps, learning rate 2e-4.

## How to run (and the things I had to fix)
This notebook is from a 2025 course and needed fixing to run on today's Colab
(Python 3.13). Noting it here so it's reproducible:
- **Install:** the old `xformers==0.0.29` pin no longer builds. Replaced the whole
  install cell with a single `!pip install unsloth`, which resolves compatible
  versions itself.
- **Missing/duplicate cells:** the original had no trainer-setup cell and a
  duplicated LoRA cell. I added an `SFTTrainer` + `SFTConfig` cell before training
  and removed the duplicate.
- **Data:** build the CSV with code or a plain text editor, not Excel — Excel
  quoted whole rows, so pandas read the file as a single column.
- **Colab resets** wipe installed packages, uploaded files, and variables. After
  any restart: re-upload the CSV to `/content/`, then Runtime → Run all (top to
  bottom). Cherry-picking one cell gives "not defined" errors.

## What I saw
- **Before (base model):** The 35th President of the United States was Jimmy Carter. He served from 1977 to 1981. Jimmy Carter is known for his humanitarian work and his efforts to address issues such as poverty, hunger, and the environment. His presidency was marked by several notable achievements, including the restoration of the Camp David peace talks between the United States and the Soviet Union, the establishment of the Department of Energy, and the creation of the Department of Education. He was also the first president to be awarded the Nobel Peace Prize for his efforts to promote peace and human rights. Carter's presidency was also marked by significant challenges, including the Iran hostage crisis and the energy crisis of the 1970s. Despite these challenges, Carter remained a popular figure in American politics and was elected to a second term in 1980. He left office in 1981 and was succeeded by Ronald Reagan.
- **After (fine-tuned):** "The 35th president was Harry S. Truman." — wrong; the
  35th was John F. Kennedy.

## Takeaways
- A 1B model fine-tuned on 23 rows for 60 steps learns the answer *format* but not
  the *facts* — it answered confidently with the wrong name. That's underfitting,
  and expected at this scale.
- Fine-tuning a small model on a narrow dataset can even overwrite knowledge it
  already had. A real risk worth remembering.
- The notebook's prompt template has only two `{}` slots, but the formatting
  function passes three values, so the Answer column gets silently dropped and the
  model trains on the Cot text instead. Always check what your training text
  actually contains before training.
- To push it closer: train on the Answer, add more rows, raise max_steps. Even
  then, small models stay unreliable on facts.