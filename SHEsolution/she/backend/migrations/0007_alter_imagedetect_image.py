# Generated by Django 4.1.4 on 2023-01-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0006_delete_history"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagedetect",
            name="image",
            field=models.ImageField(upload_to="yolov5/images"),
        ),
    ]
