from django.db import models
from django.utils import timezone

class MonthlyPricing(models.Model):
    month = models.IntegerField()
    price = models.IntegerField()

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
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.IntegerField(default=0)

    def calculate_payment(self):
        # Get the price if `months_duration` is selected
        if self.months_duration:
            payment = self.months_duration.price
        else:
            payment = 0.0

        # If a trainer is selected, add the trainer's student_fee
        if self.trainer:
            payment += self.trainer.student_fee

        # Update the `payment' field
        self.payment = payment

    def save(self, *args, **kwargs):
        # Calculate the payment before saving
        self.calculate_payment()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.full_name}"

class Bar(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    stock_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product_name}"