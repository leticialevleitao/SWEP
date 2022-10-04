from swep import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from be_drf.views import UsersViewSet, RecipesViewSet, IndicacoesViewSet


router = routers.DefaultRouter()
router.register("user", UsersViewSet, basename="user")
router.register("recipe", RecipesViewSet, basename="recipe")
router.register("indicacoes", IndicacoesViewSet, basename="indicacoes")


urlpatterns = [
    path("banco", include(router.urls), name = 'index'),
    path('', views.paginainicial, name = 'paginainicial'),
    path('admin/', admin.site.urls),
    path('alimentos/', views.alimentos, name = 'alimentos'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('indicacoesNutricionais/', views.indicacoes, name = 'indicacoesNutricionais'),

]
