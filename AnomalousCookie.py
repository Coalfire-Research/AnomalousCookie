#!/usr/bin/python
from selenium import webdriver
import time
import cookielib
import requests
import subprocess
import datetime
import re
import requests
import sys
import socket

cookie_lib = []

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
}

fuzzfile = "all-fuzzing.txt"
inputfile = open(fuzzfile, "r")
all_fuzzy = inputfile.readlines()
inputfile.close()

url = sys.argv[1]
domain1 = sys.argv[2]

#url = "http://www.kryio.com"
#domain1 = "kryio.com"

filename1 = "RESULTS/SCREENSHOT-" + domain1 + ".png"
filename3 = "RESULTS/OUTPUT-" + domain1 + "-RESULTS.csv"

print "\n" + "Anomalous Cookie v1.0a - RUNNING!" + "\n"
print "---------------------------------------------------" + "\n"

'''
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", 'localhost')
profile.set_preference("network.proxy.http_port", 8080)
profile.set_preference("network.proxy.ssl", 'localhost')
profile.set_preference("network.proxy.ssl_port", 8080)
browser = webdriver.Firefox(firefox_profile=profile)
'''

browser = webdriver.Firefox()
#browser.set_page_load_timeout(10)
browser.get(url)

all_cookies = browser.get_cookies()
total_cookies1 = len(all_cookies)
total_cookies = str(total_cookies1)


with open (filename3, "a") as outputfile:
    outputfile.write("ID" + ";" + "TOTAL-COOKIES: " + total_cookies + ";" + "COOKIE-NAME" + ";" + "COOKIE-VALUE" + ";" + url + "\n")


time.sleep(1)
browser.get_screenshot_as_file(filename1)

i = 0
ia = str(i)


print "TOTAL COOKIES DETECTED: " + total_cookies + "\n"
print "COOKIE NAME(S): "
for cookie1 in all_cookies:
    print cookie1['name']

print "\n"
print "NOW FUZZING ALL COOKIES!  "

for FUZZY in all_fuzzy:
    FUZZY = FUZZY.strip()
    for cookie in all_cookies:
        cname = cookie['name']
        cval = FUZZY + cookie['value']
        #cval = FUZZY
        cdom = cookie['domain']
        cdom = cdom.strip('.')
        cpath = cookie['path']
        newcookies = {'name':cname, 'value': cval, 'domain':cdom, 'path':cpath}
        try:
            browser.add_cookie(newcookies)
        except:
            pass
            print "error   ---   adding new cookies no good!" + "\n"
        print "\n" + "---------------------------------------------------"
        print "REQUEST ID: " + ia + "       COOKIE NAME: " + cname
        print "---------------------------------------------------"
        print cval
        print "---------------------------------------------------"
        try:
            browser.get(url)
            time.sleep(1)
            all_cookies_fuzzed = browser.get_cookies()
            total_cookies2 = len(all_cookies_fuzzed)
            total_cookies3 = str(total_cookies2)
        except:
            print "\n" + " POSSIBLE XSS OR JAVASCRIPT CODE EXECUTION!" + "\n"
            total_cookies3 = " FUZZED! "
            '''
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", 'localhost')
            profile.set_preference("network.proxy.http_port", 8080)
            profile.set_preference("network.proxy.ssl", 'localhost')
            profile.set_preference("network.proxy.ssl_port", 8080)
            browser = webdriver.Firefox(firefox_profile=profile)
            '''
            browser = webdriver.Firefox() 
            time.sleep(1)
            pass
        print "TOTAL COOKIES IN JAR: " + "[" + total_cookies3 + "]" + "\n"
        filename2 = "RESULTS/SCREENSHOT-" + ia + "-" + domain1 + ".png"
        try:
            browser.get_screenshot_as_file(filename2)
        except:
            pass
            print "error   ---   get screenshot error shit!"
        try:
            with open (filename3, "a") as outputfile:
                outputfile.write(ia + ";" + total_cookies3 + ";" + cname + ";" + cval + "\n")
        except:
            pass
            print "error   ---   outputfile write malfunction!" + "\n"
        i = i + 1
        ia = str(i)
    #   browser.delete_cookie(cname)
    #browser.delete_cookie(cname)
   

print"\nCOMPLETED!\n"
sys.exit()
