# Email Subscription System

A full-stack email subscription system built using Flask, MySQL, and JavaScript.  
This project allows users to subscribe using email verification with OTP authentication.

# Features

- OTP-based email verification
- Secure email subscription flow
- REST API backend using Flask
- MySQL database integration
- SMTP-based email delivery(yagmail)
- JSON-based frontend-backend

# Create a .env file contianing

DB_HOST=''
DB_USER=''
DB_PASS=''
DB_NAME=''

email=""
app_pass=""

# Setup MySQL DB

run this in your MySQL workbench

Create DATABASE email_subscribers;
Create Table customerInfo(
        Id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(30),
        phone VARCHAR(15),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

# Run the application

python app.py

visit http://127.0.0.1:5500/project/index.html