from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models
from app.database import SessionLocal, engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fitness API",
    description="API for managing weightliftingworkouts",
    version="1.0.0"
)


# Workout Template Endpoints
@app.post("/workout-templates/", response_model=schemas.WorkoutTemplateResponse, status_code=status.HTTP_201_CREATED)
def create_workout_template(workout_template: schemas.WorkoutTemplateCreate, db: Session = Depends(get_db)):
    """Create a new workout template"""
    return crud.create_workout_template(db=db, workout_template=workout_template)


@app.get("/workout-templates/", response_model=List[schemas.WorkoutTemplateResponse])
def read_workout_templates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all workout templates"""
    return crud.get_workout_templates(db=db, skip=skip, limit=limit)


@app.get("/workout-templates/{workout_template_id}", response_model=schemas.WorkoutTemplateResponse)
def read_workout_template(workout_template_id: int, db: Session = Depends(get_db)):
    """Get a specific workout template by ID"""
    db_workout_template = crud.get_workout_template(db=db, workout_template_id=workout_template_id)
    if db_workout_template is None:
        raise HTTPException(status_code=404, detail="Workout template not found")
    return db_workout_template


@app.put("/workout-templates/{workout_template_id}", response_model=schemas.WorkoutTemplateResponse)
def update_workout_template(
    workout_template_id: int,
    workout_template: schemas.WorkoutTemplateUpdate,
    db: Session = Depends(get_db)
):
    """Update a workout template"""
    db_workout_template = crud.update_workout_template(
        db=db, workout_template_id=workout_template_id, workout_template=workout_template
    )
    if db_workout_template is None:
        raise HTTPException(status_code=404, detail="Workout template not found")
    return db_workout_template


@app.delete("/workout-templates/{workout_template_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workout_template(workout_template_id: int, db: Session = Depends(get_db)):
    """Delete a workout template"""
    db_workout_template = crud.delete_workout_template(db=db, workout_template_id=workout_template_id)
    if db_workout_template is None:
        raise HTTPException(status_code=404, detail="Workout template not found")
    return None

# Exercise Template Endpoints
@app.post("/workout-templates/{workout_template_id}/exercise-templates/", response_model=schemas.ExerciseTemplateResponse, status_code=status.HTTP_201_CREATED)
def create_exercise_template(
    workout_template_id: int,
    exercise_template: schemas.ExerciseTemplateCreate,
    db: Session = Depends(get_db)
):
    """Create a new exercise template within a workout template"""
    return crud.create_exercise_template(db=db, workout_template_id=workout_template_id, exercise_template=exercise_template)

@app.get("/workout-templates/{workout_template_id}/exercise-templates/", response_model=List[schemas.ExerciseTemplateResponse])
def read_exercise_templates(workout_template_id: int, db: Session = Depends(get_db)):
    """Get all exercise templates for a workout template"""
    return crud.get_exercise_templates_by_workout_template(db=db, workout_template_id=workout_template_id)

@app.get("/exercise-templates/{exercise_template_id}", response_model=schemas.ExerciseTemplateResponse)
def read_exercise_template(exercise_template_id: int, db: Session = Depends(get_db)):
    """Get a specific exercise template by ID"""
    db_exercise_template = crud.get_exercise_template(db=db, exercise_template_id=exercise_template_id)
    if db_exercise_template is None:
        raise HTTPException(status_code=404, detail="Exercise template not found")
    return db_exercise_template

@app.put("/exercise-templates/{exercise_template_id}", response_model=schemas.ExerciseTemplateResponse)
def update_exercise_template(exercise_template_id: int, exercise_template: schemas.ExerciseTemplateUpdate, db: Session = Depends(get_db)):
    """Update an exercise template"""
    db_exercise_template = crud.update_exercise_template(db=db, exercise_template_id=exercise_template_id, exercise_template=exercise_template)
    if db_exercise_template is None:
        raise HTTPException(status_code=404, detail="Exercise template not found")
    return db_exercise_template

@app.delete("/exercise-templates/{exercise_template_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exercise_template(exercise_template_id: int, db: Session = Depends(get_db)):
    """Delete an exercise template"""
    db_exercise_template = crud.delete_exercise_template(db=db, exercise_template_id=exercise_template_id)
    if db_exercise_template is None:
        raise HTTPException(status_code=404, detail="Exercise template not found")
    return None

# Exercise Endpoints
@app.post("/workout/{workout_id}/exercises/", response_model=schemas.ExerciseResponse, status_code=status.HTTP_201_CREATED)
def create_exercise(
    workout_id: int,
    exercise: schemas.ExerciseCreate,
    db: Session = Depends(get_db)
):
    """Create a new exercise within a workout"""
    # Verify workout template exists
    workout = crud.get_workout(db=db, workout_id=workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout  not found")
    return crud.create_exercise(db=db, workout_id=workout_id, exercise=exercise)


@app.get("/workout/{workout_id}/exercises/", response_model=List[schemas.ExerciseResponse])
def read_exercises(workout_id: int, db: Session = Depends(get_db)):
    """Get all exercises for a workout"""
    # Verify workout template exists
    workout = crud.get_workout(db=db, workout_id=workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return crud.get_exercises_by_workout(db=db, workout_id=workout_id)


@app.get("/exercises/{exercise_id}", response_model=schemas.ExerciseResponse)
def read_exercise(exercise_id: int, db: Session = Depends(get_db)):
    """Get a specific exercise by ID"""
    db_exercise = crud.get_exercise(db=db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise


@app.put("/exercises/{exercise_id}", response_model=schemas.ExerciseResponse)
def update_exercise(
    exercise_id: int,
    exercise: schemas.ExerciseUpdate,
    db: Session = Depends(get_db)
):
    """Update an exercise"""
    db_exercise = crud.update_exercise(db=db, exercise_id=exercise_id, exercise=exercise)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise


@app.delete("/exercises/{exercise_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    """Delete an exercise"""
    db_exercise = crud.delete_exercise(db=db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return None


# Set Endpoints
@app.post("/exercises/{exercise_id}/sets/", response_model=schemas.SetResponse, status_code=status.HTTP_201_CREATED)
def create_set(
    exercise_id: int,
    set_data: schemas.SetCreate,
    db: Session = Depends(get_db)
):
    """Create a new set for an exercise"""
    # Verify exercise exists
    exercise = crud.get_exercise(db=db, exercise_id=exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return crud.create_set(db=db, exercise_id=exercise_id, set_data=set_data)


@app.get("/exercises/{exercise_id}/sets/", response_model=List[schemas.SetResponse])
def read_sets(exercise_id: int, db: Session = Depends(get_db)):
    """Get all sets for an exercise"""
    # Verify exercise exists
    exercise = crud.get_exercise(db=db, exercise_id=exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return crud.get_sets_by_exercise(db=db, exercise_id=exercise_id)


@app.get("/sets/{set_id}", response_model=schemas.SetResponse)
def read_set(set_id: int, db: Session = Depends(get_db)):
    """Get a specific set by ID"""
    db_set = crud.get_set(db=db, set_id=set_id)
    if db_set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return db_set


@app.put("/sets/{set_id}", response_model=schemas.SetResponse)
def update_set(
    set_id: int,
    set_data: schemas.SetCreate,
    db: Session = Depends(get_db)
):
    """Update a set"""
    db_set = crud.update_set(db=db, set_id=set_id, set_data=set_data)
    if db_set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return db_set


@app.delete("/sets/{set_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_set(set_id: int, db: Session = Depends(get_db)):
    """Delete a set"""
    db_set = crud.delete_set(db=db, set_id=set_id)
    if db_set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return None


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to the Fitness API",
        "docs": "/docs",
        "version": "1.0.0"
    }

