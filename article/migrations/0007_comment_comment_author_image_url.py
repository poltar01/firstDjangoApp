# Generated by Django 3.1.6 on 2021-05-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20210501_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_author_image_url',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
