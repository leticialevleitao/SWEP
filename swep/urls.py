from django.urls import path
from . import views

urlpatterns = [
    path('nome/', views.nome)
]