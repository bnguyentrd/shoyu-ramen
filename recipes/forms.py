from django.forms import ModelForm
from recipes.models import Recipe, RecipeStep, Ingredient

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
            "stars",
        ]

class RecipeStepForm(ModelForm):
    class Meta:
        model = RecipeStep
        fields = [
            "step_number",
            "instruction",
            "recipe",
        ]

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "amount",
            "food_item",
            "recipe",
        ]
