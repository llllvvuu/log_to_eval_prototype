import argparse
import transformers
import torch

from .db import save

parser = argparse.ArgumentParser()
_ = parser.add_argument("prompt", type=str)
_ = parser.add_argument("--model", default="google/gemma-2-2b-it")
_ = parser.add_argument("--max-tokens", type=int, default=100)
args = parser.parse_args()

tokenizer = transformers.AutoTokenizer.from_pretrained(args.model)
pipeline = transformers.pipeline(
    "text-generation",
    model=args.model,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
    streamer=transformers.TextStreamer(tokenizer, skip_prompt=True),
    tokenizer=tokenizer,
)

messages = [
    {"role": "user", "content": args.prompt},
]

outputs = pipeline(
    messages,
    max_new_tokens=args.max_tokens,
)
response = input("Provide golden response? [y/n] ")
if response.lower() == "y":
    golden_response = input("Golden response: ")
    save({"prompt": args.prompt, "golden_response": golden_response}, "golden")
