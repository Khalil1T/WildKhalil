from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenSerializer, cls).get_token(user)
        token['email'] = user.email
        token['is_Seller'] = user.is_Seller
        return token