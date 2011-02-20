"""
Urlconf for the sake of completeness
"""
from django.conf.urls.defaults import (patterns, include, handler404,
                                       handler500)
urlpatterns = patterns(
    '',
    (r'^icanhaz/(?P<path>.*)$', 'mycoolapp.views.can_u_haz' ),
    )
