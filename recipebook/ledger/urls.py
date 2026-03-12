from django.urls import path
from .views import recipe_list, recipe_detail, recipe_forms, recipe_add_image

urlpatterns = [
    path("recipes/list/", recipe_list, name="recipe_list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe_detail"),
    path("recipe/add/", recipe_forms, name="recipe_forms"),
    path("recipe/<int:pk>/add_image", recipe_add_image, name="recipe_image_upload"),
]

app_name = "ledger"
