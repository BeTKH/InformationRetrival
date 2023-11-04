from django.db import models
from django.utils import timezone

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=500, default='Unknown Title')
    content = models.TextField()
    author = models.CharField(max_length=100, default='Unknown Author')

    # show the name of the document instead of displaaying 	"Document object (1)""

    def __str__(self) -> str:
        return self.title
