from django.contrib import admin
from .models import Documents, TermDocumentMatrix

"""
customize the admin UI for TDM models

- create admin for document that inherits from admin
- pass it to the registration of the app in the 'admin.site.register()'


"""


# admin for the documents model in the tdm
class DocmentsAdmin(admin.ModelAdmin):
    list_display = ('docID', 'title', 'overview')


class tdmAdmin(admin.ModelAdmin):
    list_display = ('termID', 'docID', 'term', 'frequency')


# register models to access via Admin UI
admin.site.register(Documents, DocmentsAdmin)
admin.site.register(TermDocumentMatrix, tdmAdmin)
