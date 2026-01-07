import pytest

from app.schemas import (
    WorkoutUpdate,
    SetUpdate,
    ExerciseUpdate,
    # UserUpdate,
    WorkoutTemplateUpdate,
    ExerciseTemplateUpdate,
)

# -------------------------------------------------------------------
# CONSTANTS (Change as needed)
# -------------------------------------------------------------------
UPDATE_MODEL = [
    WorkoutUpdate,
    SetUpdate,
    ExerciseUpdate,
    # UserUpdate,
    WorkoutTemplateUpdate,
    ExerciseTemplateUpdate,
]

VALID_UPDATE_MODEL_TO_FIELD = {
    WorkoutUpdate: {"name": "Test Run"},
    SetUpdate: {"weight": 100.5},
    ExerciseUpdate: {"name": "Bench Press"},
    # UserUpdate: {"name": "New Name"},
    WorkoutTemplateUpdate: {"name": "New template"},
    ExerciseTemplateUpdate: {"name": "New template"},
}


# -------------------------------------------------------------------
# Unit tests
# -------------------------------------------------------------------
@pytest.mark.parametrize("model", UPDATE_MODEL)
def test_update_error_no_field(model):
    empty_field = {}
    with pytest.raises(ValueError) as excinfo:
        model(**empty_field)
    assert "At least one field must be updated" in str(excinfo.value), "Incorrect error / no error message"


@pytest.mark.parametrize(
    "model, field", [(k, v) for k, v in VALID_UPDATE_MODEL_TO_FIELD.items()]
)
def test_update_pass_one_field(model, field):
    try:
        instance = model(**field)
    except Exception as e:
        pytest.fail(f"Test failed for {model}: {e}")

    assert instance is not None, "Class not created"
    assert len(instance.model_dump(exclude_none=True)) == 1, "Model's field != 1"
