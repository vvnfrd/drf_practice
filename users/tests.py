from django.template.context_processors import request
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory

from lms.models import Course
from users.models import User, Subscription
from users.views import SubscriptionAPIView


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            email='subscription_tester@gmail.com',
            password='13799731'
        )

    def test_create_and_delete_subscription(self):

        """Тестирование функции создания подписки"""

        course = Course.objects.create(
            title='test_create_subscription',
            description='test test test',
            author=self.user

        )
        view = SubscriptionAPIView.as_view()
        request = self.factory.post('/users/subscription/', {'course_id':course.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        created = Subscription.objects.filter(user=self.user).exists()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Тестирование функции удаления подписки"""

        request = self.factory.post('/users/subscription/', {'course_id': course.id})
        force_authenticate(request, user=self.user)
        response = view(request)
        deleted = Subscription.objects.filter(user=self.user).exists()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(created)
        self.assertFalse(deleted)
