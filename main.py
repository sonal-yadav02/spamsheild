```python
from src.predictor import SpamPredictor
from src.analyzer import evaluate_model
from src.report_generator import save_report


def main():
    print("=" * 50)
    print("        SPAMSHIELD - AI SPAM DETECTOR")
    print("=" * 50)

    # Load the AI model
    try:
        predictor = SpamPredictor()
    except Exception as error:
        print(f"\nError loading model: {error}")
        print("Please check the dataset and installed dependencies.")
        return

    while True:
        print("\n" + "-" * 50)
        print("MAIN MENU")
        print("-" * 50)
        print("1. Predict a Message")
        print("2. Evaluate the Model")
        print("3. Generate Prediction Report")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        # -------------------------------------------------
        # OPTION 1: Predict Message
        # -------------------------------------------------
        if choice == "1":
            message = input("\nEnter the message to analyze:\n> ").strip()

            if not message:
                print("\nError: Message cannot be empty.")
                continue

            try:
                label, confidence = predictor.predict(message)

                print("\n" + "=" * 40)
                print("PREDICTION RESULT")
                print("=" * 40)
                print(f"Message    : {message}")
                print(f"Prediction : {label}")
                print(f"Confidence : {confidence:.2f}%")
                print("=" * 40)

            except Exception as error:
                print(f"\nPrediction error: {error}")

        # -------------------------------------------------
        # OPTION 2: Evaluate Model
        # -------------------------------------------------
        elif choice == "2":
            print("\nEvaluating the AI model...")
            
            try:
                metrics = evaluate_model()

                print("\n" + "=" * 40)
                print("MODEL EVALUATION")
                print("=" * 40)
                print(f"Accuracy  : {metrics['accuracy']:.2f}%")
                print(f"Precision : {metrics['precision']:.2f}%")
                print(f"Recall    : {metrics['recall']:.2f}%")
                print(f"F1-Score  : {metrics['f1']:.2f}%")
                print("=" * 40)

            except Exception as error:
                print(f"\nEvaluation error: {error}")

        # -------------------------------------------------
        # OPTION 3: Generate Report
        # -------------------------------------------------
        elif choice == "3":
            message = input("\nEnter the message for the report:\n> ").strip()

            if not message:
                print("\nError: Message cannot be empty.")
                continue

            try:
                label, confidence = predictor.predict(message)

                report_path = save_report(
                    message,
                    label,
                    confidence
                )

                print("\n" + "=" * 40)
                print("REPORT GENERATED")
                print("=" * 40)
                print(f"Prediction : {label}")
                print(f"Confidence : {confidence:.2f}%")
                print(f"Report     : {report_path}")
                print("=" * 40)

            except Exception as error:
                print(f"\nReport generation error: {error}")

        # -------------------------------------------------
        # OPTION 4: Exit
        # -------------------------------------------------
        elif choice == "4":
            print("\nThank you for using SpamShield!")
            print("Goodbye.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
```
