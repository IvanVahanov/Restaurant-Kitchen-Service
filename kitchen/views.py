from django.shortcuts import render, get_object_or_404, redirect
from .models import Cook, Dish, DishType, Ingredient
from .forms import DishForm, DishTypeForm, IngredientForm


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish_list.html', {'dishes': dishes})


def cook_list(request):
    cooks = Cook.objects.all()
    return render(request, 'cook_list.html', {'cooks': cooks})


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'dish_detail.html', {'dish': dish})


def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = DishForm()
    return render(request, 'add_dish.html', {'form': form})
