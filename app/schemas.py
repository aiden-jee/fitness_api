from pydantic import Field, BaseModel, model_validator
from datetime import datetime
from typing import List, Optional, Literal

# ============================================================================
# Constants
# ============================================================================

USERNAME_MAX = 24


# TODO: Export to a seperate models folder when refactoring
def validate_any_field(self):
    """Reusable logic for Pydantic model_validators"""
    if not self.model_dump(exclude_none=True):
        raise ValueError("At least one field must be updated")
    return self


# ============================================================================
# User Schemas
# ============================================================================
class UserBase(BaseModel):
    name: str = Field(
        description="Name of the user", alias="username", max_length=USERNAME_MAX
    )
    default_measurement: Optional[Literal["lbs", "kgs"]] = Field(
        "lbs", description="The default measurement unit for the user"
    )
    timezone: Optional[str] = Field(
        None, description="IANA timezone name, e.g America/Los_Angeles"
    )


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int = Field(gt=0, description="The ID of the user being returned")
    created_at: datetime = Field(
        description="Date and time in UTC the user was created"
    )

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The name of the user to update")
    default_measurement: Optional[Literal["lbs", "kg"]] = Field(
        None, description="The default measurement unit of the user to update to"
    )
    timezone: Optional[str] = Field(
        None, description="The timezone of the user to update"
    )

    @model_validator(mode="after")
    def validate_at_least_one_field(self):
        if (
            self.name is None
            and self.default_measurement is None
            and self.timezone is None
        ):
            raise ValueError("At least one value must be updated")
        return self


# ============================================================================
# Set Schemas (Sets in Exercises - Has Reps and Weight)
# ============================================================================
class SetBase(BaseModel):
    reps: int = Field(gt=0, description="The number of reps in the set")
    weight: float = Field(ge=0, description="The weight of each rep")


class SetCreate(SetBase):
    pass


class SetResponse(SetBase):
    id: int = Field(description="The ID of the set being returned")
    exercise_id: int = Field(description="The ID of the exercise the set belongs to")

    class Config:
        from_attributes = True


class SetUpdate(BaseModel):
    reps: Optional[int] = Field(
        None, gt=0, description="The number of reps in the set to update"
    )
    weight: Optional[float] = Field(
        None, ge=0, description="The weight of each rep to update"
    )

    _validate = model_validator(mode="after")(validate_any_field)


# ============================================================================
# Exercise Schemas (Exercises in Workouts - Has Sets)
# ============================================================================
class ExerciseBase(BaseModel):
    name: str = Field(description="The name of the exercise")


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):
    id: int = Field(description="The ID of the exercise being returned")
    workout_id: int = Field(description="The ID of the workout the exercise belongs to")
    sets: List[SetResponse] = Field(
        default_factory=list, description="List of sets performed for this exercise"
    )

    class Config:
        from_attributes = True


class ExerciseUpdate(BaseModel):
    name: str = Field(description="The name of the exercise to update")


# ============================================================================
# Workout Schemas (Workouts - Has Exercises)
# ============================================================================


class WorkoutBase(BaseModel):
    name: str = Field(description="Name of the workout")
    date: Optional[datetime] = Field(
        datetime.now(), decription="Date and time of the workout"
    )


class WorkoutCreate(WorkoutBase):
    pass


class WorkoutResponse(WorkoutBase):
    id: int
    exercises: List[ExerciseResponse] = []

    class Config:
        from_attributes = True


class WorkoutUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Name of the workout to update")
    date: Optional[datetime] = Field(
        None, description="Date and time of the workout to update"
    )

    _validate = model_validator(mode="after")(validate_any_field)


# ============================================================================
# Exercise Template Schemas (Exercise Templates in Workout Templates)
# ============================================================================
class ExerciseTemplateBase(BaseModel):
    name: str = Field(description="Name of the exercise template")


class ExerciseTemplateCreate(ExerciseTemplateBase):
    pass


class ExerciseTemplateResponse(ExerciseTemplateBase):
    id: int = Field(description="ID of the exercise template being returned")
    workout_template_id: int = Field(
        description="ID of the workout template that the exercise template belongs to"
    )

    class Config:
        from_attributes = True


class ExerciseTemplateUpdate(BaseModel):
    name: str = Field(description="Name of the exercise template to update")


# ============================================================================
# Workout Template Schemas (Workout Templates - Has Exercise Templates)
# ============================================================================
class WorkoutTemplateBase(BaseModel):
    name: str = Field(description="Name of the workout template")


class WorkoutTemplateCreate(WorkoutTemplateBase):
    pass


class WorkoutTemplateResponse(WorkoutTemplateBase):
    id: int = Field(description="ID of the workout template being returned")
    exercise_templates: List[ExerciseTemplateResponse] = Field(
        default_factory=list,
        description="List of exercise templates used in this workout template",
    )

    class Config:
        from_attributes = True


class WorkoutTemplateUpdate(BaseModel):
    name: str = Field(description="Name of the workout template to update")
