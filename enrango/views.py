#
# views.py
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
from django.shortcuts import render_to_response, get_object_or_404
from enrango.models import Event
from datetime import datetime


def index(request):
    future_events_list = Event.objects.filter(date_event__gt=datetime.now()).order_by('date_event')
    past_events_list = Event.objects.filter(date_event__lt=datetime.now()).order_by('date_event')
    return render_to_response('enrango/index.html', {
        'future_events_list':
        future_events_list,
        'past_events_list':
        past_events_list
    })


def event(request, event_id):
    event_object = get_object_or_404(Event, pk=event_id)
    free_seats = Event.objects.get(pk=event_id).get_empty_seats()
    if free_seats < 1:
        queue_length = abs(free_seats)
    else:
        queue_length = 0

    return render_to_response('enrango/event.html', {
        'event': event_object,
        'free_seats': free_seats,
        'queue_length': queue_length,
    })


def register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return HttpResponseRedirect(reverse('event', args=(event.id,)))
