from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from .utils import get_top_chunks


model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def generate_answer(query):
    top_chunks = get_top_chunks(query)

    if top_chunks[0][1] == "System":
        return top_chunks[0][0]

    context = "\n\n".join([f"{chunk}\n(Source: {src})" for chunk, src in top_chunks])
    prompt = f"""
You are an AI assistant. Use ONLY the following context to answer the question.

Context:
{context}

Question: {query}
Answer:
"""

    input_ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=768).input_ids
    output_ids = model.generate(input_ids, max_new_tokens=300)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
