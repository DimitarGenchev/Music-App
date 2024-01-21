from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from ExamPrepDjango.musicapp.models import Profile, Album

UserModel = get_user_model()


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                    'id': 'username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'id': 'email',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                    'id': 'age',
                }
            ),
        }


class ProfileCreateForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                    'id': 'username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'id': 'email',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                    'id': 'password1'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': 'Confirm Password',
                    'id': 'password2'
                }
            ),
        }


class ProfileDeleteForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['user']
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                    'id': 'name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                    'id': 'artist',
                }
            ),
            'genre': forms.Select(
                attrs={
                    'id': 'genre',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'id': 'description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                    'id': 'imgURL',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                    'id': 'price',
                }
            ),
        }


class AlbumCreateForm(AlbumBaseForm):
    ...


class AlbumEditForm(AlbumBaseForm):
    ...


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['genre'].widget = forms.TextInput(
            attrs={
                'id': 'genre',
            }
        )

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
            }
        ),
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password',
            }
        ),
    )
