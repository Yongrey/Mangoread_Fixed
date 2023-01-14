from django.contrib import admin
from .models import Manga, Category, Genre, Review
# Register your models here.
admin.site.register(Manga)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
