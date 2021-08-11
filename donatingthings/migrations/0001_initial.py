# Generated by Django 3.2.1 on 2021-05-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='regformdthings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('u', 'other')], max_length=1, null=True)),
                ('age', models.IntegerField()),
                ('pnumber', models.BigIntegerField()),
                ('ntoys', models.CharField(max_length=50)),
                ('nbooks', models.CharField(max_length=50)),
                ('nblankets', models.CharField(max_length=50)),
                ('dress', models.CharField(max_length=50)),
                ('cgender', models.CharField(choices=[('M', 'boy'), ('F', 'girl')], max_length=1, null=True)),
                ('others', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=5000)),
                ('landmark', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
    ]