from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name