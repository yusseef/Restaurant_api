from django.urls import path
from .views import RestaurantView, DetailedRestaurantView

urlpatterns = [
    path('', RestaurantView.as_view(), name="All Restaurants"),
    path('<str:id>', DetailedRestaurantView.as_view(), name="Restaurant"),

]