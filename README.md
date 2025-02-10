# BMI Calculator with Docker

## Overview
This is a simple BMI Calculator console application built with Python. The application takes user input (weight in kg and height in feet & inches), calculates the BMI, and logs the result in a file.

## Features
- Takes user input for weight and height
- Converts height to meters
- Calculates BMI and determines the category
- Logs the results to a text file in a Docker volume

## Setup Instructions
### Running the Application with Docker
1. **Build the Docker Image:**
  
   docker build -t bmi-calculator:<tag name> .
   
2. **Run the Container:**
  
   docker run --rm -v $(pwd)/data:/data -it bmi-calculator:<tag name>
   
   This mounts a `data` directory to persist BMI results.

## Docker Concepts Used
- **Base Image:** Uses Python 3.9 official base image.
- **Working Directory:** The application runs in `/app`.
- **COPY Directive:** Copies the script into the container.
- **VOLUME:** Mounts a `/data` directory for persistent logs.
- **CMD:** Runs the Python script on container startup.

## Example Output

BMI Calculator
Enter your weight in kg: 70
Enter your height - Feet: 5
Enter your height - Inches: 8
Your BMI: 22.1 (Normal weight)
Result saved to /data/bmi_results.txt


## Screenshots
1. Docker image successfully built for the  application
![image](https://github.com/user-attachments/assets/408691f8-b812-4a38-894e-cf8c2369e9a8)

2. Docker container spinning to successfully running application.
![image](https://github.com/user-attachments/assets/11fc3e96-f33c-4167-b8eb-215d78ba4764)

## Repository Structure
/
│── bmi_calculator.py
│── Dockerfile
│── README.md
│── data/ (mounted volume for results)

