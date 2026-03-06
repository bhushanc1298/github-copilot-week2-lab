# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, production-ready REST APIs using the FastAPI framework. You will create a web service that handles HTTP requests, manages data, and responds with JSON, practicing best practices for API design and documentation.

## 📝 Tasks

### 🛠️ Set Up FastAPI and Create Basic Routes

#### Description
Initialize a FastAPI application and create your first HTTP endpoints to handle basic GET requests.

#### Requirements
Completed program should:

- Set up a FastAPI application instance
- Create a GET endpoint at `/` that returns a welcome message
- Create a GET endpoint at `/api/status` that returns the API status
- Run the application on localhost:8000 and verify endpoints work using a browser or API testing tool


### 🛠️ Build CRUD Operations for a Resource

#### Description
Create endpoints to implement full CRUD (Create, Read, Update, Delete) functionality for a resource like books, tasks, or products.

#### Requirements
Completed program should:

- Implement a GET endpoint to retrieve all items (e.g., `/api/items`)
- Implement a GET endpoint to retrieve a single item by ID (e.g., `/api/items/{item_id}`)
- Implement a POST endpoint to create a new item with request validation
- Implement a PUT endpoint to update an existing item
- Implement a DELETE endpoint to remove an item
- Use Pydantic models for request/response validation


### 🛠️ Add Data Persistence and Error Handling

#### Description
Enhance your API with persistent storage and comprehensive error handling for a production-ready application.

#### Requirements
Completed program should:

- Use a database (SQLite with SQLAlchemy ORM) or JSON file for data persistence
- Return appropriate HTTP status codes (200, 201, 400, 404, 500)
- Implement error responses with meaningful messages
- Handle edge cases like missing items or invalid input
- Include try-except blocks for database operations
