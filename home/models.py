from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create model for Expense
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Books', 'Books'),
        ('Travel', 'Travel'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
