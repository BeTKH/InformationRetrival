from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class TFIDF(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    term = models.CharField(max_length=100)
    tfidf_score = models.FloatField()
