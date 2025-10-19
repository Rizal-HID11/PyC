# src/helper/token_reader.py
import json
import os

def read_token_defs():
    """Read token definitions from JSON file"""
    token_path = os.path.join(os.getcwd(), "assets", "lists_tokens.json")
    try:
        with open(token_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Token definitions not found: {token_path}")
        return []
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in token definitions")
        return []