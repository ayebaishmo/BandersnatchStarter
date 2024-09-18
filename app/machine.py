import joblib
import os
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from datetime import datetime


class Machine:

    def __init__(self, df: DataFrame):
        """
        Initialize the machine learning model using the provided DataFrame.
        The model will be trained with the features and target data.
        """

        self.name = "LogisticRegression"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.target = df['Rarity']
        self.features = df.drop(columns=["Rarity"])

        self.model = LogisticRegression()
        self.model.fit(self.features, self.target)

    def __call__(self, feature_basis):
        """
        Make a prediction based on the input features.
        Returns the predicted class and the confidence
        (probability) of the prediction.
        """

        prediction = self.model.predict(feature_basis)[0]
        confidence = self.model.predict_proba(feature_basis).max()
        return prediction, confidence

    def save(self, filepath):
        """
        Save the model to a file using joblib for serialization.
        """
        with open(filepath, 'wb') as f:
            joblib.dump(self, f)

    @staticmethod
    def open(filepath: str):
        """
        Load a saved model from the specified filepath.
        """
        with open(filepath, 'rb') as f:
            return joblib.load(f)

    def info(self):
        """
        Return a string with the name of the model
        and the timestamp of initialization.
        """
        return f"Base Model: {self.name} <br> Timestamp: {self.timestamp}"
