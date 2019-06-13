from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Post(models.Model):
	name = models.CharField(max_length=20)
	email=models.EmailField()
	phone=PhoneNumberField()
	video=models.FileField(upload_to='videos/')
	image=models.ImageField(upload_to='covers/')


