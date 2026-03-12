from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "recipes.html", ctx)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        "name": recipe.name,
        "ingredients": recipe.ingredients.all(),
        "author": recipe.author.name,
        "images": recipe.images.all(),
    }
    return render(request, "recipe.html", ctx)
