```python
import os

from src.predictor import SpamPredictor
from src.report_generator import save_report


def test_model_loads():
    predictor = SpamPredictor()

    assert predictor.model is not None


def test_prediction_returns_valid_label():
    predictor = SpamPredictor()

    label, confidence = predictor.predict(
        "Congratulations! You have won a free prize."
    )

    assert label in ["SPAM", "NOT SPAM"]
    assert 0 <= confidence <= 100


def test_empty_message_rejected():
    predictor = SpamPredictor()

    try:
        predictor.predict("")
        assert False
    except ValueError:
        assert True


def test_report_generation():
    path = save_report(
        "Congratulations! You won a prize.",
        "SPAM",
        95.5
    )

    assert os.path.exists(path)
```
