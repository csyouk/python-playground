# coding: utf-8
import urllib2
urllink = 'http://rstudio-pubs-static.s3.amazonaws.com/9689_803940866e174945baf297c92bb633e2.html#/'
fileformat = '.html'
# projectnamelist = ['searchlight','99-tiny-games','the-building-is']
projectnamelist = []
for i in range(0,36):
    i = str(i)
    link = urllink + i
    filename = i + fileformat
    request = urllib2.Request(link)
    request.add_header("User-Agent","Python Crawler")
    opener = urllib2.build_opener()
    response = opener.open(request)
    html = response.read()
    f = open(filename,'w')
    f.write(html)
    f.close()
#
# for project in projectnamelist:
#     link = urllink + project
#     filename = project + fileformat
#     request = urllib2.Request(link)
#     request.add_header("User-Agent","Python Crawler")
#     opener = urllib2.build_opener()
#     response = opener.open(request)
#     html = response.read()
#     f = open(filename,'w')
#     f.write(html)
#     f.close()
