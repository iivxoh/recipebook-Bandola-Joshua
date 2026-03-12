from django.shortcuts import render, redirect
from .forms import RecipeImageForm
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

@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if recipe.images.exists():
        return redirect("ledger:recipe_detail", pk)
    
    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.image_group = recipe
            image.save()
            return redirect("ledger:recipe_detail", pk)
    else:
        form = RecipeImageForm()
    
    ctx = {
        "form": form,
        "recipe": recipe
    }
    return render(request, "recipe_add_image.html", ctx)