from django import forms
from .models import RecipeImage

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["recipe_image", "description"]
