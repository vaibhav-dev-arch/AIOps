import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
import json
from models.performance_predictor import PerformancePredictor

app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

# Initialize the model
performance_model = PerformancePredictor()

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/performance/train', methods=['POST'])
def train_performance():
    try:
        # Get data from request
        data = request.json['data']
        labels = request.json['labels']
        epochs = request.json.get('epochs', 50)
        
        # Convert data to numpy array
        X = np.array(data)
        y = np.array(labels)
        
        # Train the model
        history = performance_model.train(X, y, epochs=epochs)
        
        # Save the model
        performance_model.save_model('models/performance_model.h5')
        
        return jsonify({
            'status': 'success',
            'message': 'Performance model trained successfully',
            'history': {
                'loss': [float(x) for x in history.history['loss']],
                'val_loss': [float(x) for x in history.history['val_loss']],
                'accuracy': [float(x) for x in history.history['accuracy']],
                'val_accuracy': [float(x) for x in history.history['val_accuracy']]
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/performance/predict', methods=['POST'])
def predict_performance():
    try:
        # Get data from request
        data = request.json['data']
        
        # Load model if exists
        if os.path.exists('models/performance_model.h5'):
            performance_model.load_model('models/performance_model.h5')
        else:
            return jsonify({
                'status': 'error',
                'message': 'Model not trained yet. Please train the model first.'
            }), 400
        
        # Make prediction
        prediction = performance_model.predict(data)
        
        if prediction['prediction'] == 'Model not trained':
            return jsonify({
                'status': 'error',
                'message': 'Model not trained yet. Please train the model first.'
            }), 400
        
        return jsonify({
            'status': 'success',
            'prediction': prediction['prediction'],
            'confidence': prediction['confidence'],
            'classes': prediction['classes']
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 