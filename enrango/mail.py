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
from django.conf import settings
from smtplib import SMTPConnectError, SMTPHeloError, SMTPAuthenticationError
import sys


def send_enrollment(participant):
    subject = 'Activation required for enrollment'
    message = 'To activate ' + participant.name + ' enrollment for ' + \
        participant.event.title + ' open the following link in your \
        browser of choice: ' + participant.event.get_absolute_url()
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = participant.email
    try:
        send_mail(subject, message, from_email, [to_email],
                  fail_silently=False)
    except BadHeaderError as e:
        print "Bad header found: ", e
    except SMTPConnectError as e:
        print "Connection error: ", e
    except SMTPHeloError as e:
        print "Helo error: ", e
    except SMTPAuthenticationError as e:
        print "Authentication error: ", e
    except:
        print "An error has occurred while trying to send mail: ", \
            sys.exc_info()
    print "I should now redirect to a thanks page or similar."
