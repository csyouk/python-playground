import urllib2
response = urllib2.urlopen('http://www.pnas.org/content/111/24/8788.full')
html = response.read()

f = open('emotion-contagion-thru-social-network.html','w')
f.write(html)
f.close()


print 'response.info : ', response.info()
