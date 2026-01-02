from sqlalchemy.orm import Session
from sqlalchemy import and_
from app import models, schemas
from datetime import date


# Workout Template CRUD
def create_workout_template(db: Session, workout_template: schemas.WorkoutTemplateCreate):
    db_workout_template = models.WorkoutTemplate(date=workout_template.date)
    db.add(db_workout_template)
    db.commit()
    db.refresh(db_workout_template)
    return db_workout_template


def get_workout_template(db: Session, workout_template_id: int):
    return db.query(models.WorkoutTemplate).filter(models.WorkoutTemplate.id == workout_template_id).first()


def get_workout_templates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.WorkoutTemplate).offset(skip).limit(limit).all()


def update_workout_template(db: Session, workout_template_id: int, workout_template: schemas.WorkoutTemplateUpdate):
    db_workout_template = get_workout_template(db, workout_template_id)
    if db_workout_template:
        if workout_template.date is not None:
            db_workout_template.date = workout_template.date
        db.commit()
        db.refresh(db_workout_template)
    return db_workout_template


def delete_workout_template(db: Session, workout_template_id: int):
    db_workout_template = get_workout_template(db, workout_template_id)
    if db_workout_template:
        db.delete(db_workout_template)
        db.commit()
    return db_workout_template


# Exercise CRUD
def create_exercise(db: Session, workout_template_id: int, exercise: schemas.ExerciseCreate):
    db_exercise = models.Exercise(
        name=exercise.name,
        workout_template_id=workout_template_id
    )
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def get_exercise(db: Session, exercise_id: int):
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()


def get_exercises_by_workout_template(db: Session, workout_template_id: int):
    return db.query(models.Exercise).filter(models.Exercise.workout_template_id == workout_template_id).all()


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
        reps=set_data.reps,
        weight=set_data.weight,
        exercise_id=exercise_id
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

