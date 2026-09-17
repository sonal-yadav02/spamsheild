from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "spam.csv"


def load_dataset() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    required = {"label", "message"}
    if not required.issubset(df.columns):
        raise ValueError("Dataset must contain 'label' and 'message' columns.")

    df = df[["label", "message"]].dropna()
    df["label"] = df["label"].astype(str).str.lower().str.strip()
    df["message"] = df["message"].astype(str).str.strip()

    df = df[df["message"] != ""]
    df = df[df["label"].isin(["spam", "ham"])]

    if len(df) < 10:
        raise ValueError("Dataset is too small for training.")

    return df
