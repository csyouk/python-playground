# coding: utf-8
import urllib2
urllink = 'http://hideandseek.net/projects/'
fileformat = '.html'
# projectnamelist = ['searchlight','99-tiny-games','the-building-is']
projectnamelist = ['the-sandpit','the-hideseek-weekender','last-will','drunk-dungeon','would-anyone-miss-you','consultancy','tiny-christmas-games','the-new-year-games','dreams-of-your-life','the-show-must-go-on','tiny-games','hinterland','green-lantern','the-boardgame-remix-kit','playstation-game-runners','battlefield','the-wonderlab','the-london-poetry-game-2','tate-trumps','221b','ntw-05-–-the-beach','international-sandpit-project','va-lates-playgrounds','playmakers']
for project in projectnamelist:
    link = urllink + project
    filename = project + fileformat
    request = urllib2.Request(link)
    request.add_header("User-Agent","Python Crawler")
    opener = urllib2.build_opener()
    response = opener.open(request)
    html = response.read()
    f = open(filename,'w')
    f.write(html)
    f.close()
