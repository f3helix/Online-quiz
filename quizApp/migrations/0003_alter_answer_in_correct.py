# Generated by Django 5.0.6 on 2024-07-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_rename_text_answer_text_answer_answer_in_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='in_correct',
            field=models.BooleanField(default=False),
        ),
    ]
