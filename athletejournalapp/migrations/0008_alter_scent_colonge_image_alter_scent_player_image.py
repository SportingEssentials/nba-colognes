# Generated by Django 4.1.6 on 2023-06-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletejournalapp', '0007_alter_scent_colonge_image_alter_scent_player_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scent',
            name='colonge_image',
            field=models.ImageField(blank='True', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='scent',
            name='player_image',
            field=models.ImageField(blank='True', upload_to='media/'),
        ),
    ]