from django.urls import path
from .views import UserRegister, UserDataAPI, RegisterAPIView

urlpatterns = [
    path('register', UserRegister.as_view()),
    path('get-details', UserDataAPI.as_view()),
    path("register-users", RegisterAPIView.as_view())
]
