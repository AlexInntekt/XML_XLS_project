import datetime
import urllib.request, urllib.error, urllib.parse
from xml.etree.ElementTree import fromstring, ElementTree, tostring
import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup


def extract_image_url(url):
    response = urllib.request.urlopen(url)
    webContent = response.read()
    web_html = webContent.decode('utf-8')
   # reg = r'<article(.|\n)*</article>'
   # #reg = r'(.|\n)*'
   # x = re.search(reg, web_xml)
   # #print(x)
   # ret = x.group(0)
   # #print(ret)
   # with open('o.xml', 'w') as f:
   #     f.write(ret)
    #dom = ET.fromstring(ret)
    soup = BeautifulSoup(web_html, "lxml")
    #print(soup.prettify())
    print(soup.article.div.div.find_all('img')[-1].get('src')) 

def main():
    url="https://www.toptools4learning.com/gobrunch/"
    url="https://www.toptools4learning.com/openlearn/"
    url="https://www.toptools4learning.com/instagram/"
    extract_image_url(url)
    


if __name__=='__main__':
    print(datetime.datetime.now().strftime('%H:%M'))
    main()
