# Generated by Django 2.1.7 on 2020-03-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20200328_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='identity',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='student_class',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(choices=[('dep_one', '一大队'), ('dep_two', '二大队'), ('dep_three', '三大队'), ('dep_six', '六大队'), ('dep_seven', '七大队')], default='dep_two', max_length=50, verbose_name='部门'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='major',
            field=models.CharField(choices=[('jixie', '机械'), ('teshe', '特设'), ('hangdian', '航电'), ('junxie', '军械'), ('feican', '飞参')], default='jixie', max_length=50, verbose_name='专业'),
        ),
    ]