"""
View to authenticate static files
"""
from mimetypes import guess_type

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from mycoolapp.secrets.models import SecretDocument

@login_required
def can_u_haz(request, path):
    """
    Require login to serve some static media

    Arguments:
    - `request`: HttpRequest
    - `path`: str
    """
    # Your own authentication tests here
    if not request.user.is_superuser:
        return HttpResponseForbidden('No')
    url = "/ucanhaz/"+path
    response = HttpResponse()
    filename = split(path)[1]
    response['Content-Type'] = guess_type(filename)[0]
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response['X-Accel-Redirect'] = url
    return response
