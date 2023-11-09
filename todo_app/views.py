from django.shortcuts import render

from todo_app import form
from todo_app.form import TodoForm


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
    return render(request,"indexdash1.html",{'form':form})

