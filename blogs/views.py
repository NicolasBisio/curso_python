from blogs.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class Create_blog(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = "/blogs/pages"
    template_name = "blogs/create_blog.html"
    fields = ["title", "subtitle", "body", "author", "image"]

class Show_blogs(ListView):
    model = Blog
    template_name = "blogs/show_blogs.html"

class Blog_detail(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"

class Update_blog(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = "/blogs/pages"
    template_name = "blogs/update_blog.html"
    fields = ["title", "subtitle", "body", "author"]

class Delete_blog(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = "/blogs/pages"
    template_name = "blogs/delete_blog.html"