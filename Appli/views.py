from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
from appli.models import Students

def home(request):
    students = Students.objects.all()
    return render(request, 'appli/base.html', {'students': students})

def list(request):
    students = Students.objects.all()
    return render(request, 'appli/list.html', {'students': students})

def detail(request, id):
    student = Students.objects.get(id=id)
    return render(request, 'appli/detail.html', {'student': student})

def marks(request, id):
    student = Students.objects.get(id=id)
    return render(request, 'appli/marks.html', {'student': student}) 