from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from lms.models import Lesson, Course
from users.models import User

class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        """Тестирование функции создания урока"""
        # User.objects.create(email='tester@gmail.com', password='13799731')
        # self.user = User.objects.get(email='tester@gmail.com')
        data = {
            'title': 'LessonTestCase',
            'description': 'test test test',
            'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            # 'author': self.user
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )
        # print(self.user.__dict__)
        # print(response.json)
        # print(self.client)
        """PERMISSION IN VIEWS.PY"""
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_lesson(self):

        Lesson.objects.create(
            title='LessonTestCase',
            description='test test test'
        )

        response = self.client.get('/lesson/')
        print(response.json())

        """PERMISSION IN VIEWS.PY"""
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )