from django.utils import timezone
from blogs.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class Create_blog(CreateView):
    model = Blog
    success_url = "/blogs/pages"
    template_name = "blogs/create_blog.html"
    fields = ["title", "subtitle", "body", "author", "date", "image"]
""" 
    def form_valid(self, form):
    # Establece la fecha actual en el campo date_field antes de guardar el formulario
        form.instance.date_field = timezone.now().date()
        return super().form_valid(form) """

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