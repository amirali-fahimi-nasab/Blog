from django.urls import path

from . import views as accounts_views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView




urlpatterns = [
    path('register/',accounts_views.UserRegisterView.as_view(),name='user_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

#
# router = routers.SimpleRouter()
# router.register('user',accounts_views.UserViewSet)
# urlpatterns+=router.urls
#
#
#
#
