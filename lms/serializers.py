from rest_framework import serializers
# from rest_framework.permissions import IsAuthenticated
from lms.models import Course, Lesson
from lms.validators import VideoUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoUrlValidator(field="video_url")]


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_quantity = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lessons_quantity(self, course):
        return Lesson.objects.filter(course_id=course.id).count()

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'lessons_quantity', 'lessons', 'author')