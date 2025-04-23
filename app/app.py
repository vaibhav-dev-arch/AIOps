import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
import json
from models.time_series_model import TimeSeriesPredictor

app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

# Initialize the model
model = TimeSeriesPredictor(sequence_length=10)

def create_plot(historical_data, predictions, title="Time Series Prediction"):
    """Create a plotly figure"""
    fig = go.Figure()
    
    # Add historical data
    fig.add_trace(go.Scatter(
        y=historical_data,
        mode='lines',
        name='Historical Data',
        line=dict(color='blue')
    ))
    
    # Add predictions
    if predictions is not None:
        fig.add_trace(go.Scatter(
            y=predictions,
            mode='lines',
            name='Predictions',
            line=dict(color='red', dash='dash')
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Time",
        yaxis_title="Value",
        hovermode='x'
    )
    
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    try:
        # Get data from request
        data = request.json['data']
        data = np.array(data, dtype=np.float32)
        
        # Train the model
        history = model.train(data)
        
        # Save the model
        model.save_model('models/trained_model.h5')
        
        return jsonify({
            'status': 'success',
            'message': 'Model trained successfully',
            'history': {
                'loss': [float(x) for x in history.history['loss']],
                'val_loss': [float(x) for x in history.history['val_loss']]
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.json['data']
        n_steps = request.json.get('n_steps', 10)
        
        data = np.array(data, dtype=np.float32)
        
        # Load model if exists
        if os.path.exists('models/trained_model.h5'):
            model.load_model('models/trained_model.h5')
        
        # Make predictions
        predictions = model.predict_sequence(data, n_steps)
        
        # Create plot
        plot_json = create_plot(data, predictions)
        
        return jsonify({
            'status': 'success',
            'predictions': predictions.tolist(),
            'plot': plot_json
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 