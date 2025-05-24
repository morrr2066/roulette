from django.urls import path
from . import views

app_name = 'roulette'

urlpatterns = [
    path('', views.home, name='home'),
    path('spin/', views.spin_result, name='spin_result'),
]
