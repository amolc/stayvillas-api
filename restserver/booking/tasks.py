
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream import ic

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def sendmail_smtp(recipient,subject,body):

    SMTP_SERVER = 'smtp.zoho.in'
    SMTP_PORT = 587  # For TLS
    USERNAME = 'support@stayvillas.co'
    PASSWORD = '10gXWOqeaf1'  # Replace with your password or app-specific password
    # Email content
    sender = 'support@stayvillas.co'

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        # Add attachment

        # Connect to SMTP server
        smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(USERNAME, PASSWORD)

        # Send email
        smtp.sendmail(sender, recipient, msg.as_string())
        print("Email sent successfully!")

        smtp.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")


def send_booking_email_smtp(recipient, subject, body_text, body_html):
    body = f'''
    {body_text}
    {body_html}
    '''
    sendmail_smtp(recipient, subject, body)
    sendmail_smtp("support@pamosapicks.com", subject, body)
    sendmail_smtp("amolch001@gmail.com", subject, body)
