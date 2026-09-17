from pathlib import Path

from src.trainer import MODEL_PATH, load_model, train_model


class SpamPredictor:
    def __init__(self):
        self.model = load_model()

    def model_exists(self) -> bool:
        return Path(MODEL_PATH).exists()

    def train(self) -> None:
        result = train_model()
        self.model = result["model"]

    def predict(self, message: str) -> tuple[str, float]:
        if not isinstance(message, str) or not message.strip():
            raise ValueError("Message cannot be empty.")

        probabilities = self.model.predict_proba([message])[0]
        classes = list(self.model.classes_)
        index = probabilities.argmax()

        predicted_label = classes[index]
        confidence = float(probabilities[index] * 100)

        if predicted_label == "ham":
            display_label = "NOT SPAM"
        else:
            display_label = "SPAM"

        return display_label, confidence
