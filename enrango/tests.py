#
# tests.py
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
import unittest
#from django.test import TestCase
from enrango.models import Participant, Event
from enrango.utility import get_possessive  # , get_participant_url


class GetPossessiveTest(unittest.TestCase):
    def setUp(self):
        self.event = Event.objects.create(title='Some Event',
                                          description='Event description',
                                          date_event='2020-06-06',
                                          max_participants=3)
        self.part_sss = Participant.objects.create(name='sss',
                                                   phone=12345678,
                                                   email='sss@localhost.com',
                                                   address='teststreet 3',
                                                   event=self.event)
        self.part_nnn = Participant.objects.create(name='nnn',
                                                   phone=87654321,
                                                   email='nnn@localhost.com',
                                                   address='teststreet 4',
                                                   event=self.event)

    def runTest(self):
        self.assertEqual(get_possessive(self.part_sss), u'\'')
        self.assertEqual(get_possessive(self.part_nnn), u'\'s')
