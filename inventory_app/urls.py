
from django.contrib import admin
from django.urls import path
from .views import home_view
from articles.views import article_search_view, article_create_view
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('articles/', article_search_view),
    path('articles/create/', article_create_view),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
