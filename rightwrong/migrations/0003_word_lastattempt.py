# Generated by Django 4.0.2 on 2022-02-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rightwrong', '0002_word_numofattempts_word_numofcorrect'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='lastAttempt',
            field=models.DateField(auto_now=True),
        ),
    ]
