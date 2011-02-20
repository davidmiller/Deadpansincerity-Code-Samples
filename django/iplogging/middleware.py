"""
Middleware to store IP addresses.
"""


class IPMiddleware(object):
    """
    Get the user Id and the ip then pass to celery for processing.
    Only do it once per session though.
    """
    # pylint: disable-msg=R0201
    def process_request(self, request):
        """
        Check to see if we've logged the ip this session.

        If not, pass to celery for logging.

        Arguments:
        - `request`: HttpRequest
        """
        if not request.session.__contains__('logged_ip'):
            from django.contrib.auth.models import AnonymousUser
            from mycoolapp.logging.tasks import log_ip
            if request.user and not isinstance(request.user, AnonymousUser):
                if request.META.has_key('REMOTE_ADDR'):
                    log_ip.delay(request.user.pk, request.META['REMOTE_ADDR'])
                    request.session['logged_ip'] = True



