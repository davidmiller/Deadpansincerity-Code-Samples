"""
Run our tests with coverage turned on
"""
import sys

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    We totally want to get coverage details, but that's so slow!
    """
    option_list = BaseCommand.option_list
    help = "Run our tests with coverage turned on"
    args = "[appname ...]"

    requires_model_validation = False

    def handle(self, *tests, **options):
        """
        Actually do the test run

        Arguments:
        - `*tests`: test labels
        - `**options`: passed opts
        """
        verbosity = int(options.get('verbosity', 1))
        interactive = options.get('interactive', True)
        mod = __import__("django-test-coverage.runner")
        failures = mod.runner.run_tests(tests, verbosity=verbosity,
                          interactive=interactive)
        if failures:
            sys.exit(bool(failures))
