from django.urls import path
from blogs.views import create_blog, show_blogs

urlpatterns = [
    path('create_blog/', create_blog),
    path('show_blogs/', show_blogs),
    ]