from django.db import models
from django import forms
# Create your models here.
class Details(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_reg_no=models.IntegerField(primary_key=True)
    Shift=(("Morning","Morning"),("Night","Night"))
    shift_choice=models.CharField(max_length=10,choices=Shift)
    password=models.CharField(max_length=50,default='password')

    def __str__(self):
        return self.emp_name