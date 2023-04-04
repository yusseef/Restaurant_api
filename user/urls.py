from django.urls import path
from .views import UserView, DetailedUserView
urlpatterns = [
    path('', UserView.as_view(), name = 'users'),
    path('<str:id>', DetailedUserView.as_view(), name = 'user'),

]