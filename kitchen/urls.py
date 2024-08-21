from django.urls import path
from . import views

app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    # Dish URLs
    path("dish/add/", views.add_dish, name="add_dish"),
    path("dish/<int:pk>/", views.dish_detail, name="dish_detail"),
    path("dish/<int:pk>/update/", views.update_dish, name="update_dish"),
    path("dish/<int:pk>/delete/", views.delete_dish, name="delete_dish"),
    # Dish Type URLs
    path("dish-type/", views.dish_type_list, name="dish_type_list"),
    path("dish-type/add/", views.add_dish_type, name="add_dish_type"),
    path("dish-type/<int:pk>/", views.dish_type_detail, name="dish_type_detail"),
    path("dish-type/<int:pk>/update/", views.update_dish_type, name="update_dish_type"),
    path("dish-type/<int:pk>/delete/", views.delete_dish_type, name="delete_dish_type"),
    # Cook URLs
    path("cook/", views.cook_list, name="cook_list"),
    path("cook/add/", views.add_cook, name="add_cook"),
    path("cook/<int:pk>/", views.cook_detail, name="cook_detail"),
    path("cook/<int:pk>/update/", views.update_cook, name="update_cook"),
    path("cook/<int:pk>/delete/", views.delete_cook, name="delete_cook"),
    # Ingredient URLs
    path("ingredient/", views.ingredient_list, name="ingredient_list"),
    path("ingredient/add/", views.add_ingredient, name="add_ingredient"),
    path("ingredient/<int:pk>/", views.ingredient_detail, name="ingredient_detail"),
    path("ingredient/<int:pk>/update/", views.update_ingredient, name="update_ingredient"),
    path("ingredient/<int:pk>/delete/", views.delete_ingredient, name="delete_ingredient"),
]
