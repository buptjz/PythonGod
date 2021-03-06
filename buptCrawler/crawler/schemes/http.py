


"""This module defines the functions needed for filling in information in Link
objects for urls using the http scheme."""

import config
import debugio
import httplib
import urllib
import urllib2
import time
import urlparse
import base64
import socket
import re
import cookielib

# pattern for extracting character set information from content-type header
_charsetpattern = re.compile('charset=([^ ]*)', re.I)

# set socket timeout to configured value
#socket.setdefaulttimeout(20)

def fetch(link,acceptedtypes):
    try:
        try:
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'),('Connection','Keep-Alive'),('Pragma', 'no-cache'),('Cache-Control', 'no-cache'),] 
 

            r = opener.open(link.url)
            '''
            if r.headers.has_key('Etag'):
                opener.addheaders.append(('If-None-Match',r.headers['Etag']))
                e = opener.open(link.url)
                if e.code != 304:
                    r.close()
                    r=e                    
            '''
            try:
                link.status = r.code
            except:
                pass
            try:
                link.mimetype=r.headers['Content-type'].split(';')[0]  #to do
            except:
                pass
            try:
                link.mtime = time.mktime(r.headers['Last-Modified']) # to do 
            except:
                pass
                        
            try:
                link.size = int(r.headers['Content-Length']) #to do
            except:
                pass
            
            
            if r.code in (301, 302, 303, 307):
                # consider a 301 (moved permanently) a problem
                if r.code == 301:
                    link.add_linkproblem(str(r.code))
                # find url that is redirected to
                location = urlparse.urljoin(link.url, r.headers['Location']) ###########################################
                # create the redirect
                link.redirect(location) ################################################################################
                r.close()
                return None
            elif r.code != 200:
                # handle error responses
                link.add_linkproblem(str(r.code))
                r.close()
                return None
            elif link.mimetype in acceptedtypes:
                # return succesful responses
                # TODO: support gzipped content
                # TODO: add checking for size
                link.url = r.geturl()
                t = r.read()
                r.close()
                return t     
        
        except urllib2.HTTPError,e:
            link.status=e.code
            r.close()
            
        except urllib2.URLError, e:
            print e.reason
            link.status=408
            r.close()
         
    except:
        pass    


