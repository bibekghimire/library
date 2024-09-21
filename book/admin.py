from django.contrib import admin
from .models import Book, Borrow

# Register your models here. 

# admin.site.register(Book)
# admin.site.register(Borrow)

#the following code enables search field in django administration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    autocomplete_fields = ['usr']
    search_fields = ['book__title', 'user__username']

#the above code enables search field in django administration