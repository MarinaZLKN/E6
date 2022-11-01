from django.urls import path
from . import views

urlpatterns= [
    path('auth', views.auth, name='auth'),
    path('registration', views.registration, name='registration'),
    path('', views.index, name='main')
]