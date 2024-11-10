from django.template.context_processors import request
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory

from lms.models import Lesson, Course
from lms.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from users.models import User

class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            email='lesson_tester@gmail.com',
            password='13799731'
        )

    def test_create_lesson(self):

        """Тестирование функции создания урока"""

        view = LessonCreateAPIView.as_view()
        request = self.factory.post('/lesson/create/',
                               {'title': 'test_create_lesson',
                                'description': 'test test test',
                                'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_lesson(self):

        """Тестирование функции просмотра уроков"""

        lesson = Lesson.objects.create(
            title='test_list_lesson',
            description='test test test',
            video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            author=self.user
        )

        view = LessonListAPIView.as_view()
        request = self.factory.get('/lesson/')
        force_authenticate(request, user=self.user)
        response = view(request)
        result = [{'id': lesson.id, 'title': 'test_list_lesson',
                   'description': 'test test test', 'preview': None,
                   'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'course_id': None,
                   'author': self.user.id}]
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(response.data['results'], result)

    def test_retrieve_lesson(self):

        """Тестирование функции просмотра урока"""

        view = LessonRetrieveAPIView.as_view()

        lesson = Lesson.objects.create(
            title='test_retrieve_lesson',
            description='test test test',
            video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            author=self.user
        )

        request = self.factory.get('lesson/')
        force_authenticate(request, user=self.user)
        response = view(request, pk=lesson.id)
        result = {'id': lesson.id, 'title': 'test_retrieve_lesson',
                  'description': 'test test test', 'preview': None,
                  'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                  'course_id': None, 'author': self.user.id}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, result)

    def test_update_lesson(self):

        """Тестирование функции обновления урока"""

        view = LessonUpdateAPIView.as_view()
        lesson = Lesson.objects.create(
            title='test_update_lesson',
            description='test test test',
            video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            author=self.user
        )
        data = {'title': 'test_updated_lesson',
                'video_url': 'https://www.youtube.com/watch?v=E9de-cmycx8'}
        request = self.factory.patch('lesson/update/', data=data)
        force_authenticate(request, user=self.user)
        response = view(request, pk=lesson.id)
        result = {'id': lesson.id, 'title': 'test_updated_lesson',
                  'description': 'test test test', 'preview': None,
                  'video_url': 'https://www.youtube.com/watch?v=E9de-cmycx8',
                  'course_id': None, 'author': self.user.id}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, result)

    def test_delete_lesson(self):

        """Тестирование функции удаления урока"""

        view = LessonDestroyAPIView.as_view()

        lesson = Lesson.objects.create(
            title='test_delete_lesson',
            description='test test test',
            video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            author=self.user
        )
        before = Lesson.objects.filter(title='test_delete_lesson').exists()
        request = self.factory.delete('lesson/')
        force_authenticate(request, user=self.user)
        response = view(request, pk=lesson.id)
        after = Lesson.objects.filter(title='test_delete_lesson').exists()
        self.assertTrue(before)
        self.assertFalse(after)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)