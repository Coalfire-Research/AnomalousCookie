#!/usr/bin/python
from selenium import webdriver
import time
import cookielib
import requests
import datetime
import requests
import sys
import os

cookie_lib = []

##### Change to 'yes' below to forward to proxy service #####
proxy = "no"

##### Change this to use custom User-Agent string #####
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
}

##### Change this to point to custom FUZZ FILE #####
fuzzfile = "fuzz.txt"
inputfile = open(fuzzfile, "r")
all_fuzzy = inputfile.readlines()
inputfile.close()

##### Functions/Methods! #####
def helpme():
    print 'EXAMPLE COMMAND:'
    print 'Usage: ./AnomalousCookie-v1.py -1 "https://www.example.com" output ' + "\n"
    print 'ALL POSSIBLE PARAMETERS (1 parameter is required):'
    print 'Usage: ./AnomalousCookie-v1.py -h ' + " :::: " + " HELP!"
    print '       ./AnomalousCookie-v1.py -1 "https://www.example.com" output' + " :::: " + " Append fuzz data before existing cookie payload data."
    print '       ./AnomalousCookie-v1.py -2 "https://www.example.com" output' + " :::: " + " Overwrite existing cookie payload data."
    print '       ./AnomalousCookie-v1.py -3 "https://www.example.com" output' + " :::: " + " Append fuzz data after existing cookie payload data." + "\n"
    sys.exit()


##### Variables! #####
try:
    cliparam = sys.argv[1]
    url = sys.argv[2]
    output_label = sys.argv[3]
except:
    print "\n+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+"
    print "|A|n|o|m|a|l|o|u|s| |C|o|o|k|i|e|"
    print "+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+"
    print "\nDOH! There was a problem running 'Anomalous Cookie'. Please try again!"
    print "--USE ONLY ASCII LETTERS AND/OR NUMBERS IN OUTPUT_LABEL NAME!"
    print "--USE FULL URL WITH PROTOCOL."
    print "--DOES OUTPUT DIRECTORY ALREADY EXIST?" + "\n"
    print "------------------------------------------------------------" + "\n"
    helpme()


if cliparam not in ["-1","-2","-3"]:
    helpme()

##### Create output files! #####
png_output = output_label + "/SCREENSHOT-ORIGINAL-" + output_label + ".png"
csv_output = output_label + "/OUTPUT-" + output_label + "-RESULTS.csv"

##### Create output directory based on provided 'output_label' #####
try:
    os.mkdir(output_label)
except:
    print "\n+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+"
    print "|A|n|o|m|a|l|o|u|s| |C|o|o|k|i|e|"
    print "+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+"
    print "\nDOH! There was a problem creating the output directory. Please try again!"
    print "--USE ONLY ASCII LETTERS AND/OR NUMBERS IN OUTPUT_LABEL NAME!"
    print "--DOES OUTPUT DIRECTORY ALREADY EXIST?" + "\n"
    print "------------------------------------------------------------" + "\n"
    helpme()

##### Fire up all engines and fuzz the cookies! #####
print "-------------------------------------------------------------"
print "\n" + ":::: |A|n|o|m|a|l|o|u|s| |C|o|o|k|i|e| v1.0 - RUNNING!! ::::" + "\n"
print "-------------------------------------------------------------" + "\n"

##### If proxy set to 'yes' then forward browser requests to proxy service (ie: BURP/TOR)! #####
if proxy =="yes":
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", 'localhost')
    profile.set_preference("network.proxy.http_port", 8080)
    profile.set_preference("network.proxy.ssl", 'localhost')
    profile.set_preference("network.proxy.ssl_port", 8080)
    browser = webdriver.Firefox(firefox_profile=profile)
else:
    browser = webdriver.Firefox()


##### Get original request, collect all observed cookies and take a baseline screenshot #####find / 
#browser.set_page_load_timeout(15)
browser.get(url)
all_cookies = browser.get_cookies()
total_cookies1 = len(all_cookies)
total_cookies = str(total_cookies1)
time.sleep(1)
browser.get_screenshot_as_file(png_output)

