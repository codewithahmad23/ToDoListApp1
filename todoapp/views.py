from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from .forms import RegisterForm



# Create your views here.
# Home logic
@login_required
def home(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'todoapp/home.html', {'tasks': tasks})


#def base(request):
 #   return render(request,'todoapp/base.html')


# Register page logic
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, 'todoapp/register.html', {'form': form})


# Login page logic
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user= authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'todoapp/login.html')
    return render(request, 'todoapp/login.html')




# Logout page logic
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")



def task_add(request):
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('home')
    else:
        form=TaskForm()
    return render (request,'todoapp/task_add.html',{'form':form})


def task_update(request,id):
    task=Task.objects.get(id=id,user=request.user)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TaskForm(instance=task)
    return render(request,'todoapp/task_update.html',{'form': form})


# Add task page logic
def task_delete(request,id=id):
    task=get_object_or_404(Task,id=id,user=request.user)
    task.delete()
    return redirect('home')
    