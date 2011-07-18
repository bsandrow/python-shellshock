ShellShock
==========

A collection of shell utilities/helpers for Python.

shellshock.runner
-----------------

    import sys
    import shellshock.runner

    class MyRunner(shellshock.runner.Runner):
        __optspec__ = [
            { 'args': ['-f', '--file'], 'dest':'filename' },
            { 'args': ['-n', '--dry-run'], 'dest':'dryrun', 'action': 'store_true' },
        ]

        def run(self):
            if self.options.dryrun:
                print "Dry Run!"
                sys.exit()
            print "File: %s" % (self.options.file)

    MyRunner().run()

Automatically creates an option parser (at `self._optparser`) using optparse,
and converts `__optspec__` into `self.options` and `self.args`. The original
args (prior parsing) are stored in `self._orig_args`. Parses `sys.argv` by
default, if no args are passed into the class. If you want to send no args,
then do something like this:

    MyRunner([]).run()

Basically passes the each dict directly to a `parser.add_option()` call as
`**kwargs`, with the 'args' key-value pair stripped and the value is passed
through to `add_option()` as `*args`. Therefore:

    __optspec__ = [
        { 'args': ['-f','--file'], 'dest':'filename' }
    ]

is equivalent to:

    parser.add_option('-f', '--file', dest='filename')

shellshock.tee
--------------

    import shellshock.tee

    tee = shellshock.tee.Tee(files=['test.log', 'test.log.1'],
            append=True)
    print >> tee, "My Message"

    tee.add_file('test.log.2')
    print >> tee, "My Message 2"

    tee.close()

The purpose of **Tee** is to allow the unix 'tee' utility to be
easily emulated within Python. It creates a file-like object that
allows the user to write to it, and that data will be written to
all associated files, as well as (optionally) stderr and/or
stdout.

Apparently I can't claim that this is a file-like object without a
read() method, but this is a write-only object, so I don't see the
need to define it. Personally, I view calling the read() method on a
file that was open for writing only as an undefined operation.

Author
------

Brandon Sandrowicz <brandon@sandrowicz.org>

License
-------

BSD 3-clause license. See LICENSE file for terms.
