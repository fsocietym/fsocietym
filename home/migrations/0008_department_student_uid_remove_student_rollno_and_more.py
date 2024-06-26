# Generated by Django 5.0.2 on 2024-04-15 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_recipemodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='Student_UID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
            ],
            options={
                'ordering': ['uid'],
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='rollNo',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.department'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_UID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student_uid'),
        ),
    ]
