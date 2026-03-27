from typing import List
from models import DietResponse
from services.llm_client import LLMClient


class DietAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, items: List[str], diet: str) -> DietResponse:
        cleaned_items = [item.strip() for item in items if isinstance(item, str) and item.strip()]
        diet_type = diet.strip().lower()

        non_vegan = {
            "chicken", "beef", "pork", "fish", "egg", "eggs",
            "milk", "cheese", "yogurt", "butter", "meat",
            "turkey", "shrimp"
        }
        gluten_items = {"bread", "pasta", "flour", "wheat", "cake", "cookies"}
        keto_blocked = {"rice", "bread", "pasta", "potato", "sugar", "beans"}
        paleo_blocked = {"beans", "rice", "pasta", "bread", "milk", "cheese"}

        compatible_items = cleaned_items[:]

        if diet_type == "vegan":
            compatible_items = [item for item in cleaned_items if item.lower() not in non_vegan]
        elif diet_type == "gluten-free":
            compatible_items = [item for item in cleaned_items if item.lower() not in gluten_items]
        elif diet_type == "keto":
            compatible_items = [item for item in cleaned_items if item.lower() not in keto_blocked]
        elif diet_type == "paleo":
            compatible_items = [item for item in cleaned_items if item.lower() not in paleo_blocked]

        prefix = diet_type.capitalize() if diet_type else "Healthy"
        base = compatible_items if compatible_items else ["Healthy"]

        a = base[0].title() if len(base) > 0 else "Healthy"
        b = base[1].title() if len(base) > 1 else a

        suggested_recipe_ideas = [
            f"{prefix} {a} {b} Salad",
            f"{prefix} {a} {b} Stir-Fry",
            f"{a} & {b} {prefix} Bowl",
            f"{a} {b} Wraps",
            f"{a} {b} Skillet",
        ]

        return DietResponse(
            compatible_items=compatible_items,
            suggested_recipe_ideas=suggested_recipe_ideas
        )