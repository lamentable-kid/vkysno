# Generated by Django 4.0.6 on 2022-08-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_tags_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]