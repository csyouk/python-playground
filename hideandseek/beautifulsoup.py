import urllib2
from BeautifulSoup import BeautifulSoup
html = urllib2.urlopen('http://google.com').read()
soup = BeautifulSoup(html)
links = soup('a')

for i in links:
    print i
# f = open('tiny-games-app.html', 'w')
# for link in len(links):
#     f.write(link)
# f.close()
