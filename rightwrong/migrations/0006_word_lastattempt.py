# Generated by Django 4.0.2 on 2022-02-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rightwrong', '0005_remove_word_lastattempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='lastAttempt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]