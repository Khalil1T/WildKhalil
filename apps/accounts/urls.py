from django.urls import path

from apps.accounts.views import LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
]