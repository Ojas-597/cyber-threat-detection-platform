import joblib
import pandas as pd

from sklearn.ensemble import (
    RandomForestClassifier
)


def train_model(
    dataset_path: str,
    model_path: str
):
    """
    Train threat classifier.
    """

    df = pd.read_csv(
        dataset_path
    )

    X = df.drop(
        "label",
        axis=1
    )

    y = df["label"]

    model = (
        RandomForestClassifier(
            n_estimators=100
        )
    )

    model.fit(
        X,
        y
    )

    joblib.dump(
        model,
        model_path
    )

    return {
        "status":
            "trained",
        "saved_to":
            model_path
    }
