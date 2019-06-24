from django.db import models

class University(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Faculty(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        null=True,blank=True,
        related_name='faculties_of_university'
    )
    name = models.CharField(max_length=150)
    code = models.IntegerField()
    def __str__(self):
        return self.name


