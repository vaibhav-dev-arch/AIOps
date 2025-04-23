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
├── Dockerfile            # Docker configuration for containerization
├── setup.py              # Package installation configuration
└── README.md             # This file
```

## Package Components

### Dockerfile
The Dockerfile provides containerization for the application. It:
- Uses Python 3.9 slim image as base
- Sets up the working directory
- Installs dependencies from requirements.txt
- Copies application files
- Exposes port 8080
- Uses Gunicorn as the production server

### setup.py
The setup.py file enables local installation of the package. It:
- Defines package metadata (name, version, author)
- Specifies Python dependencies with exact versions
- Includes package classifiers and requirements
- Supports both development and production installations

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

## Deployment Instructions

### Quick Start Guide

#### Starting the Application
1. Build the Docker image (first time only):
   ```bash
   docker build -t performance-predictor .
   ```

2. Start the application:
   ```bash
   docker run -d -p 8080:8080 --name performance-predictor-app performance-predictor
   ```

3. Access the application at http://localhost:8080

#### Stopping the Application
1. Stop the container:
   ```bash
   docker stop performance-predictor-app
   ```

2. To start it again:
   ```bash
   docker start performance-predictor-app
   ```

3. To remove the container completely:
   ```bash
   docker rm performance-predictor-app
   ```

### Common Use Cases

#### 1. Development Environment
```bash
# Start the application in development mode
docker run -d -p 8080:8080 --name performance-predictor-app -e FLASK_ENV=development performance-predictor

# View real-time logs
docker logs -f performance-predictor-app
```

#### 2. Production Environment
```bash
# Start with custom port
docker run -d -p 9000:8080 --name performance-predictor-app performance-predictor

# Start with custom model path
docker run -d -p 8080:8080 -v /path/to/models:/app/models --name performance-predictor-app performance-predictor
```

#### 3. Backup and Restore
```bash
# Backup the model
docker cp performance-predictor-app:/app/models/performance_model.h5 ./backup/

# Restore the model
docker cp ./backup/performance_model.h5 performance-predictor-app:/app/models/
```

#### 4. Training with Custom Data
```bash
# Mount custom data directory
docker run -d -p 8080:8080 -v /path/to/custom/data:/app/data --name performance-predictor-app performance-predictor

# Train with specific parameters
curl -X POST http://localhost:8080/performance/train \
  -H "Content-Type: application/json" \
  -d '{"data": [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]], "labels": [0, 1], "epochs": 100}'
```

#### 5. Batch Prediction
```bash
# Prepare input data
cat > input.json << EOF
{
  "data": [
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]
  ]
}
EOF

# Run batch prediction
curl -X POST http://localhost:8080/performance/predict \
  -H "Content-Type: application/json" \
  -d @input.json
```

#### 6. Monitoring and Logging
```bash
# Enable detailed logging
docker run -d -p 8080:8080 \
  -v /var/log/performance-predictor:/app/logs \
  --name performance-predictor-app \
  performance-predictor

# Monitor resource usage
docker stats performance-predictor-app
```

#### 7. Multi-Instance Deployment
```bash
# Run multiple instances with different ports
docker run -d -p 8081:8080 --name performance-predictor-app-1 performance-predictor
docker run -d -p 8082:8080 --name performance-predictor-app-2 performance-predictor

# Load balance between instances using Nginx
```

#### 8. Model Versioning
```bash
# Save model with version
docker exec performance-predictor-app cp /app/models/performance_model.h5 /app/models/performance_model_v1.h5

# Switch between model versions
docker exec performance-predictor-app cp /app/models/performance_model_v1.h5 /app/models/performance_model.h5
```

#### 9. Performance Tuning
```bash
# Run with increased memory
docker run -d -p 8080:8080 --memory=8g --name performance-predictor-app performance-predictor

# Run with multiple CPUs
docker run -d -p 8080:8080 --cpus=4 --name performance-predictor-app performance-predictor
```

#### 10. Security Hardening
```bash
# Run with read-only filesystem
docker run -d -p 8080:8080 \
  --read-only \
  -v /app/models:/app/models:ro \
  --name performance-predictor-app \
  performance-predictor

# Run with non-root user
docker run -d -p 8080:8080 \
  --user 1000:1000 \
  --name performance-predictor-app \
  performance-predictor
