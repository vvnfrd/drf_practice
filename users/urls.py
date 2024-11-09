from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, RegisterAPIView, SubscriptionAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # C User
    path('register/', RegisterAPIView.as_view(), name='register'),

    #Subscription turn on/off
    path('subscription/', SubscriptionAPIView.as_view(), name='subscription-create'),
]