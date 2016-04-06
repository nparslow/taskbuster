# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models

# Register your models here.

class ProjectsInLine(admin.TabularInline):
    # inherits from Tabular inline so Projects can appear as a table on the user page
    model = models.Project
    extra = 0

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    # display three columns, third will be from _projects function
    list_display = ("username", "interaction", "_projects")

    search_fields = ["user__username"]

    inlines = [
        ProjectsInLine
    ]

    def _projects(self, obj):
        # counts no. of projects for a particular profile, used in display
        return obj.projects.all().count()
