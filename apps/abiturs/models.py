from django.db import models


class Abitur(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    passport_serial = models.CharField(max_length=9)
    passport_given_date = models.DateField()
    passport_expiry_date = models.DateField()
    passport_given_by = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'