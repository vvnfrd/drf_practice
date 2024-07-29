from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

        users_list = [
            {'email': 'user1@gmail.com'},
            {'email': 'user2@gmail.com'},
            {'email': 'user3@gmail.com'},
            {'email': 'user4@gmail.com'}
        ]

        users_for_create = []
        for users_item in users_list:
            users_for_create.append(
                User(**users_item)
            )
        User.objects.bulk_create(users_for_create)

        payments_list = [
            {'user': User.objects.get(email='user1@gmail.com'), 'course_id': Course.objects.all()[0], 'lesson_id': Lesson.objects.all()[0], 'value': 10000, 'method': 'sbp'},
            {'user': User.objects.get(email='user2@gmail.com'), 'course_id': Course.objects.all()[0], 'lesson_id': Lesson.objects.all()[0], 'value': 20000, 'method': 'cash'},
            {'user': User.objects.get(email='user3@gmail.com'), 'course_id': Course.objects.all()[0], 'lesson_id': Lesson.objects.all()[0], 'value': 15000, 'method': 'sbp'},
            {'user': User.objects.get(email='user4@gmail.com'), 'course_id': Course.objects.all()[0], 'lesson_id': Lesson.objects.all()[0], 'value': 12000, 'method': 'cash'}
        ]

        payments_for_create = []
        for payment_item in payments_list:
            payments_for_create.append(
                Payment(**payment_item)
            )
        Payment.objects.bulk_create(payments_for_create)