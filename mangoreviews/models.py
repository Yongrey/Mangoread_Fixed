from django.db import models
from mangocatalog.models import Manga

class Review(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    text = models.TextField(editable=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0, choices=RATE_CHOICES)
