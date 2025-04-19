# Use an official Python runtime as a parent image
FROM python:3.12.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files from bike_sharing_api/app to /app in the container
#COPY app /app
RUN mkdir -p /app/artifacts
COPY artifacts/*.csv /app/artifacts/*.csv
COPY artifacts/*.pkl /app/artifacts/*.pkl

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt
COPY application.py /app/application.py

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Expose port 5000 (default Flask port)
EXPOSE 5000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the Flask application
CMD ["python", "application.py"]
