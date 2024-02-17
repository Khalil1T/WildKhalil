from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.accounts.models import User
from apps.accounts.pemissions import AnonPermission
from apps.accounts.serializers import MyTokenSerializer, UserSerializers


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenSerializer


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            seller = User.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone=request.data['phone'],
                address=request.data['address'],
                is_Seller=True,
            )
            seller.set_password(request.data['password'])
            seller.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

