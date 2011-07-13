ShellShock
==========

A collection of shell utilities/helpers for Python.

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
all files associated files, as well as (optionally) stderr and/or
stdout.

Author
------

Brandon Sandrowicz <brandon@sandrowicz.org>

License
-------

BSD 3-clause license. See LICENSE file for terms.
