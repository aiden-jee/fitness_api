from pydantic import BaseModel
from datetime import date
from typing import List, Optional


# ============================================================================
# Set Schemas (Sets in Exercises - Has Reps and Weight)
# ============================================================================
class SetBase(BaseModel):
    reps: int
    weight: float

class SetCreate(SetBase):
    pass


class SetResponse(SetBase):
    id: int
    exercise_id: int

    class Config:
        from_attributes = True

class SetUpdate(BaseModel):
    reps: Optional[int] = None
    weight: Optional[float] = None

# ============================================================================
# Exercise Schemas (Exercises in Workouts - Has Sets)
# ============================================================================
class ExerciseBase(BaseModel):
    name: str


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):
    id: int
    workout_id: int
    sets: List[SetResponse] = []

    class Config:
        from_attributes = True

class ExerciseUpdate(BaseModel):
    name: Optional[str] = None

# ============================================================================
# Workout Schemas (Workouts - Has Exercises)
# ============================================================================

class WorkoutBase(BaseModel):
    name: str
    date: date
    
class WorkoutCreate(WorkoutBase):
    pass

class WorkoutResponse(WorkoutBase):
    id: int
    exercises: List[ExerciseResponse] = []
    
    class Config:
        from_attributes = True

class WorkoutUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[date] = None
    

# ============================================================================
# Exercise Template Schemas (Exercise Templates in Workout Templates)
# ============================================================================
class ExerciseTemplateBase(BaseModel):
    name: str

class ExerciseTemplateCreate(ExerciseTemplateBase):
    pass

class ExerciseTemplateResponse(ExerciseTemplateBase):
    id: int
    workout_template_id: int

    class Config:
        from_attributes = True

class ExerciseTemplateUpdate(BaseModel):
    name: Optional[str] = None
    
    
# ============================================================================
# Workout Template Schemas (Workout Templates - Has Exercise Templates)
# ============================================================================
class WorkoutTemplateBase(BaseModel):
    name: str


class WorkoutTemplateCreate(WorkoutTemplateBase):
    pass


class WorkoutTemplateResponse(WorkoutTemplateBase):
    id: int
    exercise_templates: List[ExerciseTemplateResponse] = []

    class Config:
        from_attributes = True


class WorkoutTemplateUpdate(BaseModel):
    date: Optional[date] = None