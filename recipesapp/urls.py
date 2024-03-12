from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='Главная'),
    path('register/', views.register, name='Регистрация'),
    path('login/', views.user_login, name='Профиль'),
    path('logout/', auth_views.LogoutView.as_view(), name='Выйти'),
    path('edit_profile/', views.edit_profile, name='Редактировать профиль'),
    path('search/', views.search_recipes, name='Поиск'),
    path('recipe/<int:recipe_id>', views.get_recipe, name='Рецепт №'),
    path('recipe/<slug:recipe_name>', views.get_recipe_by_name, name='Рецепты от автора'),
    path('add_recipe/', views.add_recipe, name='Добавить рецепт'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='Редактировать рецепт'),
    path('recipes/', views.get_recipes, name='Получить рецепт'),
    path('recipes/<str:user>/', views.get_recipes, name='Рецепты от пользователя'),
]
