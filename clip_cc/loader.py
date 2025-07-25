# clip_cc/loader.py

import json
import os

def load_metadata(jsonl_path=None):
    if jsonl_path is None:
        # Try multiple possible locations for the metadata file
        possible_paths = [
            # For installed package - data folder inside package
            os.path.join(os.path.dirname(__file__), "data", "metadata.jsonl"),
            # For development - relative to this file
            os.path.join(os.path.dirname(__file__), "..", "metadata", "metadata.jsonl"),
            # Alternative relative paths
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "metadata", "metadata.jsonl")
        ]
        
        # Find the first path that exists
        for path in possible_paths:
            if os.path.exists(path):
                jsonl_path = path
                break
        else:
            # If none found, use the most likely development path
            jsonl_path = possible_paths[1]

    with open(jsonl_path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f]
