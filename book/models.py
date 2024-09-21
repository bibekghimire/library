from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta
from django.utils import timezone

# Create your models here.


def get_due_date():
    return timezone.now()+timedelta(days=45) 

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=13)
    total_copies=models.PositiveIntegerField(default=1)
    available_stock=models.PositiveIntegerField(default=total_copies)

    def __str__(self):
        return self.title 
    
class Borrow(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    usr=models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date=models.DateField(auto_now_add=True)
    due_date=models.DateField(default=get_due_date,editable=False)

    def save(self, *args, **kwargs):
        if not self.pk and self.book.available_stock > 0:
            self.book.available_stock-=1
            self.book.save()
            super().save(*args, **kwargs)
        elif self.pk:
            super().save(*args, **kwargs)
        else:
            raise ValueError('No copise of the book are availabel to borrow')
        
    def delete(self, *args, **kwargs):
        self.book.available_stock+=1
        self.book.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.usr.first_name} {self.usr.last_name} {self.borrow_date}"

