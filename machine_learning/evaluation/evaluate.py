import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score
)


def evaluate_model(
    model_path: str,
    test_path: str
):
    """
    Evaluate ML model.
    """

    model = joblib.load(
        model_path
    )

    df = pd.read_csv(
        test_path
    )

    X = df.drop(
        "label",
        axis=1
    )

    y = df["label"]

    predictions = (
        model.predict(X)
    )

    accuracy = (
        accuracy_score(
            y,
            predictions
        )
    )

    return {
        "accuracy":
            round(
                accuracy,
                4
            )
    }
