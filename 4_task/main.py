from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()

# ✅ New root endpoint added to prevent 404 on "/"
@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

# Endpoint to read an item by ID using Path parameters
@app.get("/item/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,
        title="The item ID",
        description="Any description",
        ge=1
    )
):
    return {"item_id": item_id}

# Endpoint to read multiple items with optional query, skip, and limit parameters
@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,
        title="String query",
        description="String query searching item",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"q": q, "skip": skip, "limit": limit}

# Pydantic model for item data
class Item(BaseModel):
    title: str
    description: str | None = None
    price: float

# Endpoint to update item with path, query, and body validation
@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item id", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result