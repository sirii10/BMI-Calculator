# BMI Calculator with Docker

## Overview
This is a simple BMI Calculator console application built with Python. The application takes user input (weight in kg and height in feet & inches), calculates the BMI, and logs the result in a file.

## Features
- Takes user input for weight and height
- Converts height to meters
- Calculates BMI and determines the category
- Logs the results to a text file in a Docker volume

## Setup Instructions
# BMI Calculator Docker Setup

This guide provides step-by-step instructions to set up and run the BMI Calculator application using Docker.

## Prerequisites

Before proceeding, ensure you have the following installed on your system:

- **Docker**: If not installed, download and install it from [Docker's official website](https://www.docker.com/).
- **Terminal or Command Line Interface (CLI)**: You’ll use this to run commands.

## Steps to Set Up and Run the BMI Calculator

### Step 1: Navigate to the Project Directory

1. Open a terminal.
2. Navigate to the project folder where the application files are located using the `cd` command:

   **cd /Users/udaynathyerramsetty/Downloads/Graded-1**

### Running the Application with Docker
1. **Build the Docker Image:**
  
   **docker build -t bmi-calculator:<tag-name> .**

Explanation:
*	docker build - Creates a Docker image.
*	-t bmi-calculator:<TAG-NAME> - Assigns a tag (<TAG-NAME>).
*	. - Uses the current directory as the build context.
   
3. **Run the Container:**
  
   **docker run --rm -v $(pwd)/data:/data -it bmi-calculator:<tag-name>**

Explanation:
*	docker run - Starts a new container.
*	--rm - Removes the container after execution.
*	-v $(pwd)/data:/data - Mounts the data/ folder.
*	-it - Runs interactively.
*	bmi-calculator:<TAG-NAME> - Uses the built image.
   
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

