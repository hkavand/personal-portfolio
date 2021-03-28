from django.shortcuts import render
from .models import Project
from .models import About

def home(request):
    abouts = About.objects.all()
    return render(request,'portfolio/home.html',{'id':0,'abouts':abouts})


def projects(request):
    projects = Project.objects.all().order_by('-id')
    return render(request,'portfolio/projects.html',{'projects':projects,'id':2})


def contact(request):
    return render(request,'portfolio/contact.html',{'id':3})