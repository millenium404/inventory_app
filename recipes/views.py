from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.forms.models import modelformset_factory # model form for querysets
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm


@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {'object_list': qs}
    return render(request, 'recipes/list.html', context)


@login_required
def recipe_detail_view(request, id=None):
    hx_url = reverse('recipes:hx-detail', kwargs={'id': id})
    context = {'hx_url': hx_url}
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_detail_hx_view(request, id=None):
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        return HttpResponse('Not found.')
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {'object': obj}
    return render(request, 'recipes/partials/detail.html', context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create-update.html', context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    context = {'object': obj, 'form': form}

    if form.is_valid():
        form.save()
        context['message'] = 'Data saved.'

    if request.htmx:
        return render(request, 'recipes/partials/forms.html', context)
    return render(request, 'recipes/create-update.html', context)
