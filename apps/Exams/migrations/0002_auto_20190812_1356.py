# Generated by Django 2.0.2 on 2019-08-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperlist',
            name='judgment',
            field=models.IntegerField(default=0, verbose_name='判断题数'),
        ),
        migrations.AddField(
            model_name='paperlist',
            name='judgment_score',
            field=models.IntegerField(default=0, verbose_name='判断分值'),
        ),
        migrations.AddField(
            model_name='paperlist',
            name='multiple_choice_num',
            field=models.IntegerField(default=0, verbose_name='多选题数'),
        ),
        migrations.AddField(
            model_name='paperlist',
            name='multiple_choice_score',
            field=models.IntegerField(default=0, verbose_name='多选分值'),
        ),
        migrations.AddField(
            model_name='paperlist',
            name='single_choice_num',
            field=models.IntegerField(default=0, verbose_name='单选题数'),
        ),
        migrations.AddField(
            model_name='paperlist',
            name='single_choice_score',
            field=models.IntegerField(default=0, verbose_name='单选分值'),
        ),
    ]