from django.urls import path
from . import views

urlpatterns = [
    path('sayHello/' , views.sayHello)
]