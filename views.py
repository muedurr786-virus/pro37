from django.shortcuts import render, redirect
from .models import *
from .forms import *


def Departmentpage(req):
    if req.method == "POST":
        form = DepartmentForm(req.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = DepartmentForm()

    dept = DepartmentModel.objects.all()
    con = {
        'form': form,
        'dept': dept
    }
    return render(req, 'Departmentpage.html', con)


def Departmenteditpage(req, id):
    dept = DepartmentModel.objects.get(id=id)
    if req.method == "POST":
        form = DepartmentForm(req.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('department')
    else:
        form = DepartmentForm(instance=dept)

    con = {
        'form': form,
        'dept': dept
    }
    return render(req, 'Departmenteditpage.html', con)


def Departmentdeletepage(req, id):
    DepartmentModel.objects.get(id=id).delete()
    return redirect('department')


def Techarpage(req):
    if req.method == "POST":
        form = TeacherForms(req.POST)
        if form.is_valid():
            form.save()      
    else:
        form = TeacherForms()

    dept = TecharModel.objects.all()
    con = {
        'form': form,
        'dept': dept
    }
    return render(req, 'Techarpage.html', con)


def Techareditpage(req, id):
    dept = TecharModel.objects.get(id=id)
    if req.method == "POST":
        form = TeacherForms(req.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:
        form = TeacherForms(instance=dept)

    con = {
        'form': form,
        'dept': dept
    }
    return render(req, 'Techareditpage.html', con)


def Techardeletpage(req, id):
    TecharModel.objects.get(id=id).delete()
    return redirect('teacher')



