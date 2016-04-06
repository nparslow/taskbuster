# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# for django signals:
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import RegexValidator

from . import managers

# Create your models here.
# advised general order of elements of each model:
'''
class MyModel(models.Model):
    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    # Custom Properties
    # Methods
    # Meta and String
'''

# top model is profile, one-to-one with user
class Profile(models.Model):
    # Relations
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, # this imports the AUTH_USER_MODEL from settings.py
        related_name="profile", # by default this is the class name in lower case, but we make it explicit,
                                # it's used to access this model when it's a part of another (user here)
        verbose_name=_("user")  # a more readable version, note is with '_' so will be translated
    )

    # Attributes - Mandatory
    interaction = models.PositiveIntegerField(
        default=0,
        verbose_name=_("interaction")
    )

    # Attributes - Optional

    # Object Manager
    objects = managers.ProfileManager() # used for e.g. MyModel.objects.filter(...), here we define a custom one

    # Custom Properties (these are properties but will not have a row in the database table (unlike attributes))
    @property
    def username(self):
        return self.user.username

    # Methods

    # Meta and String
    class Meta:
        # user-friendly names of models
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ("user",) # default ordering for queries without 'order_by' specified

    def __str__(self):
        return self.user.username


# Django signal
# means a profile model will be made every time a user instance is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    # sender = the user model class
    # created = a boolean indicating if a new user has been created
    # instance = the user instance being saved
    if created:
        profile = Profile(user=instance)
        profile.save()

class Project(models.Model):
    # Relations
    user = models.ForeignKey(
        Profile, # foreign key relationship with profile model, means each Project must have a User Profile
        related_name="projects",
        verbose_name=_("user") # note we call a Profile "user", not "profile" ...
    )

    # Attributes - Mandatory
    name = models.CharField(
        max_length=100,
        verbose_name=_("name"),
        help_text=_("Enter the project name") # help_text will appear in model forms
    )
    color = models.CharField(
        max_length=7,
        default="#fff", # this is the same as #ffffff = white (note #000000 = black)
        validators=[RegexValidator(
            "(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)"
        )], # note hex colors with e.g. #001122 can be abbreviated as #012, We custom validate
        verbose_name=_("color"),
        help_text=_("Enter the hex color code, like #ccc or #cccccc")
    )

    # Attributes - Optional

    # Object Manager
    objects = managers.ProjectManager()

    # Custom Properties

    # Methods

    # Meta and String
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ("user", "name")
        unique_together = ("user", "name") # means for 1 profile (="user" see above), we can't have 2 projects of the same name

    def __str__(self):
        return "%s - %s" % (self.user, self.name)
