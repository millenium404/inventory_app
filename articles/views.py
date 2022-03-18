from django.shortcuts import render
from django.http import Http404
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.db.models import Q

def article_search_view(request):
    query_dict = request.GET # This is a dictionary
    query = query_dict.get('q') # <input type="text" name="q">
    qs = Article.objects.search(query=query)
    context = {'object_list': qs}
    return render (request, 'articles/search.html', context)

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

def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
            context ={'object': article_obj}
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    return render(request, 'articles/detail.html', context)
