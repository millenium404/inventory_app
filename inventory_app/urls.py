
from django.contrib import admin
from django.urls import path
from .views import home_view
from articles import views

urlpatterns = [
    path('', home_view, name='home'),
    path('articles/', views.article_search_view),
    path('admin/', admin.site.urls),
]
