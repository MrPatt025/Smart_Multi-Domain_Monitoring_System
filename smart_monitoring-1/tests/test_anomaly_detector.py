import unittest
from src.anomaly_detector import AnomalyDetector

class TestAnomalyDetector(unittest.TestCase):

    def setUp(self):
        self.detector = AnomalyDetector()

    def test_train_model(self):
        # Sample data for training
        data = [[1, 2], [2, 3], [3, 4], [10, 10]]
        self.detector.train(data)
        self.assertIsNotNone(self.detector.model)

    def test_predict_normal(self):
        # Sample data for prediction
        self.detector.train([[1, 2], [2, 3], [3, 4], [10, 10]])
        result = self.detector.predict([2, 3])
        self.assertEqual(result, "Normal")

    def test_predict_anomaly(self):
        self.detector.train([[1, 2], [2, 3], [3, 4], [10, 10]])
        result = self.detector.predict([10, 11])
        self.assertEqual(result, "Anomaly")

if __name__ == '__main__':
    unittest.main()