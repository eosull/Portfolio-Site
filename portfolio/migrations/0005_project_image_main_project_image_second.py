# Generated by Django 4.2.2 on 2024-01-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_body_text_project_body_text_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_main',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_second',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]