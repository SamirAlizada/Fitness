from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, TrainerForm, MonthlyPricingForm, BarForm, BarSoldForm
from .models import Student, Trainer, Bar, MonthlyPricing, BarSold
from django.contrib import messages
from datetime import datetime, date, timedelta
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from dateutil.relativedelta import relativedelta

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

def add_bar_sold(request):
    if request.method == 'POST':
        form = BarSoldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_bar_sold') 
    else:
        form = BarSoldForm()
    return render(request, 'add_bar_sold.html', {'form': form})
# ----------------------------------------------------------------

#List of classes
def trainer_list(request):
    trainers = Trainer.objects.all()

    query = request.GET.get('q')
    if query:
        trainers = trainers.filter(full_name__icontains=query)

    return render(request, 'trainer_list.html', {'trainers': trainers})

# def student_list(request):
#     today = date.today()

#     # Retrieve the search query
#     query = request.GET.get('q')

#     # Get all students or filter based on the search query
#     students = Student.objects.all()
#     if query:
#         students = students.filter(full_name__icontains=query)

#     # Dictionary to group students by month
#     grouped_students_dict = {}

#     # Grouping students by month key and calculating monthly total payments
#     for student in students:
#         # Create month and year key from the registration date
#         month_key = student.registration_date.strftime('%Y-%m')
#         month_display = student.registration_date.strftime('%B %Y')

#         # Group by month key
#         if month_key not in grouped_students_dict:
#             grouped_students_dict[month_key] = {
#                 'display': month_display,
#                 'students': [],
#                 'total_payment': 0  # Track total monthly payments
#             }

#         # Add the student to the corresponding month's group
#         grouped_students_dict[month_key]['students'].append(student)

#         # Add the student's payment to the total payment for the month
#         grouped_students_dict[month_key]['total_payment'] += student.payment

#     # Convert dictionary to a list and sort by key in descending order
#     sorted_grouped_students_list = sorted(
#         grouped_students_dict.items(),
#         key=lambda x: x[0],
#         reverse=True
#     )

#     # Convert sorted list back to dictionary
#     sorted_grouped_students_dict = {
#         item[1]['display']: {
#             'students': item[1]['students'],
#             'total_payment': item[1]['total_payment']
#         }
#         for item in sorted_grouped_students_list
#     }

#     # Pass the data to the template
#     return render(request, 'student_list.html', {
#         'grouped_students': sorted_grouped_students_dict,
#         'today': today,
#     })

def student_list(request):
    today = date.today()
    
    # Retrieve the search query
    query = request.GET.get('q')
    
    # Get all students or filter based on the search query
    students = Student.objects.all()
    if query:
        students = students.filter(full_name__icontains=query)

    # Dictionary to group students by month
    grouped_students_dict = {}

    # Grouping students by month key and calculating monthly total payments
    for student in students:
        # Create month and year key from the registration date
        month_key = student.registration_date.strftime('%Y-%m')
        month_display = student.registration_date.strftime('%B %Y')

        # Group by month key
        if month_key not in grouped_students_dict:
            grouped_students_dict[month_key] = {
                'display': month_display,
                'students': [],
                'total_payment': 0  # Track total monthly payments
            }

        # Add the student to the corresponding month's group
        grouped_students_dict[month_key]['students'].append(student)

        # Add the student's payment to the total payment for the month
        grouped_students_dict[month_key]['total_payment'] += student.payment

    # Convert dictionary to a list and sort by key in descending order
    sorted_grouped_students_list = sorted(
        grouped_students_dict.items(),
        key=lambda x: x[0],
        reverse=True
    )

    # Convert sorted list back to dictionary
    sorted_grouped_students_dict = {
        item[1]['display']: {
            'students': item[1]['students'],
            'total_payment': item[1]['total_payment']
        }
        for item in sorted_grouped_students_list
    }

    # Filter students whose end_date is within one week from today
    students_near_end_date = students.filter(
        end_date__range=(today, today + timedelta(days=7))
    ).order_by('end_date')  # Sort by end_date in ascending order

    # Pass the data to the template
    return render(request, 'student_list.html', {
        'grouped_students': sorted_grouped_students_dict,
        'today': today,
        'students_near_end_date': students_near_end_date,
    })

def daily_student_list(request):
    now = datetime.now()
    today = now.date()

    students = Student.objects.filter(end_date=today)

    query = request.GET.get('q')
    if query:
        students = students.filter(full_name__icontains=query)

    return render(request, 'daily_student_list.html', {'students': students, 'today': today})

def bar_list(request):
    bars = Bar.objects.all()

    query = request.GET.get('q')
    if query:
        bars = bars.filter(product_name__icontains=query)

    return render(request, 'bar_list.html', {'bars': bars})

