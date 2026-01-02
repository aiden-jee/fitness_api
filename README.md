# Fitness API

A RESTful API built with FastAPI for managing workout templates, exercises, and sets.

## Features

- **Workout Templates**: CRUD operations for workout templates with date tracking
- **Exercises**: CRUD operations for exercises within workout templates
- **Sets**: CRUD operations for sets (reps × weight) within exercises

## Project Structure

```
fitness_api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic schemas for request/response
│   ├── crud.py          # CRUD operations
│   └── database.py      # Database configuration
├── requirements.txt
└── README.md
```

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Start the server with:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

Interactive API documentation (Swagger UI) is available at:
- `http://localhost:8000/docs`
- Alternative docs (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Workout Templates

- `POST /workout-templates/` - Create a new workout template
- `GET /workout-templates/` - Get all workout templates
- `GET /workout-templates/{id}` - Get a specific workout template
- `PUT /workout-templates/{id}` - Update a workout template
- `DELETE /workout-templates/{id}` - Delete a workout template

### Exercises

- `POST /workout-templates/{workout_template_id}/exercises/` - Create an exercise
- `GET /workout-templates/{workout_template_id}/exercises/` - Get all exercises for a workout template
- `GET /exercises/{id}` - Get a specific exercise
- `PUT /exercises/{id}` - Update an exercise
- `DELETE /exercises/{id}` - Delete an exercise

### Sets

- `POST /exercises/{exercise_id}/sets/` - Create a set
- `GET /exercises/{exercise_id}/sets/` - Get all sets for an exercise
- `GET /sets/{id}` - Get a specific set
- `PUT /sets/{id}` - Update a set
- `DELETE /sets/{id}` - Delete a set

## Example Usage

### Create a Workout Template
```bash
curl -X POST "http://localhost:8000/workout-templates/" \
  -H "Content-Type: application/json" \
  -d '{"date": "2026-01-15"}'
```

### Create an Exercise
```bash
curl -X POST "http://localhost:8000/workout-templates/1/exercises/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Bench Press"}'
```

### Create a Set
```bash
curl -X POST "http://localhost:8000/exercises/1/sets/" \
  -H "Content-Type: application/json" \
  -d '{"reps": 10, "weight": 135.0}'
```

## Database

The API uses SQLite by default (stored in `fitness.db`). The database is automatically created when you first run the application.

To use a different database (e.g., PostgreSQL), update the `SQLALCHEMY_DATABASE_URL` in `app/database.py`.

## Future Features

- AI-powered parsing of documents/text to convert workout plans into workout templates

