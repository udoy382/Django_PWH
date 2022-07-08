from django.shortcuts import render
from django.http import HttpResponse
from home.models import Task
from home.models import Contact

# Create your views here.

# --------------------------------------------------------------
# Python Admin Panel 
'''
Username = SRUDOY
Email = srudoy436@gmail.com
Password = srudoy22
'''
# --------------------------------------------------------------

def home(request):
    context = {"success":False}
    if request.method == "POST":
        # Handle the form
        title = request.POST['title']
        description = request.POST['description']
        # print(title, description)
        ins = Task(title=title, description=description)
        ins.save()
        context = {"success":True}

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = Contact(name=name, username=username, email=email, password=password)
        contact.save()
    return render(request, 'contact.html')

def tasks(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.description)
    context = {'tasks':allTasks}
    return render(request, 'tasks.html', context)