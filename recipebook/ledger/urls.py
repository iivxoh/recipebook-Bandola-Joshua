from django.urls import path
from .views import recipes, recipe_one, recipe_two

urlpatterns = [
    path('recipes/list', recipes, name='recipes'),
    path('recipe/1', recipe_one, name='recipe_one'),
    path('recipe/2', recipe_two, name='recipe_two')
]

app_name = "ledger"