# Generated by Django 4.0.6 on 2022-07-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_add_blog_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название тега'),
        ),
    ]