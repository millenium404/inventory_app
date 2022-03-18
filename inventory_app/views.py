from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

html_string = '<h1>Hello World!</h1>'

def home_view(request):
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }
    return render(request, 'home-view.html', context)