with open (csv_output, "a") as outputfile:
    outputfile.write("ID" + ";" + "TOTAL-COOKIES: " + total_cookies + ";" + "COOKIE-NAME" + ";" + "COOKIE-VALUE" + ";" + url + "\n")

##### numbers #####
i = 0
ia = str(i)

print "TOTAL COOKIES DETECTED: " + total_cookies + "\n"
print "COOKIE NAME(S): "
for cookie1 in all_cookies:
    print cookie1['name']

print "\n"
print "NOW FUZZING ALL COOKIES!  "

##### main method right here #####
for FUZZY in all_fuzzy:
    FUZZY = FUZZY.strip()
    for cookie in all_cookies:
        cname = cookie['name']
        if cliparam == "-1":
            cval = FUZZY + cookie['value']
        elif cliparam == "-2":
            cval = FUZZY
        elif cliparam == "-3":
            cval = cookie['value'] + FUZZY
        cdom = cookie['domain']
        cdom = cdom.strip('.')
        cpath = cookie['path']
        newcookies = {'name':cname, 'value': cval, 'domain':cdom, 'path':cpath}
        try:
            browser.delete_cookie(cname)
        except:
            pass
            print "error---deleting current cookie! " + "\n" 
        try:
            browser.add_cookie(newcookies)
        except:
            pass
            print "error---adding new cookie!" + "\n"
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
            try:
                png2_output = output_label + "/SCREENSHOT-" + ia + "-" + output_label + ".png"
            except:
                pass
                print "error---saving screenshot1!" + "\n"
            try:
                browser.get_screenshot_as_file(png2_output)
            except:
                pass
                print "error---get screenshot1 error!"
        except:
            print "\n" + " POSSIBLE XSS OR JAVASCRIPT CODE EXECUTION!" + "\n"
            total_cookies3 = " FUZZED! "
            if proxy =="yes":
                profile = webdriver.FirefoxProfile()
                profile.set_preference("network.proxy.type", 1)
                profile.set_preference("network.proxy.http", 'localhost')
                profile.set_preference("network.proxy.http_port", 8080)
                profile.set_preference("network.proxy.ssl", 'localhost')
                profile.set_preference("network.proxy.ssl_port", 8080)
                browser = webdriver.Firefox(firefox_profile=profile)
            else:
                browser = webdriver.Firefox()
                time.sleep(1)
            pass
            try:
                png2_output = output_label + "/SCREENSHOT-" + ia + "-" + output_label + ".png"
            except:
                pass
                print "error---saving screenshot2!" + "\n"
            try:
                browser.get_screenshot_as_file(png2_output)
            except:
                pass
                print "error---get screenshot2 error!"
            #browser.set_page_load_timeout(15)
            browser.get(url)
            time.sleep(1)
            browser.delete_all_cookies()
            for original_cookie in all_cookies:
                browser.add_cookie(original_cookie)
        print "TOTAL COOKIES IN JAR: " + "[" + total_cookies3 + "]" + "\n"
        try:
            with open (csv_output, "a") as outputfile:
                outputfile.write(ia + ";" + total_cookies3 + ";" + cname + ";" + cval + "\n")
        except:
            pass
            print "error---outputfile write malfunction!" + "\n"
        try:
            browser.delete_cookie(cname)
            browser.add_cookie(cookie)
        except:
            pass
            print "error---browser restore cookies!" + "\n"
        i = i + 1
        ia = str(i)

print"\n==============  SHUTTING DOWN!!!   ==============="
print "\n+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+"
print "|A|n|o|m|a|l|o|u|s| |C|o|o|k|i|e|"
print "+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+\n"

all_cookies_final = browser.get_cookies()
total_cookies2 = len(all_cookies_final)
total_cookies3 = str(total_cookies2)
print "FINAL COOKIES DETECTED: " + total_cookies3 + "\n"
print "COOKIE NAME(S): "
for cookie1 in all_cookies_final:
    print cookie1['name']
print "\n\n"

sys.exit()


