"""Sample code to test KwArgsChecker plugin."""


def do(*, obj_id, action):
    """Correct. Takes only keyword arguments using Python 3 syntax."""
    pass


def do_py2(**kwargs):
    """Correct. Takes only keyword arguments."""
    pass


def do_py2_wrong(*args, **kwargs):
    """Should fail the check. Takes variable arguments."""
    pass


def do_noargs():
    """Correct. Takes no arguments at all."""
    pass


def do_wrong(param):
    """Should fail the check. Takes a variable argument."""
    pass


class Service(object):
    """Dummy class to test that we also check inside a class."""

    def __init__(self):
        """Dummy constructor."""
        pass

    def do(self, *, obj_id, action):
        """Correct. Takes only keyword arguments using Python 3 syntax."""
        pass

    def do_py2(self, **kwargs):
        """Correct. Takes only keyword arguments."""
        pass

    def do_py2_wrong(self, *args, **kwargs):
        """Should fail the check. Takes variable arguments."""
        pass

    def do_noargs(self):
        """Correct. Takes no arguments at all."""
        pass

    def do_wrong(self, param):
        """Should fail the check. Takes a variable argument."""
        pass

    @staticmethod
    def do_one_arg_wrong(param):
        """Should fail the check. Takes an argument that is not self or cls."""
        pass
