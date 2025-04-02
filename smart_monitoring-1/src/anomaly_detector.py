class AnomalyDetector:
    def __init__(self):
        from sklearn.ensemble import IsolationForest
        import numpy as np
        
        self.model = IsolationForest(contamination=0.1)
        self.data_buffer = []

    def train(self):
        if len(self.data_buffer) > 0:
            self.model.fit(np.array(self.data_buffer).reshape(-1, 1))
            self.data_buffer = []  # Clear buffer after training

    def predict(self, data_point):
        self.data_buffer.append(data_point)
        if len(self.data_buffer) > 100:  # Example threshold for training
            self.train()
        prediction = self.model.predict([[data_point]])
        return "Anomaly" if prediction[0] == -1 else "Normal"