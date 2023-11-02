from django.db import models

# Create your models here.


class Documents(models.Model):
    docID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title


class TermDocumentMatrix(models.Model):
    termID = models.AutoField(primary_key=True)
    docID = models.ForeignKey(Documents, on_delete=models.CASCADE)
    term = models.CharField(max_length=100)
    frequency = models.IntegerField()

    def __str__(self):
        return self.term
