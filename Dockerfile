# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install FFmpeg and other necessary system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY streamlit-app/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the streamlit-app directory contents into the container at /app
COPY streamlit-app /app

# Copy the .env file into the container
COPY .env .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Set environment variables from .env file
ENV $(cat .env | xargs)

# Run main.py when the container launches
CMD ["streamlit", "run", "--server.port", "8080", "--server.address", "0.0.0.0", "main.py"]
