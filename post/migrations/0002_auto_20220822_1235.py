# Generated by Django 3.2.14 on 2022-08-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='ip',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mypost',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='uploaded_files/'),
        ),
    ]
