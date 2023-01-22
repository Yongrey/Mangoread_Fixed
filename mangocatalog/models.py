from django.db import models
from mangoinfo.models import Category, Genre


class Manga(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, verbose_name="тип", on_delete=models.CASCADE, null=True)
    year = models.PositiveSmallIntegerField("Год", default=2001)
    poster = models.ImageField("Постер", upload_to="manga/", blank=True, null=True)
    genre = models.ManyToManyField(Genre, verbose_name="Жанр", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манги"