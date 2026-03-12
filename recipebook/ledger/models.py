from django.db import models
from django.urls import reverse
from useraccounts.models import Profile


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:ingredient_detail", args=[str(self.id)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="recipes",
        null=True,
    )
    created_on = models.DateTimeField(null=True, auto_now_add=True)
    updated_on = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[str(self.id)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )

    def __str__(self):
        return "{} of {}".format(self.quantity, self.ingredient)


class RecipeImage(models.Model):
    recipe_image = models.ImageField(upload_to="images/", null=False)
    description = models.CharField(max_length=255)
    imageGroup = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return self.description
