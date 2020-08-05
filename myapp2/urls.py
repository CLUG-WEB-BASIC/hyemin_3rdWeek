
from django.urls import path
from . import views

urlpatterns = [
    path('', views.future, name ='future'),
    path('a/', views.a, name = 'a'),
]