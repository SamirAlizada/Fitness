from django.shortcuts import render, redirect
from .forms import StudentForm, TrainerForm, MonthlyPricingForm, BarForm
from .models import Student, Trainer, Bar

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

# def all_list(request):
#     category = request.GET.get('category')
#     if category == 'trainer':
#         data = trainer_list()
#     elif category == 'student':
#         data = student_list()
#     # elif category == 'bar':
#     #     data = bar_list()
#     else:
#         data = None 
#     return render(request, 'all_list.html', {'data': data})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def bar_list(request):
    bars = Bar.objects.all()
    return render(request, 'bar_list.html', {'bars': bars})