from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "show_recipe": recipe,
    }
    return render(request, "recipes/detail.html", context)

def show_recipe_list(request):
    return render(request, "recipes/list.html")

# def show_recipe(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     context = {
#         "recipe_object": recipe,
#     }
#     return render(request, "recipes/detail.html", context)


def recipe_list(request):
    # Recipe.objects.all()
    # Recipe is the MODEL
    # .objects is data that we wanna grab
    # but the data has to look like model
    # dumbed down version: trying to find files of the same type
    # .all() is to grab all of it
    recipes = Recipe.objects.all()
    context = {
        "show_recipe": recipes,
    }
    return render(request, "recipes/list.html", context)


@login_required
def my_recipe_list(request):
    recipes = Recipe.objects.filter(author=request.user)
    context = {
        "show_recipe": recipes,
    }
    return render(request, "recipes/list.html", context)


@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    context = {
        "form": form,
    }
    return render(request, "recipes/create.html", context)

def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=id)
    else:
        form = RecipeForm(instance=recipe)
    context = {
        "recipe": recipe,
        "form": form,
    }
    return render(request, "recipes/edit.html", context)



# def redirect_to_recipe_list(request):
#     return redirect("recipe_list")



# def show_recipe_list(request):
#     dict = {}
#     for i in range(len(Recipe.objects.all())):
#         dict["recipe_object_"+str(i)] = Recipe.objects.all()[i]
#     context = dict
#     return render(request, "recipes/list.html", context)
