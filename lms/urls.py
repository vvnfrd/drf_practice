from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, StripeCreateCourseAPIView, StripeCreateLessonAPIView, StripeSetPriceCourseAPIView, \
    StripeSetPriceLessonAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-info'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('courses/create_product/<int:pk>', StripeCreateCourseAPIView.as_view(), name='course-create-product'),
    path('lesson/create_product/<int:pk>', StripeCreateLessonAPIView.as_view(), name='lesson-create-product'),
    path('courses/set_price/<int:pk>', StripeSetPriceCourseAPIView.as_view(), name='course-setprice-product'),
    path('lesson/set_price/<int:pk>', StripeSetPriceLessonAPIView.as_view(), name='lesson-setprice-product'),
    path('lesson/set_price/<int:pk>', StripeSetPriceLessonAPIView.as_view(), name='lesson-setprice-product'),
] + router.urls