# Generated by Django 2.1.7 on 2019-06-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/static/images/ad.jpg', upload_to=''),
        ),
    ]
