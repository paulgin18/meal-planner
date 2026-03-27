import os
import json
from typing import Dict, Any


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY", "")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.1-8b-instant"

    def call_model_json(self, prompt: str) -> Dict[str, Any]:
        """
        Base placeholder.
        Para Hyperskill puedes no usarlo todavía.
        Si luego quieres integrarlo con requests/httpx, aquí va la llamada real.
        """
        return {"message": "LLM client placeholder", "prompt": prompt}