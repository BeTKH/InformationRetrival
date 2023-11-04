from django.contrib import admin
from .models import Document


"""
customize the admin UI for Documents

- create admin for document that inherits from admin
- pass it to the registration of the app in the 'admin.site.register()'


"""


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')


# Register your models here to access them via  the Admin UI
admin.site.register(Document, DocumentAdmin)
