from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import AccountSerializer


class ApiLoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.id
        })


class ObtainAccount(viewsets.ViewSet):
    authentication_classes = [authentication.TokenAuthentication]

    def list(self, request):
        pass

    def create(self, request):
        serializer = AccountSerializer(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'id': user.id
        })

    def retrieve(self, request, pk=None):
        qeuryset = User.objects.all()
        user = get_object_or_404(qeuryset, pk=pk)
        serializer = AccountSerializer(user)
        token, _ = Token.objects.get_or_create(user=user)
        response = serializer.data
        response.update({"token": token.key})
        return Response(response)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


get_account = ObtainAccount.as_view({'get': 'retrieve'})
register = ObtainAccount.as_view({'get': 'create'})
