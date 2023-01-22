# Generated by Django 4.1.5 on 2023-01-17 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mangoinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('year', models.PositiveSmallIntegerField(default=2001, verbose_name='Год')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='manga/', verbose_name='Постер')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mangoinfo.category', verbose_name='тип')),
                ('genre', models.ManyToManyField(blank=True, null=True, to='mangoinfo.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манги',
            },
        ),
    ]