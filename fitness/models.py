from django.db import models
from django.utils import timezone

class MonthlyPricing(models.Model):
    month = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.month}"

class Trainer(models.Model):
    full_name = models.CharField(max_length=100)
    registration_date = models.DateField(default=timezone.now)
    monthly_fee = models.IntegerField()
    student_fee = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.full_name}"

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    registration_date = models.DateField(default=timezone.now)
    months_duration = models.ForeignKey(MonthlyPricing, on_delete=models.CASCADE, null=True, blank=True)
    # months_duration = models.IntegerField(choices=[], default=1)
    # student_type = models.CharField(max_length=50, choices=[], default='only_gym')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.full_name}"

class Bar(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    stock_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product_name}"