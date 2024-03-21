from django.shortcuts import render,redirect
from .models import Regmodel
def index(request):
    mem=Regmodel.objects.all()
    return render(request,'index.html',{'mem':mem})
def add(request):
    return render(request,'add.html')
def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Regmodel(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")
def delete(request,id):
    mem=Regmodel.objects.get(id=id)
    mem.delete()
    return redirect("/")
def update(request,id):
    mem=Regmodel.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})
def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Regmodel.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")