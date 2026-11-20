import requests
import time
import csv
import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

WEBSITES = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.thiswebsitedoesnotexist12345.com",
]

def send_email(website, status):
    subject = f"ALERT: {website} is {status}!"
    body = f"Website: {website}\nStatus: {status}\nTime: {datetime.now()}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"Email bhej diya: {website} is {status}")
    except Exception as e:
        print(f"Email nahi bheja gaya: {e}")

def check_website(url):
    try:
        start = time.time()
        r = requests.get(url, timeout=5)
        elapsed = round(time.time() - start, 2)
        if r.status_code == 200:
            return "UP", r.status_code, elapsed
        else:
            return "DOWN", r.status_code, elapsed
    except Exception as e:
        return "DOWN", "ERROR", 0

print("Monitoring shuru ho gaya... Ctrl+C dabao band karne ke liye")

while True:
    for url in WEBSITES:
        status, code, resp_time = check_website(url)
        print(f"{url} | {status} | Status: {code} | Time: {resp_time}s")
        
        # CSV me save karo
        with open("uptime_history.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), url, status, code, resp_time])

        if status == "DOWN":
            send_email(url, status)

    print("--- phir dobara check hoga ---")
    time.sleep(30)