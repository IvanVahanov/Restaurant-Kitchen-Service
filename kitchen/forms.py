from django import forms
from .models import Dish, DishType, Ingredient


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'dish_type', 'cooks', 'ingredients']


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
