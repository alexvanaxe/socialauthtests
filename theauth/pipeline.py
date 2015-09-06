from theauth.models import DefaultProfile


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        if kwargs.get('is_new'):
          DefaultProfile(user=user).save()