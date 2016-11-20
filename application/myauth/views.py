from django.shortcuts import render

from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from myauth.models import Account
from myauth.permissions import IsAccountOwner
from myauth.serializers import AccountSerializer

from django.contrib.auth import authenticate, login, logout


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        validateData(request.data)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

def validateData(data):
    email = data.get('email', None)
    username = data.get('username', None)

    if Account.objects.filter(email=email).exists():
        return Response({
            'status': 'Unprocessable entity',
            'message': 'Found existing account for email: ' + str(email)
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if Account.objects.filter(username=username).exists():
        return Response({
            'status': 'Unprocessable entity',
            'message': 'Found existing account with username: ' + str(username)
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(views.APIView):
    def post(self, request, format=None):
        username = request.data.get('username', None)

        if Account.objects.filter(username=username).exists() == False:
            return Response({
                'status': 'Bad request',
                'message': 'Invalid username.'
            }, status=status.HTTP_400_BAD_REQUEST)

        password = request.data.get('password', None)

        account = authenticate(username=username, password=password)

        if account is not None:
            login(request, account)
            serialized = AccountSerializer(account)

            return Response(serialized.data)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Invalid password.'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)
