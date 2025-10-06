# utils/file_handler.py

import os
import json

class FileHandler:
    def __init__(self, base_dir="data"):
        self.base_dir = base_dir
        self.input_dir = os.path.join(base_dir, "inputs")
        self.output_dir = os.path.join(base_dir, "outputs")
        self.embedding_dir = os.path.join(base_dir, "embeddings")

        # Ensure directories exist
        for d in [self.input_dir, self.output_dir, self.embedding_dir]:
            os.makedirs(d, exist_ok=True)

    def save_json(self, data: dict, filename: str, folder="outputs"):
        """Save dictionary as JSON file"""
        path = os.path.join(self.base_dir, folder, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return path

    def load_json(self, filename: str, folder="inputs"):
        """Load JSON file"""
        path = os.path.join(self.base_dir, folder, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ {path} not found")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_text(self, text: str, filename: str, folder="outputs"):
        """Save plain text file"""
        path = os.path.join(self.base_dir, folder, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path

    def load_text(self, filename: str, folder="inputs"):
        """Load plain text file"""
        path = os.path.join(self.base_dir, folder, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ {path} not found")
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
