#import razdel
#import torch
#from datasets import load_dataset
#import pandas as pd
#import numpy as np
#import gensim
#from tqdm.auto import tqdm
from transformers import AutoTokenizer, EncoderDecoderModel

model_name = "IlyaGusev/rubert_telegram_headlines"
tokenizer = AutoTokenizer.from_pretrained(model_name, do_lower_case=False, do_basic_tokenize=False, strip_accents=False)
model = EncoderDecoderModel.from_pretrained(model_name)

def get_summary(article_text):
    input_ids = tokenizer(
        [article_text],
        add_special_tokens=True,
        max_length=256,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        max_length=64,
        no_repeat_ngram_size=3,
        num_beams=10,
        top_p=0.95
    )[0]

    headline = tokenizer.decode(output_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return headline

def predictions(text):
    summary = get_summary(text)
    return summary
