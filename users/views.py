from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from lms.models import Course
from users.models import Payment, Subscription
from users.permissions import IsModerator, IsSubscriber, IsOwner
from users.serializers import PaymentSerializer, RegisterSerializer, \
    SubscriptionSerializer
from users.models import User
from django.views.generic import CreateView, UpdateView, ListView, DetailView


"""PaymentListView"""


class PaymentListAPIView(generics.ListAPIView):
    """Get list of payment"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('method', 'course_id', 'lesson_id')
    ordering_fileds = ('date')



"""Сервис пользователя"""


class RegisterAPIView(generics.CreateAPIView):
    """Register account"""
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


# class RetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = RetrieveSerializer
#     queryset = User.objects.all()
#
#
# class UpdateAPIView(generics.UpdateAPIView):
#     serializer_class = UpdateSerializer
#     queryset = User.objects.all()

"""Сервис подписок"""

class SubscriptionAPIView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    request = {}
    user = {}
    queryset = Subscription.objects.all()

    def post(self, request, *args, **kwargs):
        """Create or delete subscription"""
        try:
            user = self.request.user
            course_id = self.request.data['course_id']
            course_item = get_object_or_404(Course, pk=course_id)
            subs_item = Subscription.objects.filter(user=user, course_id=course_id)
            if subs_item.exists():
                subs_item.delete()
                message = 'Подписка удалена'
            else:
                sub = Subscription(user=user, course_id=course_item)
                sub.save()
                message = 'Подписка добавлена'
            return Response({"message": message})
        except KeyError:
            return Response({"Необходимые параметры": "course_id"})

    def get(self, request, *args, **kwargs):
        """Get list of subscription"""
        self.request = request
        self.user = request.user
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        if self.user.is_superuser or self.user.groups.filter(name='moderator').exists():
            return Subscription.objects.all()
        else:
            return Subscription.objects.filter(user=self.request.user)