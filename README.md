# Website Monitoring & Alert System

Python se bana hua ek automatic system jo websites ko check karta hai, agar koi website DOWN ho jaye to email se alert bhejta hai, or history ko CSV file me save karta hai.

## Features
- Har 60 second baad websites check karta hai
- Website DOWN hone par email alert bhejta hai
- Website wapas UP hone par recovery email bhejta hai
- Uptime history ko uptime_history.csv me save karta hai
- Docker support ke saath## Project Files
- monitor.py - Main monitoring code
- requirements.txt - Zaroori libraries
- Dockerfile - Docker ke liye
- docker-compose.yml - Docker Compose ke liye
- .env - Email or websites ki settings (secret)
- uptime_history.csv - Monitoring history## Setup

1. Python libraries install karein:
pip install -r requirements.txt

2. .env file banayein:
WEBSITES=https://www.google.com,https://www.github.com
CHECK_INTERVAL=60
EMAIL_FROM=apka_email@gmail.com
EMAIL_TO=jis_ko_alert_bhejna_hai@gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=apka_email@gmail.com
SMTP_PASSWORD=apka_app_password

3. Program chalao:
python monitor.py

## Docker se Chalana
docker compose up --build

## Kaise Kaam Karta Hai?
1. Har website ko open karke status code check karta hai
2. Agar status 200 hai to UP, warna DOWN
3. DOWN hone par turant email bhejta hai
4. Sab kuch CSV me save karta hai