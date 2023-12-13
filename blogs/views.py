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
                            date = data["date"],)
                            #image = data["image_URL"],)
            new_blog.save()
            return redirect("/blogs/show_blogs/")
        else:
            print(blog.errors)

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

def search_blogs(request):
    title = request.GET["title"]
    blogs = Blog.objects.filter(title__icontains=title)
    context = {
        "blogs": blogs,
        "form": Blog_Form_Search(),
    }
    return render(request, "blogs/show_blogs.html", context)