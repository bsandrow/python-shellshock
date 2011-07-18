import optparse

class _MetaRunner(type):
    def __new__(cls, clsname, clsbases, clsdict):
        t = type.__new__(cls, clsname, clsbases, clsdict)

        optspec = getattr(t, '__optspec__', None)
        if optspec:
            parser  = optparse.OptionParser()
            for spec in optspec:
                args = spec['args']
                kwargs = spec.copy()
                del kwargs['args']
                parser.add_option(*args, **kwargs)
            t._optparser = parser

        return t

class Runner(object):
    __metaclass__ = _MetaRunner

    def __init__(self, args=None):
        self._parse_args(args or sys.argv)

    def _parse_args(self, args=None):
        if args is not None:
            self._orig_args = args
        (self.options, self.args) = self._optparser.parse_args(self._orig_args)
