# Generated by Django 2.0.5 on 2018-05-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Price', models.IntegerField(null=True)),
                ('HotorIce', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Price', models.IntegerField(null=True)),
                ('HotorIce', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mail', models.CharField(max_length=30, null=True)),
                ('Odate', models.DateField(blank=True, null=True)),
                ('Resdate', models.DateField(blank=True, null=True)),
                ('Restime', models.TimeField(blank=True, null=True)),
                ('Price', models.IntegerField(null=True)),
                ('Details', models.CharField(max_length=200)),
                ('Stats', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Price', models.IntegerField(null=True)),
                ('HotorIce', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Passwd', models.CharField(max_length=20, null=True)),
                ('Partname', models.CharField(max_length=1, null=True)),
                ('Username', models.CharField(max_length=10, null=True)),
                ('Phonenumber', models.CharField(max_length=20, null=True)),
                ('Bdate', models.DateField(blank=True, null=True)),
                ('isCaptain', models.BooleanField(default=False)),
                ('isAdmin', models.IntegerField(default=0)),
            ],
        ),
    ]
