import urllib2
import urlparse

def make_url(server, port, path, scheme='http'):
    netloc = '{0}:{1}'.format(server, port)
    url = urlparse.urlunsplit((scheme, netloc, path, '', ''))
    return url

server = '10.0.0.2'
port = 9000

print 'Connecting to server at 10.0.0.2:9000'
url = make_url(server, port, '/')
contents = urllib2.urlopen(url).read()

print 'Reading contents from text.txt'
print 'Contents: '
print contents

print 'Running word count job'
count_the = 0
for word in contents.strip().split():
	if word == 'the':
		count_the += 1

print 'Returning the count to server'
path = '/calculation/{0}'.format(count_the)
url = make_url(server, port, path)
result = int(urllib2.urlopen(url).read())
print '{0}'.format(result)

url = make_url(server, port, '/quit')
urllib2.urlopen(url).read()

