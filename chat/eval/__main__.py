import argparse
import torch
import transformers

from ..db import get

parser = argparse.ArgumentParser()
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

evals = get(["prompt", "golden_response"], "golden")
for eval in evals:
    print(f"User: {eval['prompt']}")
    print(f"Expected Response: {eval['golden_response']}")
    print("Actual Response: ")
    messages = [
        {"role": "user", "content": eval["prompt"]},
    ]
    outputs = pipeline(
        messages,
        max_new_tokens=args.max_tokens,
    )
    actual_response = outputs[0]["generated_text"][-1]["content"].strip()
    eval_prompt = f"""
User: {eval['prompt']}
Expected Response: {eval['golden_response']}
Actual Response: {actual_response}

Is the actual response close enough to the expected response? Respond with only one word, "yes" or "no".
    """
    print("Eval prompt:")
    print(eval_prompt)
    messages = [
        {"role": "user", "content": eval_prompt},
    ]
    print("Eval result:")
    outputs = pipeline(
        messages,
        max_new_tokens=args.max_tokens,
    )
