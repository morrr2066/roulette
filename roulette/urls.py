from django.urls import path
from . import views

app_name = 'roulette'

urlpatterns = [
    path('', views.roulette_home, name='roulette_home'),
    path('spin/', views.spin_result, name='spin_result'),
]
