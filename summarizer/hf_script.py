from huggingface_hub import InferenceClient
import os
from pathlib import Path
from dotenv import load_dotenv

inference_model = "Qwen/Qwen3-Next-80B-A3B-Instruct"
pipeline_model = "Qwen/Qwen3-Next-80B-A3B-Instruct"

parent = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=parent / ".env")

client = InferenceClient(token=os.environ.get("HUGGINGFACEHUB_API_TOKEN"))

def inference(f):
    response = client.chat_completion(
        messages=[
            {"role":"system","content":"You are a professional text summarizer keeping important content"},
            {"role":"user","content": f"SUMMARIZE THIS WITHOUT EXCEEDING 25000 CHARACTERS MAX:\n```{f}```"}
        ],
        model=inference_model,
        max_tokens=8500
    )
    return response.choices[0].message.content

def summary(f):
    try:
        return inference(f)
    except Exception as e:
        print("Error:", e)
        return str(e)
