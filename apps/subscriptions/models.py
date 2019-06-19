from django.db import models



class Subscription(models.Model):
    abitur = models.ForeignKey(
        'abiturs.Abitur',
        on_delete=models.CASCADE,
    )
    faculty = models.ForeignKey(
        'universities.Faculty',
        on_delete=models.CASCADE,
    )
    date_assigned = models.DateField()

    