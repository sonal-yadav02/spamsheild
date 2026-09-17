from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"


def save_report(message: str, label: str, confidence: float) -> str:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""SPAMSHIELD - PREDICTION REPORT
========================================

Generated: {timestamp}

Message:
{message}

Prediction: {label}
Confidence: {confidence:.2f}%

========================================
"""

    path = OUTPUT_DIR / "prediction_report.txt"
    path.write_text(report, encoding="utf-8")
    return str(path)
