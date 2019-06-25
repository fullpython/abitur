from django.db import models
from django.db.models import F


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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['abitur','faculty'],
                name='abitur_unique'
            )
        ]