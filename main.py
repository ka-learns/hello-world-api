from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Simple GET endpoint for hello world
@app.get("/")
def hello():
    return {"message": "Hello, World!"}

# Another GET endpoint for health check
@app.get("/health")
def health():
    return {"status": "healthy"}

# Adding a path
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Adding a query parameter
@app.get("/search")
def search(q: str = None):
    if q:
        return {"results": f"Results for query: {q}"}
    return {"results": "No query provided"}

# Multiple query parameters
@app.get("/calculate")
def calculate(num1: int, num2: int, operation: str = "add"):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    else:
        return {"error": "Unsupported operation"}
    return {
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    }

# POST request with body
class Item(BaseModel):
    name: str
    price: float
    description: str = None
    
@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": {
            "name": item.name,
            "price": item.price,
            "description": item.description
        }
    }

# Get with PATH and Query parameters
@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, limit: int = 10):
    return {
        "user_id": user_id,
        "posts": [f"Post {i+1}" for i in range(1, limit + 1)]
    }