import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import LabelEncoder

class PerformancePredictor:
    def __init__(self):
        self.model = None
        self.label_encoder = LabelEncoder()
        self.classes = None
        
    def build_model(self, input_shape, num_classes):
        """Build the neural network model"""
        self.model = Sequential([
            Dense(64, activation='relu', input_shape=input_shape),
            Dropout(0.2),
            Dense(32, activation='relu'),
            Dropout(0.2),
            Dense(num_classes, activation='softmax')
        ])
        self.model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        return self.model
    
    def prepare_data(self, data):
        """Prepare the input data"""
        # Assuming data is a dictionary with the following keys:
        # CPU_LOAD, MEMORY_LOAD, DELAY, ERROR_1000, ERROR_1001, ERROR_1002, ERROR_1003
        features = np.array([
            data['CPU_LOAD'],
            data['MEMORY_LOAD'],
            data['DELAY'],
            data['ERROR_1000'],
            data['ERROR_1001'],
            data['ERROR_1002'],
            data['ERROR_1003'],
            0  # Add a default value for the 8th feature
        ]).reshape(1, -1)
        return features
    
    def train(self, X, y, epochs=50, batch_size=32, validation_split=0.2):
        """Train the model"""
        # Encode the target labels
        y_encoded = self.label_encoder.fit_transform(y)
        self.classes = self.label_encoder.classes_
        
        if self.model is None:
            self.build_model((X.shape[1],), len(self.classes))
        
        history = self.model.fit(
            X, y_encoded,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            verbose=1
        )
        return history
    
    def predict(self, data):
        """Make a prediction with confidence scores"""
        if self.model is None or self.classes is None:
            return {
                'prediction': 'Model not trained',
                'confidence': [1.0],
                'classes': ['Please train the model first']
            }
            
        features = self.prepare_data(data)
        prediction = self.model.predict(features)
        predicted_class = self.label_encoder.inverse_transform([np.argmax(prediction)])
        confidence = prediction[0].tolist()
        
        return {
            'prediction': predicted_class[0],
            'confidence': confidence,
            'classes': self.classes.tolist()
        }
    
    def save_model(self, filepath):
        """Save the model"""
        self.model.save(filepath)
    
    def load_model(self, filepath):
        """Load the model"""
        self.model = tf.keras.models.load_model(filepath) 