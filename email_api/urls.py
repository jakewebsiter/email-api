# email_api/urls.py
from django.urls import path
from .views import send_emails

urlpatterns = [
    path("send-emails/<int:num_emails>/", send_emails, name="send_emails"),
]
