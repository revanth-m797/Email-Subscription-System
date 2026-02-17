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

def send_welcome(mail):
    html_text='''<!DOCTYPE html>
                <html>
                <body style="font-family: Arial, sans-serif; background:#f5f5f5; padding:20px;">
                    
                    <table width="100%" cellpadding="0" cellspacing="0">
                    <tr>
                        <td align="center">
                        
                        <table width="500" cellpadding="0" cellspacing="0" style="background:#ffffff; border-radius:6px; padding:20px;">
                            <tr>
                            <td align="center">
                                <h2 style="color:#2c3e50;">Welcome! 🎉</h2>
                            </td>
                            </tr>

                            <tr>
                            <td>
                                <p>Hello,</p>
                                <p>
                                Thank you for subscribing to our service.  
                                We're excited to have you with us!
                                </p>

                                <p>
                                You will now receive updates and important notifications.
                                </p>

                                <p style="margin-top:20px;">
                                Regards,<br>
                                <strong>Your Team</strong>
                                </p>
                            </td>
                            </tr>

                        </table>

                        </td>
                    </tr>
                    </table>

                </body>
                </html>
                '''
    yag=yagmail.SMTP("testerzen12345@gmail.com","kmom eqmr umyn zdfp")
    yag.send(to=mail,subject="Welcome!!!",contents=html_text)

send_welcome("revanth797@gmail.com")