def bar_sold_list(request):
    today = date.today()

    # Retrieve the search query
    query = request.GET.get('q')

    # Get all bar_solds or filter based on the search query
    bar_solds = BarSold.objects.all()
    
    if query:
        bar_solds = bar_solds.filter(product_name__name__icontains=query)


    # Create a dictionary for grouping bar_solds by month
    grouped_bar_solds_dict = {}
    for bar_sold in bar_solds:
        # Extract month and year from `date`
        month_key = bar_sold.date.strftime('%Y-%m')
        month_display = bar_sold.date.strftime('%B %Y')

        # Calculate the sale amount for the bar_sold
        sale_amount = bar_sold.count * bar_sold.price

        # Group bar_solds by year-month key
        if month_key not in grouped_bar_solds_dict:
            grouped_bar_solds_dict[month_key] = {
                'display': month_display,
                'bar_solds': [],
                'total_sales': 0  # Initialize total monthly sales
            }

        # Add the bar_sold to the corresponding month's group
        grouped_bar_solds_dict[month_key]['bar_solds'].append(bar_sold)

        # Add the bar_sold's sale amount to the total sales for the month
        grouped_bar_solds_dict[month_key]['total_sales'] += sale_amount

    # Convert the dictionary to a list of tuples for sorting
    sorted_grouped_bar_solds_list = sorted(
        grouped_bar_solds_dict.items(),
        key=lambda x: x[0],
        reverse=True
    )

    # Convert the sorted list back to a dictionary
    sorted_grouped_bar_solds_dict = {
        item[1]['display']: {
            'bar_solds': item[1]['bar_solds'],
            'total_sales': item[1]['total_sales']
        }
        for item in sorted_grouped_bar_solds_list
    }

    # Pass the `grouped_bar_solds` data to the `bar_sold_list.html` template
    return render(request, 'bar_sold_list.html', {
        'grouped_bar_solds': sorted_grouped_bar_solds_dict,
        'today': today,
    })
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

def update_bar_sold(request, pk):
    bar_sold = get_object_or_404(BarSold, pk=pk)
    form = BarSoldForm(instance=bar_sold)
    if request.method == 'POST':
        form = BarSoldForm(request.POST, instance=bar_sold)
        if form.is_valid():
            form.save()
            return redirect('bar_sold_panel')
    return render(request, 'update_bar_sold.html', {'form': form})

def update_monthlypricing(request, pk):
    monthlypricing = get_object_or_404(MonthlyPricing, pk=pk)
    form = MonthlyPricingForm(instance=monthlypricing)
    if request.method == 'POST':
        form = MonthlyPricingForm(request.POST, instance=monthlypricing)
        if form.is_valid():
            form.save()
            return redirect('monthlypricing_panel')
    return render(request, 'update_monthlypricing.html', {'form': form})
# ----------------------------------------------------------------

# Delete
def delete_trainer(request, pk):
    trainer = Trainer.objects.get(pk=pk)
    trainer.delete()
    messages.success(request, 'Trainer deleted successfully.')
    return redirect('trainer_panel')

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('student_panel')

def delete_bar(request, pk):
    bar = Bar.objects.get(pk=pk)
    bar.delete()
    messages.success(request, 'Bar item deleted successfully.')
    return redirect('bar_panel')

def delete_bar_sold(request, pk):
    bar_sold = BarSold.objects.get(pk=pk)
    bar_sold.delete()
    messages.success(request, 'Bar item deleted successfully.')
    return redirect('bar_sold_panel')

def delete_monthlypricing(request, pk):
    monthlypricing = MonthlyPricing.objects.get(pk=pk)
    monthlypricing.delete()
    messages.success(request, 'Monthly Pricing deleted successfully.')
    return redirect('monthlypricing_panel')
# ----------------------------------------------------------------

# Panel
def trainer_panel(request):
    trainers = Trainer.objects.all()

    query = request.GET.get('q')
    if query:
        trainers = trainers.filter(full_name__icontains=query)

    return render(request, 'trainer_panel.html', {'trainers': trainers})

