from django.urls import path
from blogs.views import create_blog, search_blogs, show_blogs

urlpatterns = [
    path('create_blog/', create_blog),
    path('show_blogs/', show_blogs),
    path('search_blogs/', search_blogs),
    ]