import pandas as pd


def preprocess_dataset(
    input_path: str,
    output_path: str
):
    """
    Basic preprocessing.
    """

    df = pd.read_csv(
        input_path
    )

    df = df.dropna()

    df = df.drop_duplicates()

    df.to_csv(
        output_path,
        index=False
    )

    return {
        "rows":
            len(df),
        "output":
            output_path
    }
