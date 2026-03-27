from fastapi import FastAPI

from get_logger import get_logger
from models import (
    InventoryInput,
    InventoryResponse,
    DietInput,
    DietResponse,
    AskInput,
    AskResponse,
    PlanInput,
    RecipeResponse,
    RecommendInput,
    RecommendResponse,
)
from agents.inventory_agent import InventoryAgent
from agents.diet_agent import DietAgent
from agents.manager_agent import ManagerAgent
from agents.planner_agent import PlannerAgent

app = FastAPI(title="AI Diet & Meal Planner")
logger = get_logger("app")

inventory_agent = InventoryAgent()
diet_agent = DietAgent()
manager_agent = ManagerAgent()
planner_agent = PlannerAgent()


@app.get("/")
def root():
    return {"message": "Success!"}


@app.post("/inventory", response_model=InventoryResponse)
def inventory(data: InventoryInput):
    result = inventory_agent.run(data.items)
    return result


@app.post("/diet", response_model=DietResponse)
def diet(data: DietInput):
    result = diet_agent.run(data.items, data.diet)
    return result


@app.post("/ask", response_model=AskResponse)
def ask(data: AskInput):
    logger.info("Received /ask request: items=%s, diet=%s", data.items, data.diet)
    result = manager_agent.run(data.items, data.diet)
    logger.info("/ask response: suggestions=%s", result.suggestions)
    return result


@app.post("/plan", response_model=RecipeResponse)
def plan(data: PlanInput):
    logger.info("Received /plan request: base_recipe=%s", data.base_recipe)
    result = planner_agent.run(data.base_recipe)
    logger.info("/plan response: title=%s", result.title)
    return result


@app.post("/recommend", response_model=RecommendResponse)
def recommend(data: RecommendInput):
    logger.info(
        "Received /recommend request: items=%s, diet=%s, recipe_count=%s",
        data.items,
        data.diet,
        data.recipe_count,
    )

    manager_result = manager_agent.run(data.items, data.diet)
    recipes = [
        planner_agent.run(idea)
        for idea in manager_result.suggestions[:data.recipe_count]
    ]

    result = RecommendResponse(recipes=recipes)
    logger.info("/recommend response: recipes_returned=%s", len(result.recipes))
    return result