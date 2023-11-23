from django.shortcuts import render, redirect

from todo_app import form
from todo_app.form import TodoForm
from todo_app.models import Todo


# Create your views here.
def test1(request):
    return render(request,'work.html')
def test2(request):
    return render(request,'index1.html')
def test3(request):
    return render(request,'indexdash1.html')

def create(request):

    form = TodoForm()
    if request.method == 'POST':
        data=TodoForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('page4')
    return render(request,"create.html",{'form':form})

def read(request):
    data = Todo.objects.all()
    return render(request,"read.html",{'data':data})

#delete

def delt(request,id):
    if request.method =="POST":

        data=Todo.objects.get(id=id)
        data.delete()
        return redirect('new4')

def update(request,id):
    todo=Todo.objects.get(id=id)
    form= TodoForm(instance=todo)
    if request.method == 'post':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('new5')

    return render(request,'update.html',{'form':form})