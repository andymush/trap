from django.urls import path
from .import views


app_name = 'music'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout_user', views.logout_user, name='logout-user'),
    path('', views.index, name='index'),
    path('(?P<album_id>[0-9]+)/', views.detail, name='detail'),
    path('new-album', views.create_album, name='create_album'),
    path('<int:pk>/update-album', views.AlbumUpdateView.as_view(), name='album-update'),
    path('(?P<album_id>[0-9]+)/delete-album', views.album_delete, name='album-delete'),
    path('(?P<album_id>[0-9]+)/new-song', views.create_song, name='create-song'),
    path('<int:pk>/update-song', views.SongUpdateView.as_view(), name='song-update'),
    path('(?P<album_id>[0-9]+)/delete-song/(?P<song_id>[0-9]+)/', views.delete_song, name='song-delete'),
    path('(?P<album_id>[0-9]+)/favorite-album', views.favorite_album, name='album-favorite'),
    path('(?P<album_id>[0-9]+)/favorite-song/(?P<song_id>[0-9]+)', views.favorite_song, name='song-favorite'),
]
