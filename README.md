# Performance Predictor

A web-based performance prediction application using TensorFlow/Keras and Flask. This application allows users to input system metrics, train a neural network model, and predict root causes of performance issues with interactive visualizations.

## Features

- Neural network-based performance prediction
- Interactive web interface
- Real-time data visualization using Plotly
- Easy-to-use system metrics input
- Configurable training parameters
- Model persistence

## Project Structure

```
performance-predictor/
├── app/
│   └── app.py              # Flask application
├── models/
│   └── performance_predictor.py # Neural network model implementation
├── static/
│   └── style.css          # CSS styles
├── templates/
│   └── main.html         # Web interface template
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
   cd performance-predictor
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
   http://localhost:8080
   ```

3. Using the application:
   - Enter system metrics (CPU, Memory, Delay, Error codes)
   - Click "Train Model" to train the neural network
   - Use the prediction interface to identify root causes
   - View confidence scores and historical predictions

## Model Details

The application uses a neural network with:
- Multiple dense layers
- Dropout layers for regularization
- Softmax output layer for classification
- Adam optimizer and categorical crossentropy loss function

## Input Data Format

- System metrics should be provided in CSV format
- Required metrics: CPU_LOAD, MEMORY_LOAD, DELAY, ERROR codes
- Example: CPU_LOAD,MEMORY_LOAD,DELAY,ERROR_1000,ERROR_1001,ERROR_1002,ERROR_1003,ROOT_CAUSE

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 