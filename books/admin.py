from django.contrib import admin
from .models import Book, Bookshelf, Author, Language, Format, Subject
# Register your models here.
admin.site.register([Book, Bookshelf, Author, Language, Format, Subject])
