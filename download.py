import shutil
import sys, urllib.request, re
#from urllib.parse import urlparse
from bs4 import BeautifulSoup


def get_large_file(url, file, length=16*1024):
    req = urllib.request.urlopen(url)
    with open(file, 'wb') as fp:
        shutil.copyfileobj(req, fp, length)
        
if not len(sys.argv) == 2:
    print("Usage: " + sys.argv[0] + " <URL>", file=sys.stderr)
    sys.exit()

url = sys.argv[1]

f = urllib.request.urlopen(url)
soup = BeautifulSoup(f.read(), "lxml")
for i in soup.find_all('a', attrs={'href': re.compile('(?i)(zip|xlsx)$')}):
    fileurl=i.get('href')
    filename="/Users/aiyenggar/OneDrive/data/archive/20170307-patentsview/" + fileurl.split('/')[-1]
    print(fileurl + " -> " + filename)
    get_large_file(fileurl, filename)
#    urllib.request.urlretrieve(i.get('href'), file=)
