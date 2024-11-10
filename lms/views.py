from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from lms.models import Course, Lesson
from lms.paginators import StudyPaginator
from users.permissions import IsNotModerator, IsOwner
from lms.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer

"""CRUD Course"""


class CourseViewSet(viewsets.ModelViewSet):
    request = {}
    user = {}
    queryset = Course.objects.all()
    pagination_class = StudyPaginator

    """Оформляю всятие реквеста для каждого CRUD вьюсета"""

    def destroy(self, request, *args, **kwargs):
        """Delete course"""
        self.request = request
        self.user = request.user
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        """Check info about course"""
        self.request = request
        self.user = request.user
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """Update course"""
        self.request = request
        self.user = request.user
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """Partial update course"""
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """Get list of courses"""
        self.request = request
        self.user = request.user
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.author = self.request.user
        new_course.save()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def get_queryset(self):
        try:
            print(self.user.__dict__)
            if self.user.is_superuser or self.user.groups.filter(name='moderator').exists():
                return Course.objects.all()
            else:
                return Course.objects.filter(author=self.request.user)
        except AttributeError:
            """fix for swagger"""
            return []


"""CRUD Lesson"""


class LessonCreateAPIView(generics.CreateAPIView):
    """Create a lesson"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsNotModerator]

    def perform_create(self, serializer):
        try:
            new_lesson = serializer.save()
            new_lesson.author = self.request.user
            new_lesson.save()
        except ValueError:
            pass


class LessonListAPIView(generics.ListAPIView):
    """Get lesson's list"""
    request = {}
    user = {}
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StudyPaginator

    def get(self, request, *args, **kwargs):
        self.request = request
        self.user = request.user
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        if self.user.is_superuser or self.user.groups.filter(name='moderator').exists():
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(author=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Get detail info about lesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Update lesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Delete lesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated, IsOwner|IsAdminUser]