from django.urls import path
# import show_recipe from views
from recipes.views import show_recipe, show_recipe_list, recipe_list, create_recipe, edit_recipe, my_recipe_list

# "recipes" is the URL (localhost:8000/recipes)
# show_recipe is our view function name
urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/list.html", recipe_list, name="recipes_list"),
    path("recipes/detail.html", show_recipe),
    path("recipes/list.html", show_recipe),
    path("recipes/create/", create_recipe, name="create_recipe"),
    path("recipes/<int:id>/edit/", edit_recipe, name="edit_recipe"),
    path("mine/", my_recipe_list, name="my_recipe_list"),
]
