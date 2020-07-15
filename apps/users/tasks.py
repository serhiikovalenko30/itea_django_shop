from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task
def add_task(a, b):
    return a + b


@shared_task
def send_mail_task(subject, message, to, **kwargs):
    send_mail(
        subject, message, settings.EMAIL_HOST_USER, to, **kwargs
    )
