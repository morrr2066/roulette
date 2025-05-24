from django.urls import path
from . import views

app_name = 'roulette'

urlpatterns = [
    path('spin/', views.spin_result, name='spin_result'),
    path('', views.roulette_home, name='roulette'),
]
