from django.contrib.auth import models as auth_models, get_user_model
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint


class Profile(auth_models.AbstractUser):
    username = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                r'^[a-zA-Z0-9_]+$', 'Ensure this value contains only letters, numbers, and underscore.'
            ),
        ],
    )

    email = models.EmailField(
        unique=True,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        null=True,
        blank=True,
    )


UserModel = get_user_model()


class Album(models.Model):
    class GenreChoices(models.TextChoices):
        POP = 'Pop Music', 'Pop Music'
        JAZZ = 'Jazz Music', 'Jazz Music'
        RNB = 'R&B Music', 'R&B Music'
        ROCK = 'Rock Music', 'Rock Music'
        COUNTRY = 'Country Music', 'Country Music'
        DANCE = 'Dance Music', 'Dance Music'
        HIPHOP = 'Hip Hop Music', 'Hip Hop Music'
        OTHER = 'Other', 'Other'

    album_name = models.CharField(
        max_length=30,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(

    )

    price = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ],
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'album_name'],
                name='unique_album_name_per_user'
            )
        ]


