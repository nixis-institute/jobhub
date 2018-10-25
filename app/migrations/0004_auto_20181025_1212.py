# Generated by Django 2.1 on 2018-10-25 06:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_application',
            name='applied_date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.JOB_POSTING'),
        ),
    ]
