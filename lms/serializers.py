from rest_framework import serializers

from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_quantity = serializers.SerializerMethodField()

    def get_lessons_quantity(self, course):
        return Lesson.objects.filter(course_id=course.id).count()

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'lessons_quantity')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'