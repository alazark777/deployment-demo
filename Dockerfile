# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /user/src/app

# Copy application files
COPY . .

# Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5001

# Start the Flask app
CMD ["python", "./flask_api.py"]