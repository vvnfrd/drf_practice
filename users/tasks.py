import datetime

from django.conf import settings
from django.core.mail import send_mail
from users.models import Subscription, User
from rest_framework.response import Response
from celery import shared_task

@shared_task
def send_mailing(instance, model):
    if model == 'Course':
        subscriptions = Subscription.objects.filter(course_id=instance.pk)
        email_list = []
        for i in subscriptions:
            email = i.user.email
            email_list.append(email)

        send_mail(
                subject=f'Курс {instance.title} обновлён',
                message=f'Курс {instance.title} обновлён\nПосмотрите что добавили нового',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email_list
        )
        return Response(data={'message': 'Подписчики уведомлены'})

    elif model == 'Lesson':
        subscriptions = Subscription.objects.filter(lesson_id=instance.pk)
        email_list = []
        for i in subscriptions:
            email = i.user.email
            email_list.append(email)

        send_mail(
            subject=f'Урок {instance.title} обновлён',
            message=f'Урок {instance.title} обновлён\nПосмотрите что добавили нового',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_list
        )
        return Response(data={'message': 'Подписчики уведомлены'})

@shared_task
def user_turn_is_active():
    user_list = User.objects.filter(is_active=True)
    time_now = datetime.datetime.now(datetime.timezone.utc)
    for user in user_list:
        try:
            if time_now - user.last_login > datetime.timedelta(days=30):
                print(f'User {user.email} is not active')
                user.is_active = False
                user.save()
        except TypeError:
            user.last_login = datetime.datetime.now(datetime.timezone.utc)
            user.save()
            print(f'User {user.email} last_login updated')
