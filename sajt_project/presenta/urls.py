from django.urls import path
from presenta import views

urlpatterns = [
    path('', views.index, name='index'),
]
