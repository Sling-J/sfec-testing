# Generated by Django 2.1.2 on 2019-04-05 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0003_auto_20190405_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionRadio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('hint', models.CharField(max_length=200)),
                ('test', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Diplom.Test', verbose_name='questions')),
            ],
        ),
        migrations.CreateModel(
            name='VariantRadio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='Diplom.QuestionRadio')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='answer',
        ),
        migrations.AddField(
            model_name='student',
            name='answer_of_TEST4',
            field=models.ManyToManyField(blank=True, related_name='students', to='Diplom.VariantRadio'),
        ),
    ]
