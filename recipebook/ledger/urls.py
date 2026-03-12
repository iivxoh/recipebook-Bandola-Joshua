from django.urls import path
from .views import recipe_list, recipe_detail, recipe_forms

urlpatterns = [
    path("recipes/list/", recipe_list, name="recipe_list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe_detail"),
    path("recipe/add/", recipe_forms, name="recipe_forms"),
]

app_name = "ledger"
