from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
]
