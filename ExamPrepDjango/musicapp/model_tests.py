from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Album, Song


class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        user_model = get_user_model()
        profile = user_model.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.assertEqual(profile.username, 'testuser')
        self.assertEqual(profile.email, 'test@example.com')
        self.assertIsNone(profile.age)


class AlbumModelTest(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_album_creation(self):
        album = Album.objects.create(
            album_name='Test Album',
            artist='Test Artist',
            genre=Album.GenreChoices.POP,
            description='This is a test album',
            image_url='http://example.com/image.jpg',
            price=9.99,
            user=self.user
        )
        self.assertEqual(album.album_name, 'Test Album')
        self.assertEqual(album.artist, 'Test Artist')
        self.assertEqual(album.genre, Album.GenreChoices.POP)
        self.assertEqual(album.description, 'This is a test album')
        self.assertEqual(album.image_url, 'http://example.com/image.jpg')
        self.assertEqual(album.price, 9.99)
        self.assertEqual(album.user, self.user)

    def test_unique_album_name_per_user(self):
        Album.objects.create(
            album_name='Test Album',
            artist='Test Artist',
            genre=Album.GenreChoices.POP,
            description='This is a test album',
            image_url='http://example.com/image.jpg',
            price=9.99,
            user=self.user
        )
        # Attempt to create another album with the same name and user
        with self.assertRaises(Exception):
            Album.objects.create(
                album_name='Test Album',
                artist='Test Artist',
                genre=Album.GenreChoices.POP,
                description='This is a test album',
                image_url='http://example.com/image.jpg',
                price=9.99,
                user=self.user
            )


class SongModelTest(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.album = Album.objects.create(
            album_name='Test Album',
            artist='Test Artist',
            genre=Album.GenreChoices.POP,
            description='This is a test album',
            image_url='http://example.com/image.jpg',
            price=9.99,
            user=self.user
        )

    def test_song_creation(self):
        song = Song.objects.create(
            title='Test Song',
            music_file='path/to/music.mp3',
            album=self.album
        )
        self.assertEqual(song.title, 'Test Song')
        self.assertEqual(song.music_file, 'path/to/music.mp3')
        self.assertEqual(song.album, self.album)

