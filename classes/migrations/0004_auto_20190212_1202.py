# Generated by Django 2.1.5 on 2019-02-12 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20190212_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom'),
        ),
    ]
