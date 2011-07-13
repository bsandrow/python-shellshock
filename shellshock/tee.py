import sys

# TODO with statement support
# TODO handle lack of fileobj.flush() in Tee.flush()
# TODO raise exceptions when self.close == True ?

class Tee(object):
    def __init__(self, files=[], stdout=True, stderr=None, append=False):
        self.append     = False
        self.stdout     = stdout
        self.stderr     = stderr
        self.closed     = False
        self.softspace  = 0
        self.newlines   = None
        self.files      = [ ]

        for f in files:
            self.add_file(f)

    def add_file(self, newfile):
        ''' Open a file and append it to the list of file objects that we're
        writing to. Opened in append or write mode based on self.append.'''
        self.files.append(
            open(newfile, 'a+' if self.append else 'w+')
        )

    @property
    def name(self):
        '''Return a list of files that are currently being tee'd, including the
        stderr and/or stderr streams of they are enabled.'''
        strs = [
            [ fileobj.__str__() for fileobj in self.files ]
            + ([ 'stdout' ] if self.stdout else [])
            + ([ 'stderr' ] if self.stderr else [])
        ]
        return '<%s>' % (','.join(strs))

    def close(self):
        '''Close all of the files, and set self.close to True'''
        for fileobj in self.files:
            fileobj.close()
        self.close = True

    def flush(self):
        '''Flush all files, and enabled streams (i.e. stderr and/or stdout)'''
        if self.stdout:
            sys.stdout.flush()
        if self.stderr:
            sys.stderr.flush()
        for fileobj in self.files:
            fileobj.flush()

    def write(self, string):
        '''Write string to all files and enabled streams (i.e. stderr and/or
        stdout)'''
        if self.stdout:
            sys.stdout.write(string)
        if self.stderr:
            sys.stderr.write(string)
        for fileobj in self.files:
            fileobj.write(string)

    def writelines(self, sequence):
        '''Write each string in sequence to all files and enabled streams. Each
        item in sequence is iterated over for each file (rather than just
        passing the sequence on to the .writelines() method on the file
        objects.'''
        for line in sequence:
            if self.stdout:
                sys.stdout.write(line)
            if self.stderr:
                sys.stderr.write(line)
            for fileobj in self.files:
                fileobj.write(line)
