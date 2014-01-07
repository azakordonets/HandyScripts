import socks
import socket
def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "localhost", 9050)

# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection

import urllib2

print urllib2.urlopen('http://opp.leaseweb.com/orderService.wsdl').read()

import mechanize
from mechanize import Browser

br = Browser()
print br.open('http://opp.leaseweb.com/orderService.wsdl').read()