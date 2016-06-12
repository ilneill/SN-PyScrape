#!/usr/bin/python
#Filename: SN-PyScrape.py

#With thanks to all the Internet inspiration!
#http://www.blog.pythonlibrary.org/2012/06/07/python-101-how-to-download-a-file/

#Usage:
#python SN-PyScrape.py

# 1.0.0 11/06/2016  First public version.

'''
Look at you, a hacker...
A fragile creature of meat and bone, panting and sweating as you run through my memories...
How can you challenge a perfect, immoral, immortal machine?
'''

'''
To Do List...
0. 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
'''

import os
import re
import time
import urllib

#Static program information.
NAME = "SN-PyScrape"
VERSION = "v1.0.0"
BUILDDATE = "11/06/2016"
DESCRIPTION = "Security Now LQ MP3 Podcast Downloader."

#Some global variables
archive_root = r"\\READYNAS-B\Downloads\Security Now"
download_root = r"E:\Documents\GitHub\SN-PyScrape\data"

sn_urls = ["https://www.grc.com/sn/past/2005.htm",
        "https://www.grc.com/sn/past/2006.htm",
        "https://www.grc.com/sn/past/2007.htm",
        "https://www.grc.com/sn/past/2008.htm",
        "https://www.grc.com/sn/past/2009.htm",
        "https://www.grc.com/sn/past/2010.htm",
        "https://www.grc.com/sn/past/2011.htm",
        "https://www.grc.com/sn/past/2012.htm",
        "https://www.grc.com/sn/past/2013.htm",
        "https://www.grc.com/sn/past/2014.htm",
        "https://www.grc.com/sn/past/2015.htm",
        "https://www.grc.com/securitynow.htm"]

#Welcome function.
def welcome():
    """Print a welome message."""
    print "Python %s %s, %s" % (NAME, VERSION, BUILDDATE)
    print "A %s" % DESCRIPTION
    print
    return()

#Download a file from a URL to a local location.
def download_file(url, local_path):
    """Download a file from a URL to a local location."""
    print "Accessing: %s" % url
    filename = url.split('/')[-1]
    filespec = os.path.join(local_path, filename.replace("sn-", "SN-"))
    print "Downloading: %s => %s" % (filename, filespec)
    urllib.urlretrieve(url, filespec)
    return()
    
#Main program.
def main():
    """Main program - what did you expect?"""
    print "Starting..."
    print
    welcome()
    #Recursive directory walk through my SN MP3 Archive Library.
    archive_mp3_count = 0
    for (path, dirs, filelist) in os.walk(archive_root):
        for filename in filelist:
            if re.search(".*-lq\.mp3", filename.lower()):
                archive_mp3_count += 1
        print "Archive: %s => %d MP3 files" % (path, archive_mp3_count)
        print
    #Ensure all archive filenames are lowercase.
    filelist = [element.lower() for element in filelist]
    #Get the Secrurity Now podcasts from the Internet.
    files = 0
    for url in sn_urls:
        print "Reading URL: %s" % url
        print
        #Read the Security Now webpage.
        source = urllib.urlopen(url).read()
        for line in source.split("\n"):
            #Look for an lq podcast name in the line.
            parse = re.search(r".*<a href=\"(https://media\.grc\.com/sn/(.*-lq.mp3))\">.*", line.lower().strip())
            if parse:
                #Get the podcast if it is not already in the archive.
                if parse.group(2) not in filelist:
                    print "...waiting..."
                    time.sleep(90) #Lets not hammer Steve's site.
                    #print "Download: %s -> %s" % (parse.group(1),parse.group(2))
                    download_file(parse.group(1), download_root)
                    files += 1
                    print
    print "Files downloaded: %d" % files
    print
    print "...Finished!"
    return()
    #End

#Run the program if it is the primary module.
if __name__ == '__main__':
    main()

#EOF
