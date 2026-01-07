import pytest

from datetime import datetime
from pydantic import ValidationError
from app.schemas import (
    WorkoutCreate,
    WorkoutUpdate,
    SetCreate,
    SetUpdate,
    ExerciseCreate,
    ExerciseUpdate,
    # UserUpdate,
    WorkoutTemplateCreate,
    WorkoutTemplateUpdate,
    ExerciseTemplateCreate,
    ExerciseTemplateUpdate,
)

# -------------------------------------------------------------------
# CONSTANTS (Change as needed)
# -------------------------------------------------------------------
# Models that obey standard creation rules
CREATE_MODELS = [
    (SetCreate, {"reps": 10, "weight": 100.0}),
    (ExerciseCreate, {"name": "Bench Press"}),
    (WorkoutCreate, {"name": "Chest Day", "date": datetime.now()}),
    (ExerciseTemplateCreate, {"name": "Squat Template"}),
    (WorkoutTemplateCreate, {"name": "Leg Day Template"}),
]

# Models that use your custom `validate_any_field` (All fields optional)
OPTIONAL_UPDATE_MODELS = [
    (SetUpdate, {"reps": 12}, {"reps": 0}),  # (Model, Valid Data, Invalid Data)
    (WorkoutUpdate, {"name": "New Name"}, None),
]

# Models that have REQUIRED fields in their update schema
STRICT_UPDATE_MODELS = [
    (ExerciseUpdate, {"name": "New Name"}),
    (ExerciseTemplateUpdate, {"name": "New Template Name"}),
    (WorkoutTemplateUpdate, {"name": "New Workout Name"}),
]


# -------------------------------------------------------------------
# Unit tests
# -------------------------------------------------------------------
@pytest.mark.parametrize("model, valid_data", CREATE_MODELS)
def test_create_model_valid(model, valid_data):
    """Test that models can be created with valid data."""
    instance = model(**valid_data)
    assert instance is not None


@pytest.mark.parametrize("model, valid_data, _", OPTIONAL_UPDATE_MODELS)
def test_optional_update_valid(model, valid_data, _):
    """Test that the 'flexible' update models work with partial data."""
    instance = model(**valid_data)
    assert instance is not None


@pytest.mark.parametrize("model, valid_data", STRICT_UPDATE_MODELS)
def test_strict_update_valid(model, valid_data):
    """Test that 'strict' update models work when required fields are present."""
    instance = model(**valid_data)
    assert instance.name == valid_data["name"]


@pytest.mark.parametrize("model, _, __", OPTIONAL_UPDATE_MODELS)
def test_update_error_if_empty_body(model, _, __):
    """
    Verifies that models using `validate_any_field` raise a ValueError
    when initialized with an empty dict.
    """
    with pytest.raises(ValueError) as exc:
        model(**{})

    # Matches your specific error message
    assert "At least one field must be updated" in str(exc.value)


@pytest.mark.parametrize("model, _", STRICT_UPDATE_MODELS)
def test_strict_update_error_missing_field(model, _):
    """
    Verifies that 'Strict' models raise a standard Pydantic 'Field required'
    error instead of the custom validator error when empty.
    """
    with pytest.raises(ValidationError) as exc:
        model(**{})

    assert "Field required" in str(exc.value)
