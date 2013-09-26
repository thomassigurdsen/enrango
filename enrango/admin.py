#
# admin.py
#
# Copyright 2013 Thomas Sigurdsen <thomas.sigurdsen@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
from django.contrib import admin
from enrango.models import Event, Participant


class ParticipantInline(admin.TabularInline):
    model = Participant


class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('title', 'date_event', 'max_participants',),
                       'description',)
        }),)
    inlines = [ParticipantInline]
    list_display = ('title', 'max_participants', 'get_empty_seats',)
    list_filter = ['date_event']
    search_fields = ('title', 'description',)
    date_hierarchy = 'date_event'

admin.site.register(Event, EventAdmin)
