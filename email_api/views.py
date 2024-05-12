# email_api/views.py
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import choice
import logging
from django.core.mail import send_mail  #
from django.http import HttpResponse


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
    res = {}

    if not password:
        res["error"] = "OUTLOOK_PASSWORD environment variable not set."
        return Response({res}, status=500)

    # Create message container

    # Connect to Outlook's SMTP server
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()

    try:
        # Login to your Outlook account
        # server.login(sender_email, password)

        # Send the emails
        for i in range(num_emails):
            # message = MIMEMultipart()
            # message["From"] = sender_email
            # message["To"] = receiver_email
            # message["Subject"] = choice(
            #     ["hi", "hello", "WWAAAASSSSSUUUUPPPP", "greetings cat lover"]
            # )

            subject = choice(
                ["hi", "hello", "WWAAAASSSSSUUUUPPPP", "greetings cat lover"]
            )

            # Email body
            body = choice(options)
            # message.attach(MIMEText(body, "plain"))
            # server.sendmail(sender_email, receiver_email, message.as_string())

            send_mail(
                subject,
                body,
                "jakeharris30@outlook.com",
                ["effiehemail@gmail.com"],
                fail_silently=False,
            )

        # Return success response
        return Response(
            {
                "message": f"{num_emails} emails sent to {receiver_email} successfully.",
                "Access-Control-Allow-Origin": "*",
            },
            status=200,
        )
    except smtplib.SMTPAuthenticationError as e:
        # Log the error message
        logging.error(f"SMTP authentication failed: {e}")
        return Response(
            {"error": str(e), "Access-Control-Allow-Origin": "*"}, status=500
        )

    except Exception as e:
        # Return error response
        return Response(
            {"error": str(e), "Access-Control-Allow-Origin": "*"},
            status=500,
        )
    finally:
        # Quit the server
        server.quit()
