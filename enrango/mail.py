#
# mail.py
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
from django.core.mail import send_mail, BadHeaderError
#from enrango.models import Participant
import sys


def send_enrollment(participant):
    subject = 'Activation required for enrollment'
    message = 'To activate ' + participant.name + ' enrollment for ' + \
            participant.event.title + ' open the following link in your \
            browser of choice: ' + participant.event.get_absolute_url()
    from_email = ['lol']
    to_email = participant.email
    try:
        send_mail(subject, message, from_email, [to_email])
    except BadHeaderError:
        print "There is error in sputnik"
    except:
        print "ERROR IN SPJUTNJIK: ", sys.exc_info()[0]
    print "sputnik is ok"
