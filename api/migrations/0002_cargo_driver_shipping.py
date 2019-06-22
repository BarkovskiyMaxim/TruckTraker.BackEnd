# Generated by Django 2.2.1 on 2019-06-22 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('owner', models.CharField(max_length=128)),
                ('weight', models.PositiveIntegerField()),
                ('cargo_type', models.CharField(max_length=128)),
                ('danger', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('m', 'man'), ('f', 'female')], max_length=1)),
                ('birth_day', models.DateField()),
                ('foto', models.ImageField(max_length=128, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('destination', models.CharField(max_length=128)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('route', models.TextField(null=True)),
                ('cargo_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Cargo')),
                ('driver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Driver')),
                ('truck_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Truck')),
            ],
        ),
    ]
