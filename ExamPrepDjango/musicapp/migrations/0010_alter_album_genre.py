# Generated by Django 5.0 on 2024-01-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0009_alter_album_genre_alter_profile_age_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30),
        ),
    ]
