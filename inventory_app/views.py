from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

html_string = '<h1>Hello World!</h1>'

def home_view(request):
    objects = Article.objects.all()

    context = {
        'objects': objects,
    }
    return render(request, 'home-view.html', context)