def student_panel(request):
    today = date.today()

    query = request.GET.get('q')

    students = Student.objects.all()

    if query:
        students = students.filter(full_name__icontains=query)

    # Create a dictionary for grouping students by month
    grouped_students_dict = {}
    for student in students:
        # Extract month and year from `registration_date`
        month_key = student.registration_date.strftime('%Y-%m')
        month_display = student.registration_date.strftime('%B %Y')
        # Group students by year-month key
        if month_key not in grouped_students_dict:
            grouped_students_dict[month_key] = {
                'display': month_display,
                'students': [],
                'total_payment': 0  # Track total monthly payments
            }
        
        # Add the student to the corresponding month's group
        grouped_students_dict[month_key]['students'].append(student)

        # Add the student's payment to the total payment for the month
        grouped_students_dict[month_key]['total_payment'] += student.payment

    # Convert the dictionary to a list of tuples for sorting
    sorted_grouped_students_list = sorted(
        grouped_students_dict.items(),
        key=lambda x: x[0],
        reverse=True
    )

    # Convert sorted list back to dictionary
    sorted_grouped_students_dict = {
        item[1]['display']: {
            'students': item[1]['students'],
            'total_payment': item[1]['total_payment']
        }
        for item in sorted_grouped_students_list
    }

    # Pass the `grouped_students` data to the `student_list.html` template
    return render(request, 'student_panel.html', {
        'grouped_students': sorted_grouped_students_dict,
        'today': today})

def bar_panel(request):
    bars = Bar.objects.all()

    query = request.GET.get('q')
    if query:
        bars = bars.filter(product_name__icontains=query)

    return render(request, 'bar_panel.html', {'bars': bars})

def bar_sold_panel(request):
    today = date.today()

    # Retrieve the search query
    query = request.GET.get('q')

    # Get all bar_solds or filter based on the search query
    bar_solds = BarSold.objects.all()

    if query:
        bar_solds = bar_solds.filter(product_name__icontains=query)

    # Create a dictionary for grouping bar_solds by month
    grouped_bar_solds_dict = {}
    for bar_sold in bar_solds:
        # Extract month and year from `date`
        month_key = bar_sold.date.strftime('%Y-%m')
        month_display = bar_sold.date.strftime('%B %Y')

        # Calculate the sale amount for the bar_sold
        sale_amount = bar_sold.count * bar_sold.price

        # Group bar_solds by year-month key
        if month_key not in grouped_bar_solds_dict:
            grouped_bar_solds_dict[month_key] = {
                'display': month_display,
                'bar_solds': [],
                'total_sales': 0  # Initialize total monthly sales
            }

        # Add the bar_sold to the corresponding month's group
        grouped_bar_solds_dict[month_key]['bar_solds'].append(bar_sold)

        # Add the bar_sold's sale amount to the total sales for the month
        grouped_bar_solds_dict[month_key]['total_sales'] += sale_amount

    # Convert the dictionary to a list of tuples for sorting
    sorted_grouped_bar_solds_list = sorted(
        grouped_bar_solds_dict.items(),
        key=lambda x: x[0],
        reverse=True
    )

    # Convert the sorted list back to a dictionary
    sorted_grouped_bar_solds_dict = {
        item[1]['display']: {
            'bar_solds': item[1]['bar_solds'],
            'total_sales': item[1]['total_sales']
        }
        for item in sorted_grouped_bar_solds_list
    }

    # Pass the `grouped_bar_solds` data to the `bar_sold_panel.html` template
    return render(request, 'bar_sold_panel.html', {
        'grouped_bar_solds': sorted_grouped_bar_solds_dict,
        'today': today,
    })

def monthlypricing_panel(request):
    monthlypricings = MonthlyPricing.objects.all().order_by('price')
    return render(request, 'monthlypricing_panel.html', {'monthlypricings': monthlypricings})
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

def renew_student(request, student_id):
    # Find the relevant student
    student = get_object_or_404(Student, id=student_id)
    
    # Set registration_date to the current date
    student.registration_date = timezone.now()
    
    # Update end_date by adding month above registration_date
    student.end_date = student.registration_date + relativedelta(months=student.months_duration.month)

    # Save changes
    student.save()

    # Redirect to an updated student related page or listing page
    return redirect('student_panel')

# ----------------------------------------------------------------

# Operations
def increase_stock(request, bar_id):
    bar = get_object_or_404(Bar, pk=bar_id)
    bar.stock_number += 1
    bar.save()
    return redirect('bar_panel')

def decrease_stock(request, bar_id):
    bar = get_object_or_404(Bar, pk=bar_id)
    # to check before reducing stock_number
    # you can add any stock control (for example, negative value prevention).
    if bar.stock_number > 0:
        bar.stock_number -= 1
        bar.save()
    return redirect('bar_panel')

def increase_sold(request, pk):
    bar_sold = get_object_or_404(BarSold, pk=pk)
    bar_sold.count += 1
    bar_sold.save()
    return redirect('bar_sold_panel')

def decrease_sold(request, pk):
    bar_sold = get_object_or_404(BarSold, pk=pk)
    # to check before reducing count
    # you can add any count control (for example, negative value prevention).
    if bar_sold.count > 0:
        bar_sold.count -= 1
        bar_sold.save()
    return redirect('bar_sold_panel')