# Generated by Django 2.1.2 on 2019-04-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0007_variantradio_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberquestion',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
