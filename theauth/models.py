from django.contrib.auth.models import User, Group
from django.db import models


class DefaultProfile(models.Model):
    user = models.OneToOneField(User)

    def save(self, *args, **kwargs):
        self.user.groups.add(Group.objects.get_by_natural_key(name="default"))
        super(DefaultProfile, self).save(*args, **kwargs)