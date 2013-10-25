#
# utility.py
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
""" This file contains short utility functions specific to enrango """
from django.conf import settings


def possessive(participant):
    """ returns ' or 's depending on the last character of participants name """
    if participant.name[len(participant.name) - 1] == 's':
        return u'\''

    return u'\'s'


def get_participant_url(participant):
    """ Returns a permanent url for the participant's details on event """
    return (settings.ENRANGO_FQDN +
            participant.event.get_absolute_url() +
            repr(participant.identifier) +
            u'/')
