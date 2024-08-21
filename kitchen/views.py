from django.shortcuts import render, get_object_or_404, redirect
from .models import Cook, Dish, DishType, Ingredient
from .forms import DishForm, DishTypeForm, IngredientForm, CookForm


def index(request):
    return render(request, 'kitchen/index.html')


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'kitchen/dish_list.html', {'dishes': dishes})


def cook_list(request):
    cooks = Cook.objects.all()
    return render(request, 'kitchen/cook_list.html', {'cooks': cooks})


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'kitchen/ingredient_list.html', {'ingredients': ingredients})


def dish_type_list(request):
    dish_types = DishType.objects.all()
    return render(request, 'kitchen/dish_type_list.html', {'dish_types': dish_types})


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'kitchen/dish_detail.html', {'dish': dish})


def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save()
            return redirect('kitchen:dish_detail', pk=dish.pk)
    else:
        form = DishForm()
    return render(request, 'kitchen/add_dish.html', {'form': form})


def update_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('kitchen:dish_detail', pk=dish.pk)
    else:
        form = DishForm(instance=dish)
    return render(request, 'kitchen/add_dish.html', {'form': form})


def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        dish.delete()
        return redirect('kitchen:index')
    return render(request, 'kitchen/dish_confirm_delete.html', {'dish': dish})


def add_cook(request):
    if request.method == "POST":
        form = CookForm(request.POST)
        if form.is_valid():
            cook = form.save()
            return redirect('kitchen:cook_detail', pk=cook.pk)
    else:
        form = CookForm()
    return render(request, 'kitchen/add_cook.html', {'form': form})


def cook_detail(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    return render(request, 'kitchen/cook_detail.html', {'cook': cook})


def update_cook(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    if request.method == "POST":
        form = CookForm(request.POST, instance=cook)
        if form.is_valid():
            form.save()
            return redirect('kitchen:cook_detail', pk=cook.pk)
    else:
        form = CookForm(instance=cook)
    return render(request, 'kitchen/add_cook.html', {'form': form})


def delete_cook(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    if request.method == "POST":
        cook.delete()
        return redirect('kitchen:index')
    return render(request, 'kitchen/cook_confirm_delete.html', {'cook': cook})


def add_ingredient(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save()
            return redirect('kitchen:ingredient_detail', pk=ingredient.pk)
    else:
        form = IngredientForm()
    return render(request, 'kitchen/add_ingredient.html', {'form': form})


def ingredient_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, 'kitchen/ingredient_detail.html', {'ingredient': ingredient})


def update_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('kitchen:ingredient_detail', pk=ingredient.pk)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'kitchen/add_ingredient.html', {'form': form})


def delete_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == "POST":
        ingredient.delete()
        return redirect('kitchen:index')
    return render(request, 'kitchen/ingredient_confirm_delete.html', {'ingredient': ingredient})


def add_dish_type(request):
    if request.method == "POST":
        form = DishTypeForm(request.POST)
        if form.is_valid():
            dish_type = form.save()
            return redirect('kitchen:dish_type_detail', pk=dish_type.pk)
    else:
        form = DishTypeForm()
    return render(request, 'kitchen/add_dish_type.html', {'form': form})


def dish_type_detail(request, pk):
    dish_type = get_object_or_404(DishType, pk=pk)
    return render(request, 'kitchen/dish_type_detail.html', {'dish_type': dish_type})


def update_dish_type(request, pk):
    dish_type = get_object_or_404(DishType, pk=pk)
    if request.method == "POST":
        form = DishTypeForm(request.POST, instance=dish_type)
        if form.is_valid():
            form.save()
            return redirect('kitchen:dish_type_detail', pk=dish_type.pk)
    else:
        form = DishTypeForm(instance=dish_type)
    return render(request, 'kitchen/add_dish_type.html', {'form': form})


def delete_dish_type(request, pk):
    dish_type = get_object_or_404(DishType, pk=pk)
    if request.method == "POST":
        dish_type.delete()
        return redirect('kitchen:index')
    return render(request, 'kitchen/dish_type_confirm_delete.html', {'dish_type': dish_type})

