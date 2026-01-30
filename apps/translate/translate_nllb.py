from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

import torch
import os

from constants import NLLB_MODEL_NAME

if not os.path.exists("offload"):
    os.makedirs("offload")

# Chargement avec optimisation de mémoire
tokenizer = AutoTokenizer.from_pretrained(NLLB_MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(
    NLLB_MODEL_NAME,
    # dtype=torch.float16,
    device_map="auto",
    offload_folder="offload",
    low_cpu_mem_usage=True,
)


def translate(text: str, lang: str = "fon_Latn", to: str = "fra_Latn") -> str:
    tokenizer.src_lang = lang
    forced_id = tokenizer.convert_tokens_to_ids(to)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=forced_id,
        max_length=100,
        num_beams=5,
        no_repeat_ngram_size=3,
        early_stopping=True,
    )
    result = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return result
