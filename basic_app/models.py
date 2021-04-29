from django.db import models


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveBigIntegerField()
    school = models.ForeignKey(
        School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
