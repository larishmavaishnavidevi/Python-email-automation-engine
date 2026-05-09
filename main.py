import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from email.message import EmailMessage
import aiosmtplib

# 1. Load the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI()

# 2. Fetch credentials
SMTP_HOST = os.getenv("MAIL_SERVER")
SMTP_PORT = int(os.getenv("MAIL_PORT", 587))
SMTP_USER = os.getenv("MAIL_USERNAME")
SMTP_PASS = os.getenv("MAIL_PASSWORD")

@app.get("/")
def home():
    return {"Status": "Email Engine Active", "User": SMTP_USER}

# 3. NEW: Endpoint to send a test email
@app.post("/send-test-email")
async def send_test_email():
    message = EmailMessage()
    message["From"] = SMTP_USER
    message["To"] = SMTP_USER  # Sending it to yourself for testing
    message["Subject"] = "Test from your Automation Engine"
    message.set_content("Success! Your FastAPI Email Engine is now sending messages.")

    try:
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SMTP_USER,
            password=SMTP_PASS,
            use_tls=False,
            start_tls=True,
        )
        return {"message": f"Test email sent successfully to {SMTP_USER}"}
    except Exception as e:
        return {"error": str(e)}