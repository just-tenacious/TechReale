from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
import random
import string

def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

conf = ConnectionConfig(
    MAIL_USERNAME="just.tenacious05@gmail.com",
    MAIL_PASSWORD="gewo loof kcxj vgkf",
    MAIL_FROM="just.tenacious05@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,      
    MAIL_SSL_TLS=False,       
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True       
)

async def send_password_email(email: EmailStr, password: str):
    message = MessageSchema(
        subject="Your Account Password",
        recipients=[email],
        body=f"Hello,\n\nYour account has been created.\n\nPassword: {password}\n\nPlease log in and change it.",
        subtype="plain"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    print(f"Password email sent to {email}")