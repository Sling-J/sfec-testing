# Generated by Django 2.1.2 on 2019-04-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0008_numberquestion_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='seventh_test_variants',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
