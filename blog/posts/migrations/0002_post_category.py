# Generated by Django 3.0.1 on 2019-12-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('drama', 'Drama'), ('action', 'Action')], default='drama', max_length=6),
        ),
    ]