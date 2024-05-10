from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class MonthlyPricing(models.Model):
    name = models.CharField(max_length=30, null=True)
    month = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

class Trainer(models.Model):
    full_name = models.CharField(max_length=100)
    registration_date = models.DateField(default=timezone.now)
    monthly_fee = models.IntegerField()
    student_fee = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.full_name}"

class DailyPricing(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    registration_date = models.DateField(default=timezone.now)
    months_duration = models.ForeignKey(MonthlyPricing, on_delete=models.CASCADE, null=True, blank=True)
    daily = models.ForeignKey(DailyPricing, on_delete=models.CASCADE, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.IntegerField(default=0)
    end_date = models.DateField(null=True, blank=True)

    def calculate_payment(self):
        payment = 0.0  # Initially, the payment is reset

        if self.daily is not None:
            payment += self.daily.price  # Add the daily price

        if self.months_duration is not None:
            payment += self.months_duration.price  # Add the monthly price
            
            if self.trainer:
                payment += self.trainer.student_fee * self.months_duration.month
        
        # Update the payment in the `payment` variable
        self.payment = payment

    def calculate_end_date(self):
        # Calculation of end_date by adding months to months_duration on registration_date
        if self.months_duration:
            self.end_date = self.registration_date + relativedelta(months=self.months_duration.month)

    def save(self, *args, **kwargs):
        # Calculate the payment before saving
        self.calculate_payment()
        self.calculate_end_date()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.full_name}"

class Bar(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    stock_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product_name}"
    
class BarSold(models.Model):
    product_name = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    price = models.FloatField()
    count = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product_name}"