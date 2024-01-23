from django.urls import path, include

from ExamPrepDjango.musicapp import views

urlpatterns = [
    path('', views.UserRedirectView.as_view(), name='redirect user'),
    path('register/', views.UserRegisterView.as_view(), name='register profile'),
    path('login/', views.UserLoginView.as_view(), name='login profile'),
    path('logout/', views.UserLogoutView.as_view(), name='logout profile'),
    path('home/', views.AlbumsDisplayView.as_view(), name='index'),
    path('album/', include([
        path('add/', views.AlbumCreateView.as_view(), name='add album'),
        path('details/<int:id>/', include([
            path('', views.AlbumDetailsView.as_view(), name='details album'),
            path('songs/', views.AlbumSongsDisplayView.as_view(), name='album songs')
        ])),
        path('edit/<int:id>/', views.AlbumEditView.as_view(), name='edit album'),
        path('delete/<int:id>/', views.AlbumDeleteView.as_view(), name='delete album'),
    ])),
    path('profile/', include([
        path('details/', views.UserDetailsView.as_view(), name='details profile'),
        path('delete/', views.UserDeleteView.as_view(), name='delete profile'),
        path('edit/', views.UserEditView.as_view(), name='edit profile')
    ])),
    path('song/', include([
        path('add/', views.SongCreateView.as_view(), name='add song'),
        # path('edit/<int:id>/', views.SongEditView.as_view(), name='edit song'),
        path('delete/<int:id>/', views.SongDeleteView.as_view(), name='delete song'),
    ])),
]
