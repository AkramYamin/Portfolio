from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blogs.html', {'blogs': blogs})


def details(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog': detail_blog})


def titled_url(request, slog):
    detail_blog = get_object_or_404(Blog, title=slog)
    return render(request, 'blogs/detail.html', {'blog': detail_blog})
