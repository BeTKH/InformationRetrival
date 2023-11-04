from django.db import models


# Create your models here.


class Documents(models.Model):
    docID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='Unknown Title')
    content = models.TextField()
    overview = models.CharField(max_length=150, default='Unknown Title')

    def __str__(self):
        return self.title


class TermDocumentMatrix(models.Model):
    termID = models.AutoField(primary_key=True)

    # 1 to 1 relationship
    # docID = models.OneToOneField(Documents, on_delete=models.CASCADE)

    # 1 t * relationship
    docID = models.ForeignKey(Documents, on_delete=models.CASCADE)
    term = models.CharField(max_length=100)
    frequency = models.IntegerField()

    def __str__(self):
        return self.term
