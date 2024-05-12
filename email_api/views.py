# email_api/views.py
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import choice


@api_view(["GET"])
def send_emails(request, num_emails):
    options = [
        "hello",
        "u shouldn't have given me ur email",
        "computer science >>>>>> animal care",
        "u might be able to sign me up to ur cat websites but i can spam u",
        "hfuvehdih",
        "nerd",
        "failing life",
        "jalapenos on top",
        "carrots are good with everything",
    ]
    # Email configuration
    sender_email = "jakeharris30@outlook.com"
    receiver_email = "effiehemail@gmail.com"
    password = os.getenv("OUTLOOK_PASSWORD")

    if not password:
        return Response(
            {"error": "OUTLOOK_PASSWORD environment variable not set."}, status=500
        )

    # Create message container

    # Connect to Outlook's SMTP server
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()

    try:
        # Login to your Outlook account
        server.login(sender_email, password)

        # Send the emails
        for i in range(num_emails):
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = choice(
                ["hi", "hello", "WWAAAASSSSSUUUUPPPP", "greetings cat lover"]
            )

            # Email body
            body = choice(options)
            message.attach(MIMEText(body, "plain"))
            server.sendmail(sender_email, receiver_email, message.as_string())

        # Return success response
        return Response(
            {"message": f"{num_emails} emails sent to {receiver_email} successfully."},
            status=200,
        )
    except smtplib.SMTPAuthenticationError as e:
        # Log the error message
        logging.error(f"SMTP authentication failed: {e}")

    except Exception as e:
        # Return error response
        return Response(
            {
                "error": str(e),
                "password": password,
            },
            status=500,
        )
    finally:
        # Quit the server
        server.quit()
