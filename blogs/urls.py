from django.urls import path
from blogs.views import search_blogs, Create_blog, Show_blogs, Blog_detail, Update_blog, Delete_blog

urlpatterns = [
    path('pages/', Show_blogs.as_view(), name = "show_blogs"),
    path('detail/<int:pk>', Blog_detail.as_view(), name="blog_detail"),
    path('create_blog/', Create_blog.as_view()),
    path('update/<int:pk>', Update_blog.as_view(), name="update_blog"),
    path('delete/<int:pk>', Delete_blog.as_view(), name="delete_blog"),
    ]