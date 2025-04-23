# Time Series Predictor

A web-based time series prediction application using TensorFlow/Keras and Flask. This application allows users to input time series data, train an LSTM model, and make future predictions with interactive visualizations.

## Features

- LSTM-based time series prediction
- Interactive web interface
- Real-time data visualization using Plotly
- Easy-to-use data input system
- Configurable prediction horizon
- Model persistence

## Project Structure

```
time-series-predictor/
├── app/
│   └── app.py              # Flask application
├── models/
│   └── time_series_model.py # LSTM model implementation
├── static/
│   └── style.css          # CSS styles
├── templates/
│   └── index.html         # Web interface template
├── data/                  # Directory for data storage
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd time-series-predictor
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app/app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Using the application:
   - Enter your time series data as comma-separated numbers
   - Click "Train Model" to train the LSTM model
   - Specify the number of steps to predict
   - Click "Make Prediction" to see the forecast

## Model Details

The application uses a stacked LSTM (Long Short-Term Memory) neural network with:
- Two LSTM layers with 50 units each
- Dropout layers for regularization
- Dense output layer for predictions
- Adam optimizer and MSE loss function

## Input Data Format

- Data should be numeric and comma-separated
- Minimum 11 data points required for training
- Example: 1.5, 2.3, 3.1, 2.8, 4.2, 3.9, 5.1, 4.8, 6.2, 5.9, 7.1

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 