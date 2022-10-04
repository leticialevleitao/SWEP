from swep import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import UsersViewSet, ReceitasViewSet, IndicacoesViewSet


router = routers.DefaultRouter()
router.register("user", UsersViewSet, basename="user")
router.register("receitas", ReceitasViewSet, basename="receitas")
router.register("indicacoes", IndicacoesViewSet, basename="indicacoes")


urlpatterns = [
    path("banco", include(router.urls), name = 'index'),
    path('', views.paginainicial, name = 'paginainicial'),
    path('admin/', admin.site.urls),
    path('alimentos/', views.alimentos, name = 'alimentos'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('receitas/', views.receitas, name = 'receitas'),
    path('indicacoesNutricionais/', views.indicacoes, name = 'indicacoesNutricionais'),

]