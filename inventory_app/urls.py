from django.contrib import admin
from django.urls import path
from .views import home_view
from articles.views import article_search_view, article_create_view, article_detail_view
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('articles/', article_search_view, name='articles'),
    path('articles/create/', article_create_view, name='article-create'),
    path('articles/<slug:slug>/', article_detail_view, name='article-detail'),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
