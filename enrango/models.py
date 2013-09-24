from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Participant(models.Model):
    """
    Participants are currently required to leave this info. Should be fixed.

    Rationale: event producer needs to send bills using this info. By fixing I
    mean make it customizable, preferrably via the admin interface. TODO
    """
    name = models.CharField(max_length=settings.MAX_CHARFIELD_LENGTH)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=settings.MAX_CHARFIELD_LENGTH)

    def __unicode__(self):
        return self.name

    def check_phonenumber_length(self):
        """Norwegian phonenumbers are between 8 and 12 digits long

        Returns true if length is ok.
        TODO: do a more thorough/robust check.
        """
        if self.phone.length > 12 or self.phone < 8:
            raise ValidationError(u'%s does not look like a phonenumber \
                                  (Norwegian phonenumbers are between 8 and \
                                  12 digits).' % self.phone)
        return True

    phone.validators = [check_phonenumber_length]


class Event(models.Model):
    title = models.CharField(max_length=settings.MAX_CHARFIELD_LENGTH)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_event = models.DateTimeField(auto_now_add=False)
    #participants = models.ForeignKey(ParticipantList)

    def __unicode__(self):
        return self.title


class ParticipantList(models.Model):
    event = models.ForeignKey(Event)
    members = models.ForeignKey(Participant)
