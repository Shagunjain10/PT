# Generated by Django 3.1.5 on 2021-02-01 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Course', '0006_auto_20210202_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
