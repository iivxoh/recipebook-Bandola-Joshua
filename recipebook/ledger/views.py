from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'recipes.html', ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        'name': recipe.name,
        'ingredients': recipe.ingredients.all(),
    }
    return render(request, 'recipe.html', ctx)
