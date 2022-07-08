from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from blog.models import Contact

# Create your views here.

# ------------------------------------------------------

# Django Admn panel--
# username = udoy
# password = 11223344

# ------------------------------------------------------

def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}

    return render(request, 'bloghome.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}

    return render(request, 'blogpost.html', context)

def contact(request):
    if request.method == "POST":
        emailusername = request.POST.get('emailusername')
        password = request.POST.get('password')
        instance = Contact(emailusername=emailusername, password=password)
        instance.save()

    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')