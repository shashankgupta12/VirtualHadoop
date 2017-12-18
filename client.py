import urllib2
import urlparse

def make_url(server, port, path, scheme='http'):
    netloc = '{0}:{1}'.format(server, port)
    url = urlparse.urlunsplit((scheme, netloc, path, '', ''))
    return url

#
# Main
#
server = '10.0.0.2'
port = 9000

# 1 - Request directory listing
url = make_url(server, port, '/')
file_list = urllib2.urlopen(url).read()
print 'Files from server:'
for filename in file_list.splitlines():
    print '- {0}'.format(filename)

# 2 - Request contents of a file
filename = raw_input('Type a file name: ')
url = make_url(server, port, filename)
contents = urllib2.urlopen(url).read()
print 'Contents:'
print contents

# 3 - Upload a file to the server
contents = 'hello, world.\nThe End'
filename = 'foo.txt'
url = make_url(server, port, filename)
f = urllib2.urlopen(url, data=contents)

# 4 - Do some calculation
n1 = 19
n2 = 5
path = '/calculation/{0}/{1}'.format(n1, n2)
url = make_url(server, port, path)
result = int(urllib2.urlopen(url).read())
print '{0} + {1} = {2}'.format(n1, n2, result)

# Send quit signal

url = make_url(server, port, '/quit')
urllib2.urlopen(url).read()
