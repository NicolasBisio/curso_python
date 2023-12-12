from django.shortcuts import render, redirect
from blogs.models import Blog
from blogs.forms import Create_Blog_Form, Blog_Form_Search

def create_blog(request):
    if request.method == "POST":
        
        blog = Create_Blog_Form(request.POST)
        if blog.is_valid():
            data = blog.cleaned_data
            new_blog = Blog(title = data["title"], 
                            subtitle = data["subtitle"], 
                            body = data["body"], 
                            author = data["author"], 
                            date = data["date"],
                            image = data["image"],)
            new_blog.save()
            return redirect("/blogs/show_blogs/")

    blog_form = Create_Blog_Form()
    context = {
        "form": blog_form
    }
    return render(request, "blogs/create_blog.html", context)

def show_blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
        "form": Blog_Form_Search(),
    }

    return render(request, 'blogs/show_blogs.html', context)