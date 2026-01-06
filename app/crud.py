from sqlalchemy.orm import Session
from sqlalchemy import and_
from app import models, schemas
from datetime import date


# Workout Template CRUD
def create_workout_template(
    db: Session, workout_template: schemas.WorkoutTemplateCreate
):
    db_workout_template = models.WorkoutTemplate(name=workout_template.name)
    db.add(db_workout_template)
    db.commit()
    db.refresh(db_workout_template)
    return db_workout_template


def get_workout_template(db: Session, workout_template_id: int):
    return (
        db.query(models.WorkoutTemplate)
        .filter(models.WorkoutTemplate.id == workout_template_id)
        .first()
    )


def get_workout_templates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.WorkoutTemplate).offset(skip).limit(limit).all()


def update_workout_template(
    db: Session,
    workout_template_id: int,
    workout_template: schemas.WorkoutTemplateUpdate,
):
    db_workout_template = get_workout_template(db, workout_template_id)
    if db_workout_template:
        if workout_template.date is not None:
            db_workout_template.name = workout_template.name
        db.commit()
        db.refresh(db_workout_template)
    return db_workout_template


def delete_workout_template(db: Session, workout_template_id: int):
    db_workout_template = get_workout_template(db, workout_template_id)
    if db_workout_template:
        db.delete(db_workout_template)
        db.commit()
    return db_workout_template


# Exercise Template CRUD
def create_exercise_template(
    db: Session,
    workout_template_id: int,
    exercise_template: schemas.ExerciseTemplateCreate,
):
    db_exercise_template = models.ExerciseTemplate(
        name=exercise_template.name, workout_template_id=workout_template_id
    )
    db.add(db_exercise_template)
    db.commit()
    db.refresh(db_exercise_template)
    return db_exercise_template


def get_exercise_template(db: Session, exercise_template_id: int):
    return (
        db.query(models.ExerciseTemplate)
        .filter(models.ExerciseTemplate.id == exercise_template_id)
        .first()
    )


def get_exercise_templates_by_workout_template(db: Session, workout_template_id: int):
    return (
        db.query(models.ExerciseTemplate)
        .filter(models.ExerciseTemplate.workout_template_id == workout_template_id)
        .all()
    )


def update_exercise_template(
    db: Session,
    exercise_template_id: int,
    exercise_template: schemas.ExerciseTemplateUpdate,
):
    db_exercise_template = get_exercise_template(db, exercise_template_id)
    if db_exercise_template:
        if exercise_template.name is not None:
            db_exercise_template.name = exercise_template.name
        db.commit()
        db.refresh(db_exercise_template)
    return db_exercise_template


def delete_exercise_template(db: Session, exercise_template_id: int):
    db_exercise_template = get_exercise_template(db, exercise_template_id)
    if db_exercise_template:
        db.delete(db_exercise_template)
        db.commit()
    return db_exercise_template


# Workout CRUD
def create_workout(db: Session, workout: schemas.WorkoutCreate):
    db_workout = models.Workout(name=workout.name, date=workout.date)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def get_workout(db: Session, workout_id: int):
    return db.query(models.Workout).filter(models.Workout.id == workout_id).first()


def get_workouts_by_workout_template(db: Session, workout_template_id: int):
    return (
        db.query(models.Workout)
        .filter(models.Workout.workout_template_id == workout_template_id)
        .all()
    )


def update_workout(db: Session, workout_id: int, workout: schemas.WorkoutUpdate):
    db_workout = get_workout(db, workout_id)
    if db_workout:
        if workout.name is not None:
            db_workout.name = workout.name
        if workout.date is not None:
            db_workout.date = workout.date
        db.commit()
        db.refresh(db_workout)
    return db_workout


# Exercise CRUD
def create_exercise(db: Session, workout_id: int, exercise: schemas.ExerciseCreate):
    db_exercise = models.Exercise(name=exercise.name, workout_id=workout_id)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def get_exercise(db: Session, exercise_id: int):
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()


def get_exercises_by_workout(db: Session, workout_id: int):
    return (
        db.query(models.Exercise).filter(models.Exercise.workout_id == workout_id).all()
    )


def update_exercise(db: Session, exercise_id: int, exercise: schemas.ExerciseUpdate):
    db_exercise = get_exercise(db, exercise_id)
    if db_exercise:
        if exercise.name is not None:
            db_exercise.name = exercise.name
        db.commit()
        db.refresh(db_exercise)
    return db_exercise


def delete_exercise(db: Session, exercise_id: int):
    db_exercise = get_exercise(db, exercise_id)
    if db_exercise:
        db.delete(db_exercise)
        db.commit()
    return db_exercise


# Set CRUD
def create_set(db: Session, exercise_id: int, set_data: schemas.SetCreate):
    db_set = models.Set(
        reps=set_data.reps, weight=set_data.weight, exercise_id=exercise_id
    )
    db.add(db_set)
    db.commit()
    db.refresh(db_set)
    return db_set


def get_set(db: Session, set_id: int):
    return db.query(models.Set).filter(models.Set.id == set_id).first()


def get_sets_by_exercise(db: Session, exercise_id: int):
    return db.query(models.Set).filter(models.Set.exercise_id == exercise_id).all()


def update_set(db: Session, set_id: int, set_data: schemas.SetCreate):
    db_set = get_set(db, set_id)
    if db_set:
        db_set.reps = set_data.reps
        db_set.weight = set_data.weight
        db.commit()
        db.refresh(db_set)
    return db_set


def delete_set(db: Session, set_id: int):
    db_set = get_set(db, set_id)
    if db_set:
        db.delete(db_set)
        db.commit()
    return db_set
