import subprocess
import time
import os

# Function to start the Flask application
def start_flask_app():
    return subprocess.Popen(["python", "main.py"])

# Function to start Locust
def start_locust():
    return subprocess.Popen(["locust", "-f", "locustfile.py", "--host=http://127.0.0.1:5000"])

# Start the Flask application
flask_process = start_flask_app()

# Give Flask a few seconds to start
time.sleep(5)

# Start Locust
locust_process = start_locust()

try:
    # Wait for the Locust process to complete
    locust_process.wait()
finally:
    # Terminate the Flask application
    flask_process.terminate()
