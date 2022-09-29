from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import CreateTask
from todolist.models import Task

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('todolist:show_todo')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Berhasil disimpan!")
            return redirect('todolist:show_todo')
    else:
        form = CreateTask(initial={'user': request.user})
    context = {'form': form}
    return render(request, 'create_task.html', context)


@login_required(login_url='/todolist/login/')
def change_status_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_finished = not(task.is_finished)
    task.save() 
    return redirect("todolist:show_todo")

@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    delete_task = Task.objects.get(id=pk)
    delete_task.delete() 
    return redirect("todolist:show_todo")

@login_required(login_url='/todolist/login/')
def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTask(instance=task)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:show_todo')
    context = {'form': form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def show_todo(request):
    task_list = Task.objects.all()
    user_todo_list = []
    current_user = request.user
    for task in task_list:
        if task.user == current_user:
            user_todo_list.append(task)
    context = {
        'task_list': task_list,
    }
    return render(request, 'todolist.html', context)