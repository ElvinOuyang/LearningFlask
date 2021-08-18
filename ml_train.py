import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import pickle

def train_iris_nb():
    """Train a GaussianNB model on iris dataset."""
    X, y_train = load_iris(return_X_y=True, as_frame=True)
    colnames = X.columns
    X_train = X.values
    model = GaussianNB()
    model.fit(X_train, y_train)
    return model

def dump_model(model_path, model):
    """Save model as binary pickle file."""
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

def load_model(model_path):
    """Load model to return for future use."""
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    model = train_iris_nb()
    dump_model('model.pickle', model)

if __name__ == '__main__':
    main()