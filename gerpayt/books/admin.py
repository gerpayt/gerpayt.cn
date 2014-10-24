from django.contrib import admin

from books.models import BookTag, BookItem

admin.site.register(BookItem)
admin.site.register(BookTag)
