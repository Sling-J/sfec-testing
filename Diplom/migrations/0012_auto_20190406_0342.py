# Generated by Django 2.1.2 on 2019-04-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0011_auto_20190406_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='first_test_variants',
            name='owner',
        ),
        migrations.AddField(
            model_name='first_test_variants',
            name='owner',
            field=models.ManyToManyField(blank=True, related_name='first_test_answer', to='Diplom.Student'),
        ),
    ]
