from django import forms
from .models import Student, Trainer, MonthlyPricing, Bar, BarSold

class MonthlyPricingForm(forms.ModelForm):
    class Meta:
        model = MonthlyPricing
        fields = ['month', 'price']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'registration_date', 'months_duration', 'trainer']

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['full_name', 'registration_date', 'monthly_fee', 'student_fee']

class BarForm(forms.ModelForm):
    class Meta:
        model = Bar
        fields = ['product_name', 'price', 'stock_number']

class BarSoldForm(forms.ModelForm):
    class Meta:
        model = BarSold
        fields = ['product_name', 'price', 'count']