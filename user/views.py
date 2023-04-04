from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from .serializers import UserSerializer
from .models import User
from django.http import Http404
# Create your views here.


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetailedUserView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id = id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id = id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id):
        user = self.get_object(id = id)
        serializer = UserSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        user = self.get_object(id = id)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



