# Generated by Django 4.0.6 on 2022-07-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalIdHolders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('district', models.CharField(blank=True, max_length=150, null=True)),
                ('birthday', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, max_length=150, null=True)),
                ('civil_status', models.CharField(blank=True, max_length=150, null=True)),
                ('is_vaccinated', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='districts',
            options={'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterField(
            model_name='districts',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='District Name'),
        ),
    ]