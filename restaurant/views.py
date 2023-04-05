from django.shortcuts import render
from rest_framework.views import APIView
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.


class RestaurantView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = RestaurantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetailedRestaurantView(APIView):
    def get_object(self, id):
        try:
            return Restaurant.objects.get(id = id)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, id):
        restaurant = self.get_object(id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id):
        restaurant = self.get_object(id)
        serializer = RestaurantSerializer(restaurant, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        restaurant = self.get_object(id)
        restaurant.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)