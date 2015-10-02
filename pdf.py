#!/usr/bin/python -tt

import sys
import urllib
import urllib2
from bs4 import BeautifulSoup

def get_downloadUrl(page_url):
    request = urllib2.Request(page_url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response)
    pdf_links = []
    for a in soup.find_all('a', href=True):
        if 'pdf' in a['href']:
            pdf_links.append(a['href'])
    return pdf_links

    
def download_file(download_url, filename):
    response = urllib2.urlopen(download_url)
    file = open(filename, 'w')
    file.write(response.read())
    file.close()
    print("Completed")

# main function 
def main():
    args = sys.argv[1:]
    if not args:
        print "usage: [page_url]"
        sys.exit(1)

    page_url = args[0]
    pdf_links = get_downloadUrl(page_url)
    count = 1
    for link in pdf_links:
        download_file("http://homes.cerias.purdue.edu/~crisn/courses/cs505_Spring_2013/"
        + link,str(count) + '.pdf')
        count += 1
    


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
