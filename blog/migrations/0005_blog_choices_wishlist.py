# Generated by Django 4.1.1 on 2022-10-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_disliked_remove_blog_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='choices_wishlist',
            field=models.CharField(choices=[('liked', 1), ('disliked', 0)], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
