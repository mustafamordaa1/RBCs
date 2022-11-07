from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=1024)
    year = models.IntegerField()
    subject = models.CharField(max_length=128)
    doctor = models.CharField(max_length=128)
    lecture_num = models.IntegerField(default=1)
    part_num = models.IntegerField(default=None ,blank=True, null=True)
    link = models.URLField()
    version = models.IntegerField()

    def __str__(self):
        return self.title
