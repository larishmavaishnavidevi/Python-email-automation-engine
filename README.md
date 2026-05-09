🚀 Python Email Automation Engine

A high-performance, asynchronous email automation system built using FastAPI and aiosmtplib. This project is designed to handle automated communication securely and efficiently.



✨ Key Features

FastAPI Framework: Modern Python for a fast and interactive API experience.



Asynchronous Processing: Uses aiosmtplib to ensure the server remains responsive while sending emails.



Secure Configuration: Implements .env management to keep sensitive SMTP credentials off version control.



Visual Proof: Includes a Swagger UI Dashboard screenshot in the outputs/ folder confirming functional endpoints.



🛠️ Project Structure

main.py: The core application logic and API endpoints.



outputs/: Contains the Swagger UI Dashboard.jpeg proving the engine is active.



.env.example: A template for environment variables to help other developers set up the project.



requirements.txt: List of all necessary Python libraries for one-click installation.



🚀 Getting Started

Clone the repository:



Bash

git clone https://github.com/larishmavaishnavidevi/Python-email-automation-engine.git

Set up your environment:

Create a .env file in the root directory based on the .env.example provided.



Install dependencies:



Bash

pip install -r requirements.txt

Run the server:



Bash

uvicorn main:app --reload

Test the Engine:

Visit http://127.0.0.1:8000/docs to send a test email via the interactive dashboard.

