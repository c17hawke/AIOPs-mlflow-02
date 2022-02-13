import os
import mlflow
import mlflow.sklearn
import argparse
import time
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import numpy as np
import pandas as pd

def evaluate(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def get_data():
    URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    try:
        df = pd.read_csv(URL, sep=";")
        return df
    except Exception as e:
        raise e

def main(alpha, l1_ratio):
    df = get_data()

    train, test = train_test_split(df)

    TARGET = "quality"

    train_x = train.drop([TARGET], axis=1)
    test_x = test.drop([TARGET], axis=1)

    train_y = train[[TARGET]]
    test_y = test[[TARGET]]

    # mlflow implementation-
    mlflow.sklearn.autolog()
    model_lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    model_lr.fit(train_x, train_y)
    pred = model_lr.predict(test_x)
    rmse, mae, r2 = evaluate(test_y, pred)
    print(f"params- alpha: {alpha}, l1_ratio: {l1_ratio}")
    print(f"eval metrics - rmse: {rmse}, mae: {mae}, r2: {r2}")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--alpha", "-a", type=float, default=0.5)
    args.add_argument("--l1_ratio", "-l1", type=float, default=0.5)
    parsed_args = args.parse_args()

    main(alpha=parsed_args.alpha, l1_ratio=parsed_args.l1_ratio)