# Generated by Django 3.1.4 on 2021-01-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210102_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_file',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