'''
def fetch(link, acceptedtypes):
    """Open connection to url and report information given by GET command."""
    # TODO: HTTP connection pooling?
    # TODO: implement proxy requests for https
    # split netloc in user:pass part and host:port part
    
    (userpass, netloc) = urllib.splituser(link.netloc)
    # if the URL did not contain userpass and the netloc is configured
    # get the userpass from that
    if not netloc:
        return
    if not userpass and netloc in config.USERPASS:
        userpass=config.USERPASS[netloc]
        debugio.debug('schemes.http.fetch(): using userpass=%s' % userpass)
    proxyuserpass = None
    scheme = link.scheme
    # check validity of netloc (to work around bug in idna module)
    if netloc[0] == '.':
        debugio.debug('schemes.http.fetch(): fail on hostname starting with dot')
        link.add_linkproblem('hostname starts with a dot')
        return None
    # check which host to connect to (if using proxies)
    if config.PROXIES and config.PROXIES.has_key(link.scheme):
        # pass the complete url in the request, connecting to the proxy
        path = urlparse.urlunsplit((link.scheme, netloc, link.path, link.query, ''))
        (scheme, netloc) = urlparse.urlsplit(config.PROXIES[link.scheme])[0:2]
        (proxyuserpass, netloc) = urllib.splituser(netloc)
    else:
        # otherwise direct connect to the server with partial url
        path = urlparse.urlunsplit(('', '', link.path, link.query, ''))
    # remove trailing : from netloc
    if netloc[-1] == ':':
        netloc = netloc[:-1]
    conn = None
    try:
        
        try:
            # create the connection
            debugio.debug('schemes.http.fetch: connecting to %s' % netloc)
            if scheme == 'http':
                conn = httplib.HTTPConnection(netloc)
            elif scheme == 'https':
                conn = httplib.HTTPSConnection(netloc)
            conn.set_debuglevel(100)
            # start the request
            conn.putrequest('GET', path, skip_host=True)
            conn.putheader('Host', urllib.splitport(netloc)[0])
            if userpass is not None:
                (user, passwd) = urllib.splitpasswd(userpass)
                conn.putheader(
                  'Authorization',
                  'Basic '+base64.encodestring(str(user)+':'+str(passwd)).strip() )
            if proxyuserpass is not None:
                (user, passwd) = urllib.splitpasswd(proxyuserpass)
                conn.putheader(
                  'Proxy-Authorization',
                  'Basic '+base64.encodestring(str(user)+':'+str(passwd)).strip() )
            # bypass proxy cache
            if config.BYPASSHTTPCACHE:
                conn.putheader('Cache-control', 'no-cache')
                conn.putheader('Pragma', 'no-cache')
            conn.putheader('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1) ')
            conn.endheaders()
            # wait for the response
            response = conn.getresponse()
            #link.status = '%s %s' % (response.status, response.reason)
            link.status = '%s' % response.status  ###########################################################3
            debugio.debug('schemes.http.fetch(): HTTP response: %s' % link.status)
            # dump proxy hit/miss debugging info
            if config.PROXIES and config.PROXIES.has_key(link.scheme):
                try:
                    debugio.debug('schemes.http.fetch(): X-Cache: %s' % str(response.getheader('X-Cache')))
                except AttributeError:
                    pass
            # retrieve some information from the headers
            try:
                link.mimetype = response.msg.gettype().lower() #################################################
                debugio.debug('schemes.http.fetch(): mimetype: %s' % str(link.mimetype))
            except AttributeError:
                pass
            ''''''
            try:
                link.set_encoding(_charsetpattern.search(response.getheader('Content-type')).group(1))
            except (AttributeError, TypeError):
                pass
                
            try:
                link.size = int(response.getheader('Content-length')) ###############################################
                debugio.debug('schemes.http.fetch(): size: %s' % str(link.size))
            except (KeyError, TypeError):
                pass
            try:
                link.mtime = time.mktime(response.msg.getdate('Last-Modified')) ###########################################
                debugio.debug('schemes.http.fetch(): mtime: %s' % time.strftime('%c', time.localtime(link.mtime)))
            except (OverflowError, TypeError, ValueError):
                pass
            # handle redirects
            # 301=moved permanently, 302=found, 303=see other, 307=temporary redirect
            if response.status in (301, 302, 303, 307):
                # consider a 301 (moved permanently) a problem
                if response.status == 301:
                    link.add_linkproblem(str(response.status)+': '+response.reason)
                # find url that is redirected to
                location = urlparse.urljoin(link.url, response.getheader('Location', '')) ###########################################
                # create the redirect
                link.redirect(location) ################################################################################
                return None
            elif response.status != 200:
                # handle error responses
                link.add_linkproblem(str(response.status)+': '+response.reason)
                return None
            elif link.mimetype in acceptedtypes:
                # return succesful responses
                # TODO: support gzipped content
                # TODO: add checking for size
                return response.read()
        except httplib.HTTPException, e:
            debugio.debug('error reading HTTP response: '+str(e))
            link.add_linkproblem('error reading HTTP response: '+str(e))
            return None
        except (socket.error, socket.sslerror), e:
            if hasattr(e, 'args') and len(e.args) == 2:
                debugio.debug("error reading HTTP response: "+str(e.args[1]))
                link.add_linkproblem("error reading HTTP response: "+str(e.args[1]))
            else:
                debugio.debug("error reading HTTP response: "+str(e))
                link.add_linkproblem("error reading HTTP response: "+str(e))
            return None
        except KeyboardInterrupt:
            # handle this in a higher-level exception handler
            raise
        except Exception, e:
            # handle all other exceptions
            debugio.warn('unknown exception caught: '+str(e))
            link.add_linkproblem('error reading HTTP response: '+str(e))
            import traceback
            traceback.print_exc()
            return None
    finally:
        # close the connection before returning
        if conn is not None:
            conn.close()
'''
            
if __name__ == '__main__':
    
    conn = httplib.HTTPConnection('www.jl.10086.cn')
    conn.putrequest('GET', '/10086/channel/tonghua/', skip_host=True)
    conn.putheader('Host', 'www.jl.10086.cn:80')
    #conn.putheader('Cache-control', 'no-cache')
    #conn.putheader('Pragma', 'no-cache')
    conn.putheader('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
    conn.endheaders()
    
    response = conn.getresponse()
    #link.status = '%s %s' % (response.status, response.reason)
    link.status = '%s' % response.status
    
    print link.status