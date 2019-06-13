from django.urls import path
from . import views
from .views import Viewall,Register

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('register/', Register.as_view(), name='blog-register'),
    path('viewall/', Viewall.as_view(), name='blog-view'),
]