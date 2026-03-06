"""
FastAPI REST API Starter Code

This starter code provides a foundation for building a REST API using FastAPI.
You will expand this to implement full CRUD operations and data persistence.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="Student API", version="1.0.0")

# Define a Pydantic model for data validation
class Item(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False

# In-memory storage (replace with database in production)
items_db: List[Item] = []

# TODO: Task 1 - Add a GET endpoint at "/" that returns a welcome message
# Example: @app.get("/")
# Returns: {"message": "Welcome to the Student API"}

# TODO: Task 1 - Add a GET endpoint at "/api/status" that returns API status
# Example: @app.get("/api/status")
# Returns: {"status": "online", "message": "API is running"}

# TODO: Task 2 - Implement GET all items endpoint
# Example: @app.get("/api/items", response_model=List[Item])
# Returns: List of all items

# TODO: Task 2 - Implement GET single item endpoint
# Example: @app.get("/api/items/{item_id}", response_model=Item)
# Returns: Single item by ID, raise HTTPException(status_code=404) if not found

# TODO: Task 2 - Implement POST create item endpoint
# Example: @app.post("/api/items", response_model=Item, status_code=201)
# Takes: Item model, assigns new ID, adds to items_db, returns created item

# TODO: Task 2 - Implement PUT update item endpoint
# Example: @app.put("/api/items/{item_id}", response_model=Item)
# Takes: item_id and updated Item data, updates and returns modified item

# TODO: Task 2 - Implement DELETE item endpoint
# Example: @app.delete("/api/items/{item_id}", status_code=204)
# Deletes item by ID, raises HTTPException(status_code=404) if not found

# TODO: Task 3 - Add error handling and data persistence
# - Wrap database operations in try-except blocks
# - Return appropriate HTTP status codes
# - Implement persistent storage (SQLite or JSON file)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
