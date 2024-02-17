from rest_framework_simplejwt.views import TokenObtainPairView

from apps.accounts.pemissions import AnonPermission
from apps.accounts.serializers import MyTokenSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenSerializer