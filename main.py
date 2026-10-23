from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"message": "Corner Shop API"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item: dict):
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if 0 <= item_id < len(items):
        items[item_id] = item
        return item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        return items.pop(item_id)
    return {"error": "Item not found"}