from django import forms
from .models import Album, Song
from django.contrib.auth.models import User


class Albumform(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_name', 'artist_name', 'album_genre', 'album_cover']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_name', 'song_audio']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

