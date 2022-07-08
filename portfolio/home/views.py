from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    # return HttpResponse('this is home or index page (/)')
    # contex = {'name':'Udoy', 'course':'Django'}

    return render(request, 'home.html')

def about(request):
    # return HttpResponse('this is about page (/about)')

    return render(request, 'about.html')

def project(request):
    # return HttpResponse('this is project page (/project)')

    return render(request, 'project.html')

def contact(request):
    # return HttpResponse('this is contact page (/contact)')

    if request.method=="POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        textarea = request.POST['textarea']

        # We print this print statments for check in colsole our data come or not
        # print(name, username, email, number, textarea)

        contact = Contact(name=name, username=username, email=email, number=number, textarea=textarea)
        contact.save()
        print('The data has been weitten to the db')

    return render(request, 'contact.html')