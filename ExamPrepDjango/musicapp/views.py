from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from ExamPrepDjango.musicapp.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm, LoginForm
from ExamPrepDjango.musicapp.models import Album

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    form_class = ProfileCreateForm
    template_name = 'common/register.html'
    success_url = reverse_lazy('login profile')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'common/login.html'


class UserLogoutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    ...


class AlbumsDisplayView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'common/home.html'

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)


class AlbumCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = AlbumCreateForm
    template_name = 'album/add-album.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class AlbumDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Album
    template_name = 'album/album-details.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise Http404("You do not have permission to view this album.")

        return obj


class AlbumEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'album/edit-album.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise Http404("You do not have permission to edit this album.")

        return obj


class AlbumDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = 'album/delete-album.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'id'

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)

        return form_kwargs

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise Http404("You do not have permission to delete this album.")

        return obj


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'profile/profile-details.html'

    def get_object(self, *args, **kwargs):
        return self.request.user


class UserDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = UserModel
    form_class = ProfileDeleteForm
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('redirect user')

    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        
        return form_kwargs


class UserRedirectView(views.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('index')
        else:
            return reverse_lazy('register profile')


class UserEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = UserModel
    template_name = 'profile/profile-edit.html'
    fields = ['username', 'email', 'age', 'profile_picture']
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        return self.request.user
