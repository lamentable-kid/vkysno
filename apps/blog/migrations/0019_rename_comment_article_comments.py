# Generated by Django 4.0.6 on 2022-10-08 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_article_comment_comment_article_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='comment',
            new_name='comments',
        ),
    ]