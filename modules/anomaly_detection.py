from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.1)

    def train(self, data):
        self.model.fit(data)

    def predict(self, data):
        return self.model.predict(data)

# Example usage
if __name__ == "__main__":
    detector = AnomalyDetector()
    training_data = np.random.rand(100, 2)
    detector.train(training_data)

    test_data = np.random.rand(10, 2)
    predictions = detector.predict(test_data)
    print(predictions)

