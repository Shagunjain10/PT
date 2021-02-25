# Generated by Django 3.1.7 on 2021-02-24 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Element', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mnemonics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mnemonics_hindi', models.CharField(blank=True, max_length=500, null=True)),
                ('mnemonics_english', models.CharField(blank=True, max_length=500, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mnemonics', to='Element.group')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mnemonics', to='Element.period')),
            ],
        ),
    ]
