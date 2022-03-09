from django.shortcuts import render
from .models import Article

def article_search_view(request):
    query_dict = request.GET # This is a dictionary
    query = query_dict.get('q') # <input type="text" name="q">
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {'object': article_obj}
    print(query_dict, context)
    return render (request, 'articles/search.html', context=context)
