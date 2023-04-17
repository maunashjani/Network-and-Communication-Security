import smtplib
from cryptography.fernet import Fernet

# Set up the SMTP server and credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sender-email id'
smtp_password = 'sender-password'

# Set up the email parameters
sender = 'sender-email id'
recipient = 'receiver-email id'
subject = 'Testing Email'
message = 'Hello World! This is a test email.'

# Generate a secret key for encrypting the message
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt the message
encrypted_message = cipher.encrypt(message.encode('utf-8'))

# Construct the email message
msg = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{message}"

# Construct the encrypted email message
#msg = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{encrypted_message.decode('utf-8')}"

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(sender, recipient, msg)

print("Email sent successfully!")