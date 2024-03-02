from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserLoginView(APIView):
    def post(self, request):
        # This is a shortcut/hack to avoid overloading / rewritting the default django validation
        try:
            not_validated_user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=401)

        user = authenticate(username=not_validated_user.username, password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)