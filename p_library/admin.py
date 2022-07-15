from django.contrib import admin

# Register your models here.
from django.contrib import admin
from p_library.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     pass
