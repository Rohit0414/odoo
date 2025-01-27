from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True) 
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)


    def _str_(self):
        return self.title