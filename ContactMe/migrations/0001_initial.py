# Generated by Django 3.1.4 on 2020-12-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=100)),
                ('Full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('received_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
