"""
Store an IP address against a user.
"""
import socket
import threading

from celery.decorators import task

from django.contrib.auth.models import User
from myapp.logging.models import IPAddress, UserIP

class InterruptableThread(threading.Thread):
    """
    Call a function that we can timeout
    """
    # pylint: disable-msg=W0102
    def __init__(self, func, args=(), kwargs={}):
        """
        Establish the thread

        Arguments:
        - `func`: function
        - `args`: args for func
        - `kwargs`: kwargs for func
        """
        self.func = func
        self.args = args
        self.kwargs = kwargs
        threading.Thread.__init__(self)
        self.result = None

    def run(self):
        """
        Call, passing along args
        """
        self.result = self.func(*self.args, **self.kwargs)


@task
def log_ip(user_id, ip_address):
    """
    Log a user's IP address.

    Arguments:
    - `user_id`: str
    - `ip_address`: str

    """
    try:
        # pylint: disable-msg=E1101
        user = User.objects.get(pk=user_id)
        ip_addr = IPAddress.objects.get_or_create(ip_address=ip_address)[0]
        if not ip_addr.hostaddr:
            try:
                host_thread = InterruptableThread(socket.gethostbyaddr,
                                                  args=tuple([ip_address]))
                host_thread.start()
                host_thread.join(5)
                if host_thread.isAlive():
                    host = host_thread.result
                else:
                    host = host_thread.result
                if host:
                    ip_addr.hostaddr = host[0]
                    ip_addr.save()
            except socket.gaierror:
                pass
            user_ip = UserIP.objects.get_or_create(user=user, ip=ip_addr)[0]
            user_ip.count += 1
            user_ip.save()
    except User.DoesNotExist:
        pass
    return False
