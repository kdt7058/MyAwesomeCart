from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogIndex, name="blog name"),
]