```

### Troubleshooting Guide

#### 1. Application Won't Start
- **Error**: Port 8080 already in use
  ```bash
  # Check if port is in use
  lsof -i :8080
  # Kill the process using the port
  kill -9 <PID>
  # Or use a different port
  docker run -d -p 8081:8080 --name performance-predictor-app performance-predictor
  ```

- **Error**: Container exits immediately
  ```bash
  # Check container logs
  docker logs performance-predictor-app
  # Check container status
  docker ps -a
  # Restart with more memory
  docker run -d -p 8080:8080 --memory=4g --name performance-predictor-app performance-predictor
  ```

#### 2. Model Training Issues
- **Error**: CUDA/GPU not available
  ```
  This is normal if you don't have a GPU. The application will use CPU instead.
  ```

- **Error**: Memory issues during training
  ```bash
  # Increase container memory
  docker run -d -p 8080:8080 --memory=8g --name performance-predictor-app performance-predictor
  ```

#### 3. Performance Issues
- **Issue**: Slow response times
  ```bash
  # Check container resource usage
  docker stats performance-predictor-app
  # Increase CPU allocation
  docker run -d -p 8080:8080 --cpus=2 --name performance-predictor-app performance-predictor
  ```

- **Issue**: High memory usage
  ```bash
  # Monitor memory usage
  docker stats performance-predictor-app
  # Restart container to clear memory
  docker restart performance-predictor-app
  ```

#### 4. Data Persistence
- **Issue**: Model not saving
  ```bash
  # Check if volume is mounted correctly
  docker inspect performance-predictor-app
  # Mount volume explicitly
  docker run -d -p 8080:8080 -v $(pwd)/models:/app/models --name performance-predictor-app performance-predictor
  ```

#### 5. Network Issues
- **Issue**: Can't access application
  ```bash
  # Check if container is running
  docker ps
  # Check container logs
  docker logs performance-predictor-app
  # Verify network settings
  docker network inspect bridge
  ```

### Option 1: Using Docker (Recommended)

1. Install Docker on your system
2. Build the Docker image:
   ```bash
   docker build -t performance-predictor .
   ```
3. Run the container:
   ```bash
   docker run -p 8080:8080 performance-predictor
   ```
4. Access the application at http://localhost:8080

#### Docker Commands Reference
- Build image: `docker build -t performance-predictor .`
- Run container: `docker run -p 8080:8080 performance-predictor`
- View logs: `docker logs <container_id>`
- Stop container: `docker stop <container_id>`
- Remove container: `docker rm <container_id>`
- Remove image: `docker rmi performance-predictor`

### Option 2: Local Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the package:
   ```bash
   pip install -e .  # For development
   # OR
   pip install .     # For production
   ```

3. Run the application:
   ```bash
   gunicorn --bind 0.0.0.0:8080 app.app:app
   ```

4. Access the application at http://localhost:8080

### Environment Variables

The following environment variables can be configured:

- `FLASK_ENV`: Set to 'production' for production deployment
- `MODEL_PATH`: Path to save/load the trained model (default: 'models/performance_model.h5')
- `PORT`: Port number for the application (default: 8080)
- `HOST`: Host address to bind to (default: 0.0.0.0)

### Production Deployment

For production deployment, it's recommended to:

1. Use a reverse proxy (like Nginx) in front of the application
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8080;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

2. Set up SSL/TLS certificates using Let's Encrypt or similar service

3. Configure proper logging
   - Application logs: `/var/log/performance-predictor/app.log`
   - Access logs: `/var/log/performance-predictor/access.log`
   - Error logs: `/var/log/performance-predictor/error.log`

4. Use environment variables for sensitive configuration
   - Create a `.env` file for local development
   - Use system environment variables in production

5. Set up monitoring and alerting
   - Use Prometheus for metrics collection
   - Configure Grafana dashboards
   - Set up alerting rules

### System Requirements

- Python 3.9 or higher
- 4GB RAM minimum
- 2 CPU cores minimum
- 1GB disk space
- Docker (for containerized deployment)
- Nginx (for production deployment)

### Troubleshooting

1. Docker Issues:
   - If container fails to start, check logs: `docker logs <container_id>`
   - Ensure port 8080 is not in use: `lsof -i :8080`
   - Verify Docker daemon is running: `systemctl status docker`

2. Local Installation Issues:
   - If dependencies fail to install, try: `pip install --upgrade pip`
   - For TensorFlow issues, ensure you have the correct Python version
   - Check virtual environment is activated: `which python`

3. Application Issues:
   - Check application logs in `/var/log/performance-predictor/`
   - Verify environment variables are set correctly
   - Ensure model files are in the correct location 