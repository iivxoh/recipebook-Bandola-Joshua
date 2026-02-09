from django.urls import path
from .views import recipes, recipe_one

urlpatterns = [
    path('recipes/list', recipes, name='recipes'),
    path('recipe/1', recipe_one, name='recipe_one')
]

app_name = "ledger"