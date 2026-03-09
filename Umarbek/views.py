from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')

def contact(request):
    return render(request, 'contact.html')

def project_detail(request):
    return render(request, 'project-detail.html')