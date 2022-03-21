from django.contrib import admin
from django.urls import include, path
from .views import home_view
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('pantry/recipes/', include('recipes.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
