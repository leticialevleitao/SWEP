from swep import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.nome, name = 'index'),
    path('admin/', admin.site.urls),
    path('swep/', include('swep.urls')),
    path('alimentos/', views.alimentos, name = 'alimentos'),

]
