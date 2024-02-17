from django.urls import path

from apps.accounts.views import LoginAPIView, SellerListAPIView, RegisterView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('sellers/', SellerListAPIView.as_view(), name='seller-list'),
    path('register/', RegisterView.as_view(), name='register'),
]