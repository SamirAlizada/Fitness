from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, TrainerForm, MonthlyPricingForm, BarForm
from .models import Student, Trainer, Bar
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Add
def add_monthlypricing(request):
    if request.method == 'POST':
        form = MonthlyPricingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_monthlypricing') 
    else:
        form = MonthlyPricingForm()
    return render(request, 'add_monthlypricing.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student') 
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_trainer') 
    else:
        form = TrainerForm()
    return render(request, 'add_trainer.html', {'form': form})

def add_bar(request):
    if request.method == 'POST':
        form = BarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_bar') 
    else:
        form = BarForm()
    return render(request, 'add_bar.html', {'form': form})
# ----------------------------------------------------------------

#List of classes
def trainer_list(request):
    trainers = Trainer.objects.all()

    query = request.GET.get('q')
    if query:
        trainers = trainers.filter(full_name__icontains=query)

    return render(request, 'trainer_list.html', {'trainers': trainers})

def student_list(request):
    students = Student.objects.all()

    query = request.GET.get('q')
    if query:
        students = students.filter(full_name__icontains=query)

    return render(request, 'student_list.html', {'students': students})

def bar_list(request):
    bars = Bar.objects.all()

    query = request.GET.get('q')
    if query:
        bars = bars.filter(product_name__icontains=query)

    return render(request, 'bar_list.html', {'bars': bars})
# ----------------------------------------------------------------

# Update
def update_trainer(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    form = TrainerForm(instance=trainer)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_panel')
    return render(request, 'update_trainer.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_panel')
    return render(request, 'update_student.html', {'form': form})

def update_bar(request, pk):
    bar = get_object_or_404(Bar, pk=pk)
    form = BarForm(instance=bar)
    if request.method == 'POST':
        form = BarForm(request.POST, instance=bar)
        if form.is_valid():
            form.save()
            return redirect('bar_panel')
    return render(request, 'update_bar.html', {'form': form})
# ----------------------------------------------------------------

# Delete
def delete_trainer(request, pk):
    trainer = trainer.objects.get(pk=pk)
    trainer.delete()
    messages.success(request, 'Trainer deleted successfully.')
    return redirect('trainer_panel')

def delete_student(request, pk):
    student = student.objects.get(pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('student_panel')

def delete_bar(request, pk):
    bar = bar.objects.get(pk=pk)
    bar.delete()
    messages.success(request, 'Bar item deleted successfully.')
    return redirect('bar_panel')
# ----------------------------------------------------------------

# Panel
def trainer_panel(request):
    trainers = Trainer.objects.all()

    query = request.GET.get('q')
    if query:
        trainers = trainers.filter(full_name__icontains=query)

    return render(request, 'trainer_panel.html', {'trainers': trainers})

def student_panel(request):
    students = Student.objects.all()

    query = request.GET.get('q')
    if query:
        students = students.filter(full_name__icontains=query)

    return render(request, 'student_panel.html', {'students': students})

def bar_panel(request):
    bars = Bar.objects.all()

    query = request.GET.get('q')
    if query:
        bars = bars.filter(product_name__icontains=query)

    return render(request, 'bar_panel.html', {'bars': bars})
# ----------------------------------------------------------------

# User
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            messages.error(request, 'Username or password is incorrect.')
    return render(request, 'account/login.html')

def user_logout(request):
    logout(request)
    return redirect('student_list')

def about(request):
    return render(request, 'about.html')
# ----------------------------------------------------------------
