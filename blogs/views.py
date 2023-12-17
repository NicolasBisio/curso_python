from blogs.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class Create_blog(CreateView):
    model = Blog
    success_url = "/blogs/pages"
    template_name = "blogs/create_blog.html"
    fields = ["title", "subtitle", "body", "author", "image"]

class Show_blogs(ListView):
    model = Blog
    template_name = "blogs/show_blogs.html"

class Blog_detail(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"

class Update_blog(UpdateView):
    model = Blog
    success_url = "/blogs/pages"
    template_name = "blogs/update_blog.html"
    fields = ["title", "subtitle", "body", "author", "date"]

class Delete_blog(DeleteView):
    model = Blog
    success_url = "/blogs/pages"
    template_name = "blogs/delete_blog.html"