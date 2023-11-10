from django.db import models


# Create your models here.


class Document(models.Model):
    docID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='Unknown Title')
    content = models.TextField()
    overview = models.CharField(max_length=150, default='Unknown Title')

    def __str__(self):
        return self.title
