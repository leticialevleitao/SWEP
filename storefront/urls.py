from swep import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from be_drf.views import UsersViewSet, RecipesViewSet

router = routers.DefaultRouter()
router.register("user", UsersViewSet, basename="user")
router.register("recipe", RecipesViewSet, basename="recipe")


urlpatterns = [
    path("", include(router.urls), name = 'index'),
    path('admin/', admin.site.urls),
    path('swep/', include('swep.urls')),
    path('alimentos/', views.alimentos, name = 'alimentos'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),

]
