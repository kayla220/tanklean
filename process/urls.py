from django.urls import path
from process import views

urlpatterns = [
    path('', views.process, name='Process'),
]
