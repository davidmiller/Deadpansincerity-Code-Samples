from django.contrib.auth.models import User
from django.db import models


class IPAddress(models.Model):
    """
    An IPAddress that has logged in to mycoolapp.
    """
    ip_address = models.IPAddressField()
    known_location = models.CharField(max_length=300, blank=True, null=True)
    hostaddr = models.CharField(max_length=300, blank=True, null=True,
                                verbose_name="Reverse DNS")

    def __unicode__( self ):
        if self.known_location:
            return self.known_location
        if self.hostaddr:
            return "%s (%s)" % (self.hostaddr, self.ip_address)
        return self.ip_address

class UserIP(models.Model):
    """
    Store IP addresses a user has logged in from
    """
    user = models.ForeignKey(User)
    ip = models.ForeignKey(IPAddress)
    count = models.IntegerField(default=0)

    def __unicode__( self ):
        return "%s %s" % (self.user, self.ip)
