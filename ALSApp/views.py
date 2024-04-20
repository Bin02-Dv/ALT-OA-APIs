from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import AuthApiModelSerializer
from .models import AuthApiModel
import jwt, datetime
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .decorators import add_cors_headers

@add_cors_headers
class SignUpView(APIView):
    def post(self, request):
        serializer = AuthApiModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@add_cors_headers
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = AuthApiModel.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Email not found!!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        message = "Login success....."

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token,
            'msg': message
        }
        
        return response

@add_cors_headers
class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('User Unauthenticated!!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('User Unauthenticated!!')
        
        user = AuthApiModel.objects.filter(id=payload['id']).first()

        serializer = AuthApiModelSerializer(user)

        return Response(serializer.data)

@add_cors_headers
class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout Successful..'
        }

        return response

@add_cors_headers
class AllUserView(APIView):

    def get(self, request):
        users = AuthApiModel.objects.all()
        serializer = AuthApiModelSerializer(users, many=True)
        return Response(serializer.data)