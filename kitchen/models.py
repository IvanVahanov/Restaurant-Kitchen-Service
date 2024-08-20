from django.db import models
from django.contrib.auth.models import AbstractUser


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    def __str__(self):
        return self.name
