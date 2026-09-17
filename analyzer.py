from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.data_loader import load_dataset
from src.trainer import build_pipeline


def evaluate_model() -> dict:
    df = load_dataset()

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        df["message"],
        df["label"],
        test_size=0.25,
        random_state=42,
        stratify=df["label"],
    )

    model = build_pipeline()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return {
        "accuracy": accuracy_score(y_test, predictions) * 100,
        "precision": precision_score(
            y_test, predictions, pos_label="spam", zero_division=0
        )
        * 100,
        "recall": recall_score(
            y_test, predictions, pos_label="spam", zero_division=0
        )
        * 100,
        "f1": f1_score(
            y_test, predictions, pos_label="spam", zero_division=0
        )
        * 100,
    }
