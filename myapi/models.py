from django.db import models
from django.db.models.fields import BooleanField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField(blank=True)
    photo=models.URLField(blank=True)
    location = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    user_id=models.CharField(max_length=45)
    content = models.CharField(max_length=50)
    Stock_code =models.CharField(max_length=20)

class User_login(models.Model): #登入與註冊
    user_id=models.CharField(max_length=45)
    Stock_code =models.CharField(max_length=20)
    content = models.CharField(max_length=50)
