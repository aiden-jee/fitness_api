from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    default_measurement(String, nullable=True)
    timezone = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    
class WorkoutTemplate(Base):
    __tablename__ = "workout_templates"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    exercise_templates = relationship("ExerciseTemplate", back_populates="workout_template", cascade="all, delete-orphan")

class ExerciseTemplate(Base):
    __tablename__ = "exercise_templates"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    workout_template_id = Column(Integer, ForeignKey("workout_templates.id"), nullable=False)
    workout_template = relationship("WorkoutTemplate", back_populates="exercise_templates")
    

class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    exercises = relationship("Exercise", back_populates="workout", cascade="all, delete-orphan")

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    workout_id = Column(Integer, ForeignKey("workout.id"), nullable=False)
    workout = relationship("Workout", back_populates="exercises")
    sets = relationship("Set", back_populates="exercise", cascade="all, delete-orphan")


class Set(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    exercise = relationship("Exercise", back_populates="sets")

