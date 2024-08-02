import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_score_email(student_id, student_name, email, score):
    # Email configuration
    sender_email = "your_email@gmail.com"  # Replace with your email address
    sender_password = "your_email_password"  # Replace with your email password
    subject = "Test Score Notification"

    # Email body
    body = f"Dear {student_name},\n\nCongratulations! Your test score is {score}.\n\nBest regards,\nYour School"

    # Create message object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject

    # Attach body as plain text
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, email, message.as_string())

# Read the data from CSV file
file_path = "E:\Data.xlsx"  # Replace with the actual file path
data = pd.read_csv(file_path)

# Iterate through the rows and send emails
for index, row in data.iterrows():
    student_id = row["Student id"]
    student_name = row["Student Name"]
    email = row["Mail-id"]
    score = row["Score"]

    send_score_email(student_id, student_name, email, score)

print("Emails sent successfully.")
