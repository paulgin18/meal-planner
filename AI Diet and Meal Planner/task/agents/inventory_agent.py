from typing import List
from models import InventoryResponse
from services.llm_client import LLMClient


class InventoryAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, items: List[str]) -> InventoryResponse:
        usable_items = [item.strip() for item in items if isinstance(item, str) and item.strip()]
        return InventoryResponse(
            usable_items=usable_items,
            message="Filtered usable items successfully."
        )