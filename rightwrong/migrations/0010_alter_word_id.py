# Generated by Django 4.0.2 on 2022-03-04 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rightwrong', '0009_remove_word_pronunciation_alter_word_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
