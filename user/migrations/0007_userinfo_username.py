# Generated by Django 3.1.6 on 2021-05-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210503_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Kullanıcı Adı'),
        ),
    ]