# Generated by Django 2.2.6 on 2019-10-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]