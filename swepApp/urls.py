from django.contrib import admin
from django.urls import path
from .views import *

#Incluir aqui as urls das novas páginas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='index'),
    path('register/', RegisterView, name='register'),
]
