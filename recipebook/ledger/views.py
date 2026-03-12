from django.shortcuts import render
from .models import Recipe, Profile
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    if (request.method == "POST"):
        r = Recipe()
        r.name = request.POST.get("recipe_name")
        r.author = Profile.objects.get(user=request.user)
        r.save()
        return render(request, "recipes.html", ctx)
    else:
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

@login_required
def recipe_forms(request):
    return render(request, "recipe_forms.html")