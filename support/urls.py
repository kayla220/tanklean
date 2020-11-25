from django.urls import path
from support import views

urlpatterns = [
    path('', views.support, name='Support'),
]
