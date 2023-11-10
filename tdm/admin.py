from django.contrib import admin
from .models import Document

"""
customize the admin UI for TDM models

- create admin for document that inherits from admin
- pass it to the registration of the app in the 'admin.site.register()'


"""


# admin for the documents model in the tdm
class DocmentsAdmin(admin.ModelAdmin):
    list_display = ('docID', 'title', 'overview')


# register models to access via Admin UI
admin.site.register(Document, DocmentsAdmin)
