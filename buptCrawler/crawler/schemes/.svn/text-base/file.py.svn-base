

"""This module defines the functions needed for creating Link objects for urls
using the file scheme."""

import config
import debugio
import urlparse
import urllib
import os
import mimetypes

def _fetch_directory(link, path, acceptedtypes):
    """Retrieve some basic information about the directory.
    This checks that the directory has a trailing slash and
    returns a list of files in the directory, unless a configured
    filename is found in the directory (in which case this function
    acts as if the file was fetched)."""
    # if the name does not end with a slash, redirect
    if path[-1:] != os.path.sep:
        debugio.debug('directory referenced without trailing slash')
        link.redirect(urlparse.urljoin(link.url, link.path+'/'))
        return None
    # check contents of directory for some common files
    for fname in config.FILE_INDEXES:
        if os.path.isfile(os.path.join(path, fname)):
            debugio.debug('pick up %s from directory' % fname)
            # the the directory contains an index.html, use that
            return _fetch_file(link, os.path.join(path, fname), acceptedtypes)
    # otherwise add the directory's files as children
    debugio.debug('add files as children of this page')
    try:
        link.ispage = True
        for f in os.listdir(path):
            link.add_child(urlparse.urljoin(link.url, urllib.pathname2url(f)))
    except os.error, e:
        link.add_linkproblem(str(e))
    return None

def _fetch_file(link, path, acceptedtypes):
    """Retrieve some basic information of the specified file and return
    the contents of the file."""
    # get stats of file
    try:
        stats = os.stat(path)
        link.size = stats.st_size
        link.mtime = stats.st_mtime
    except os.error, e:
        link.add_linkproblem(str(e))
        return None
    # guess mimetype
    if link.mimetype is None:
        link.mimetype = mimetypes.guess_type(path)[0]
    debugio.debug('mimetype='+str(link.mimetype))
    debugio.debug('acceptedtypes='+str(acceptedtypes))
    # fetch the document if there is any point
    if link.mimetype in acceptedtypes:
        debugio.debug('FETCH')
        try:
            # TODO: add size checking
            return open(path, 'r').read()
        except IOError, e:
            debugio.debug('PROBLEM: '+str(e))
            link.add_linkproblem(str(e))
    return None

def fetch(link, acceptedtypes):
    """Retreive some basic information about the file.
    Store the results in the link object."""
    # get the local path component
    path = urllib.url2pathname(link.path)
    # do special things if we are a directory
    if os.path.isdir(path):
        return _fetch_directory(link, path, acceptedtypes)
    else:
        return _fetch_file(link, path, acceptedtypes)
