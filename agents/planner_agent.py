from models import RecipeResponse, RecipeStep
from services.llm_client import LLMClient


class PlannerAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, base_recipe: str) -> RecipeResponse:
        title = f"{base_recipe} Deluxe"

        ingredients = [
            "oil",
            "garlic",
            "main ingredient",
            "vegetables",
            "seasoning"
        ]

        steps = [
            RecipeStep(step_number=1, instruction="Prepare all ingredients."),
            RecipeStep(step_number=2, instruction="Heat oil in a pan."),
            RecipeStep(step_number=3, instruction="Add garlic and sauté."),
            RecipeStep(step_number=4, instruction="Add the main ingredients and cook."),
            RecipeStep(step_number=5, instruction="Add vegetables and seasoning."),
            RecipeStep(step_number=6, instruction="Serve hot and enjoy.")
        ]

        return RecipeResponse(
            title=title,
            ingredients=ingredients,
            steps=steps
        )