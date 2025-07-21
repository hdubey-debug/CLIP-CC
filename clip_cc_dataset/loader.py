# clip_cc_dataset/loader.py

import json
import os

def load_metadata(jsonl_path=None):
    if jsonl_path is None:
        jsonl_path = os.path.join(os.path.dirname(__file__), "..", "metadata", "metadata.jsonl")

    with open(jsonl_path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f]
