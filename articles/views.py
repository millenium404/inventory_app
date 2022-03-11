from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

def article_search_view(request):
    query_dict = request.GET # This is a dictionary
    query = query_dict.get('q') # <input type="text" name="q">
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {'object': article_obj}
    print(query_dict, context)
    return render (request, 'articles/search.html', context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        article_obj = form.save()
        context['object'] = article_obj
        context['created'] = True
    return render(request, 'articles/create.html', context=context)
