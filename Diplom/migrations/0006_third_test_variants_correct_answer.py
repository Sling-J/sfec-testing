# Generated by Django 2.1.2 on 2019-04-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0005_first_test_variants_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='third_test_variants',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
