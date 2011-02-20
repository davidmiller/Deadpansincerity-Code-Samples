"""
Let's have a management command to profile our tests
"""
from django.core.management.base import BaseCommand
from django.test.simple import run_tests
try:
    import cProfile as profile
except ImportError:
    import profile
try:
    import pstats
except ImportError, e:
    import platform
    distro = platform.dist()
    if distro[0] == 'Ubuntu':
        import sys
        print "Looks like you're running Ubuntu."
        print "Debian have some licencing issues with some of Python's stdlib."
        print "As a result, you will have to apt-get install python-profiler"
        print "Unless you're using virtualenv/buildout. in which case try here:"
        print "code.python.org/hg/branches/release2.6-maint/file/8afc6adeab86/\
Lib/pstats.py"
    else:
        raise e
    sys.exit()

def profile_tests(*args, **kwargs):
    "Run tests with the profiler"
    profile.runctx('run_tests(*args, **kwargs)',
                {'run_tests':run_tests,'args':args,'kwargs':kwargs},
                {}, None )

class Command(BaseCommand):
    """
    We totally want to get profiled
    """
    option_list = BaseCommand.option_list
    help = "Run our tests with profiling turned on"
    args = "[appname ...]"

    requires_model_validation = False

    def handle(self, *tests, **options):
        # pylint: disable-msg=R0801
        """
        Dispatch the command

        Arguments:
        - `*tests`: test labels
        - `**options`: passed opts
        """
        verbosity = int(options.get('verbosity', 1))
        interactive = options.get('interactive', True)
        profile_tests(tests, verbosity=verbosity,
                      interactive=interactive)

