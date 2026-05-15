import pandas as pd


def preprocess(file):

    data = pd.read_csv(file)

    return data.dropna()
