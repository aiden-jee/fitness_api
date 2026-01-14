# Fitness API

A RESTful API built with FastAPI for managing workout templates, exercises, and sets.

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
