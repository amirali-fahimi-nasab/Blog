# Generated by Django 4.1.1 on 2022-10-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_choices_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='choices_wishlist',
            field=models.CharField(choices=[('disliked', 0), ('liked', 1)], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
