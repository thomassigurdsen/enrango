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
from enrango.models import Event, ParticipantForm, Participant
from django.utils import timezone
from django.template import RequestContext
from enrango.mail import send_enrollment
from enrango.utility import get_possessive


def index(request):
    future_events_list = Event.objects.filter(date_event__gt=timezone.now()).order_by('date_event')
    past_events_list = Event.objects.filter(date_event__lt=timezone.now()).order_by('date_event')
    return render_to_response('enrango/index.html', {
        'future_events_list': future_events_list,
        'past_events_list': past_events_list
    })


# If sending email fails I should redirect to a failure page; and NOT save
# to db...
def event(request, event_id):
    event_object = get_object_or_404(Event, pk=event_id)
    future_event = bool(event_object.date_event > timezone.now())
    part_form = ParticipantForm()
    if request.method == 'POST':
        part_form = ParticipantForm(request.POST)
        if part_form.is_valid():
            participant = part_form.save(commit=False)
            participant.event = event_object
            free_seats = event_object.get_empty_seats()
            participant.save()
            part_form = ParticipantForm()
            send_enrollment(participant)

    free_seats = event_object.get_empty_seats()
    if free_seats < 1:
        queue_length = abs(free_seats)
    else:
        queue_length = 0

    return render_to_response('enrango/event.html', {
        'event': event_object,
        'free_seats': free_seats,
        'queue_length': queue_length,
        'future_event': future_event,
        'participant_form': part_form,
    }, RequestContext(request))


def participant_details(request, event_id, part_identifier):
    # TODO: SECURITY: Have participants enter their name or similar,
    # TODO: SECURITY: to prevent false activations?)
    #
    # TODO: Also make sure of queueing and status correctness.
    participant = get_object_or_404(Participant, identifier=part_identifier)
    participant.update_status(activate=True)
    return render_to_response('enrango/participant_details.html', {
        'participant': participant,
        'participant_possessive': get_possessive(participant),
    },)
