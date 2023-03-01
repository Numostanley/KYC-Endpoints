from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserExistsError(Exception):
    pass

class User(AbstractUser):
    
    def __str__(self) -> str:
        return self.username
    
    @staticmethod
    def create_user(username: str, email: str, password: str, password2: str):
        if User.objects.filter(username=username).exists():
            raise UserExistsError({'message':'user with username already exists'})
        elif User.objects.filter(email=email).exists():
            raise UserExistsError({'message':'user with email already exists'})
        elif password != password2:
            raise UserExistsError({'message':'Password fields do not match.'})
        
        user = User.objects.create(
            username=username,
            email=email,
            is_active = True,
        )
        user.set_password(password)
        user.save()
        return user
     