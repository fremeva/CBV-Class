# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import QuerySet

class UserQueryset(QuerySet):
    def get_only_superusers(self):
        return self.filter(is_superuser=True)

    def non_superuser(self):
        return self.filter(is_superuser=False)

class UserProxy(User):
    class Meta:
        # proxy = True
        abstract = True

    objects = UserQueryset.as_manager()


