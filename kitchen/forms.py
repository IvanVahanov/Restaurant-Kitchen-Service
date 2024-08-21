from django import forms
from .models import Dish, DishType, Ingredient, Cook


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


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["username", "email", "password", "first_name", "last_name", "years_of_experience"]
        widgets = {
            'password': forms.PasswordInput(),
        }