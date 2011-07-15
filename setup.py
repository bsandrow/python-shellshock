
try:
    from setuptools import setup
except ImportError:
    print "Falling back to distutils. Functionality may be limited."
    from distutils.core import setup

config = {
    'description'       : 'A set of tools for shell operations in Python',
    'author'            : 'Brandon Sandrowicz',
    'url'               : 'http://github.com/bsandrow/python-shellshock',
    'author_email'      : 'brandon@sandrowicz.org',
    'version'           : 0.1,
    'install_requires'  : ['nose', 'mock'],
    'packages'          : ['shellshock'],
    'name'              : 'python-shellshock',
}

setup(**config)
