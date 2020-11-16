from django.urls import path
from tankcleaning import views

urlpatterns = [
    path('', views.tankcleaning, name='TankCleaning'),
]
