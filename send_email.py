import yagmail
import random
import os
from dotenv import load_dotenv

load_dotenv()

def send_mail(mail):
    yag=yagmail.SMTP(os.getenv("email"),os.getenv("app_pass"))
    yag.send(to=mail,subject="Welcome!!!",contents="Thanks for subscribing")

def send_verification(mail):
    yag=yagmail.SMTP(os.getenv("email"),os.getenv("app_pass"))
    num=random.randint(10000,50000)
    yag.send(to=mail,subject="Verification code",contents=f"Here is your verification code {num}")
    return num
