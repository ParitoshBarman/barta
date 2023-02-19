# Generated by Django 4.1.3 on 2022-11-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantharooapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowDevice',
            fields=[
                ('slNo', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=122)),
                ('EmployeeID', models.IntegerField()),
                ('Email', models.CharField(max_length=122)),
                ('DesktopID', models.CharField(max_length=122)),
                ('IP_Address', models.CharField(max_length=100)),
                ('MainDateTime', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotAllow',
            fields=[
                ('slNo', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=122)),
                ('EmployeeID', models.IntegerField()),
                ('Email', models.CharField(max_length=122)),
                ('DesktopID', models.CharField(max_length=122)),
                ('IP_Address', models.CharField(max_length=100)),
                ('UserDateTime', models.CharField(max_length=100)),
                ('ServerDateTime', models.CharField(max_length=50)),
                ('MainDateTime', models.DateField(auto_now=True)),
            ],
        ),
    ]