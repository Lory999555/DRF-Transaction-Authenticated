from django.db import models
from users.models import User

class Transaction(models.Model):
    CURRENCY_CHOICES = [
        ('$', 'Dollar'),
        ('€', 'Euro')
    ]
    
    IN_OUT_CHOICES = [
        ('in', 'Income'),
        ('out', 'Expense')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES)
    in_out = models.CharField(max_length=3, choices=IN_OUT_CHOICES)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} - {self.date} - {self.amount} {self.currency}'
