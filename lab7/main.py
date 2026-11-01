
import os
import shutil
import smtplib
from email.message import EmailMessage

THRESHOLD = 80
SERVER_PATH = "/"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["OWNER_EMAIL"]
    msg.set_content(body)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(
            os.environ["EMAIL_USER"],
            os.environ["EMAIL_PASSWORD"]
        )
        server.send_message(msg)

def main():
    usage = shutil.disk_usage(SERVER_PATH)
    used_percent = usage.used / usage.total * 100

    print(f"Disk usage: {used_percent:.1f}%")

    if used_percent >= THRESHOLD:
        send_email(
            "Server disk usage warning",
            f"Disk usage has reached {used_percent:.1f}%."
        )

if __name__ == "__main__":
    main()

