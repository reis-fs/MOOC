# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)
