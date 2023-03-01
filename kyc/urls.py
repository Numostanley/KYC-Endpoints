from django.urls import path
from .views import UserRegister, UserDataAPI

urlpatterns = [
    path('register', UserRegister.as_view()),
    path('get-details', UserDataAPI.as_view()),
]
