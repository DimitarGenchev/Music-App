from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from ExamPrepDjango.musicapp.models import Album, Song
from ExamPrepDjango.musicapp.views import (UserRegisterView, UserLoginView, AlbumsDisplayView, AlbumCreateView,
                                           AlbumDetailsView)

User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.album = Album.objects.create(album_name='Test Album', artist='Test Artist', genre='Pop Music', price=9.99, user=self.user)
        self.song = Song.objects.create(title='Test Song', album=self.album)

    def test_user_register_view(self):
        url = reverse('register profile')
        request = self.factory.get(url)
        response = UserRegisterView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_user_login_view(self):
        url = reverse('login profile')
        request = self.factory.get(url)
        response = UserLoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_albums_display_view(self):
        url = reverse('index')
        request = self.factory.get(url)
        request.user = self.user
        response = AlbumsDisplayView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_album_create_view(self):
        url = reverse('add album')
        request = self.factory.get(url)
        request.user = self.user
        response = AlbumCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_album_details_view(self):
        url = reverse('details album', kwargs={'id': self.album.id})
        request = self.factory.get(url)
        request.user = self.user
        response = AlbumDetailsView.as_view()(request, id=self.album.id)
        self.assertEqual(response.status_code, 200)
