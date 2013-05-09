


"""This package groups all the supported schemes.

A scheme module can be requested by the get_schememodule() function.
Each module should export the following function:

    fetch(link, acceptedtypes)
        Fetch the link. Some basic information about the document is
        provided if possible (size, mimetype, mtime, status in case of
        errors, etc). Also the contents of the link is fetched and
        returned if the content type is mentioned in the acceptedtypes
        list."""

import re

# pattern to match valid scheme names
_schemepattern = re.compile('^[A-Za-z][A-Za-z0-9]*$')

# a map of schemes to modules
_schememodules = {}

def get_schememodule(scheme):
    """Look up the correct module for the specified scheme."""
    # check validity of scheme name
    if not _schemepattern.search(scheme):
        return None
    # find module for scheme name
    if not _schememodules.has_key(scheme):
        try:
            _schememodules[scheme] = \
              __import__('schemes.'+scheme, globals(), locals(), [scheme])
        except ImportError,e:
            print e
            _schememodules[scheme] = None
    return _schememodules[scheme]
