IP logging middleware for Django with Celery
=============================================

* Middleware checks for authenticated in users without a logged_ip session var
* Passes to celery to log ip
* celery tries to do a remote lookup on the hostname for nicer reporting
* turns socket.gethostbyaddr into an interruptible Thread to avoid pointless long running taskes due to general gethostbyaddr flaky-ness
* stores the ip address and increments the count against the user.
