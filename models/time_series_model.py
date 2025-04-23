import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler

class TimeSeriesPredictor:
    def __init__(self, sequence_length=10):
        self.sequence_length = sequence_length
        self.model = None
        self.scaler = MinMaxScaler()
        
    def create_sequences(self, data):
        """Create sequences for LSTM model"""
        X, y = [], []
        for i in range(len(data) - self.sequence_length):
            X.append(data[i:(i + self.sequence_length)])
            y.append(data[i + self.sequence_length])
        return np.array(X), np.array(y)
    
    def build_model(self, input_shape):
        """Build LSTM model"""
        self.model = Sequential([
            LSTM(50, activation='relu', input_shape=input_shape, return_sequences=True),
            Dropout(0.2),
            LSTM(50, activation='relu'),
            Dropout(0.2),
            Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')
        return self.model
    
    def prepare_data(self, data):
        """Scale and prepare data"""
        scaled_data = self.scaler.fit_transform(data.reshape(-1, 1))
        X, y = self.create_sequences(scaled_data)
        return X, y
    
    def train(self, data, epochs=50, batch_size=32, validation_split=0.2):
        """Train the model"""
        X, y = self.prepare_data(data)
        if self.model is None:
            self.build_model((X.shape[1], 1))
        
        history = self.model.fit(
            X, y,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            verbose=1
        )
        return history
    
    def predict(self, data):
        """Make predictions"""
        # Scale the input data
        scaled_data = self.scaler.transform(data.reshape(-1, 1))
        # Create sequences
        X = np.array([scaled_data[-self.sequence_length:]])
        # Make prediction
        scaled_prediction = self.model.predict(X)
        # Inverse transform the prediction
        prediction = self.scaler.inverse_transform(scaled_prediction)
        return prediction[0][0]
    
    def predict_sequence(self, initial_sequence, n_steps):
        """Predict sequence of n_steps into the future"""
        current_sequence = initial_sequence[-self.sequence_length:].copy()
        predictions = []
        
        for _ in range(n_steps):
            next_pred = self.predict(current_sequence)
            predictions.append(next_pred)
            current_sequence = np.append(current_sequence[1:], next_pred)
        
        return np.array(predictions)
    
    def save_model(self, filepath):
        """Save the model"""
        self.model.save(filepath)
    
    def load_model(self, filepath):
        """Load the model"""
        self.model = tf.keras.models.load_model(filepath) 