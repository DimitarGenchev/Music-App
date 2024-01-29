from django.http import Http404

from ExamPrepDjango.musicapp.models import Album, Song


def check_if_object_belongs_to_user(obj, user):
    if isinstance(obj, Album):
        if obj.user != user:
            raise Http404("You do not have permission to view this page.")
    elif isinstance(obj, Song):
        if obj.album.user != user:
            raise Http404("You do not have permission to view this page.")

    return obj
