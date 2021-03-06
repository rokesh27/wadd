# Generated by Django 3.2.1 on 2021-05-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', upload_to='pictures')),
                ('name', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('card', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='virat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=7, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('Role', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
