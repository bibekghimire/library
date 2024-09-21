
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Borrow
#Member, Borrow

from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseRedirect
#
from django.urls import reverse
# Create your views here.

#from .forms import BookForm, MemberForm, BorrowForm

def is_admin(user):
    return user.is_superuser
def is_staff(user):
    return user.is_staff



@login_required
def book_list(request):
    books=Book.objects.all()
    return render(request, 'book_list.html', {'books':books})


@login_required
def borrowed_books(request):
    usr=request.user
    borrows=Borrow.objects.filter(usr=usr)
    return render(request,'borrowed_list.html',{'borrows':borrows, 'user':usr})
