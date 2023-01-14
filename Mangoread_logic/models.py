from django.db import models


class Category(models.Model):
    name = models.CharField('тип', max_length=150)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Manga(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, verbose_name="тип", on_delete=models.CASCADE, null=True)
    year = models.PositiveSmallIntegerField("Год", default=2001)
    poster = models.ImageField("Постер", upload_to="manga/", blank=True, null=True)
    genre = models.ManyToManyField(Genre, verbose_name="Жанр")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манги"


class Review(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    text = models.TextField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0, choices=RATE_CHOICES)

    @property
    def manga_name(self):
        try:
            return self.manga.title
        except:
            return ''
