from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import RecoveryPasswordRequestView, RecoveryPasswordView, UserActivateView
from apps.users.views import MeView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/me', MeView.as_view(), name='auth_me'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='auth_activate'),
    path('/recovery', RecoveryPasswordRequestView.as_view(), name='auth_recovery_request'),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view(), name='auth_recovery')
]
