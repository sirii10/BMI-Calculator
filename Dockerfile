# Use official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY bmiapp.py /app/

# Set up a volume for storing BMI results
VOLUME ["/data"]

# Set the entry point to run the script
CMD ["python", "bmiapp.py"]