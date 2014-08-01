from django.db import models

# Create your models here.

class Article(models.Model):
    date = models.CharField(max_length=300)
    snippet = models.TextField()

    def __unicode__(self):
        return self.title



