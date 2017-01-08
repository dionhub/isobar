# return a log file of when a web file is updated
# option to save down updated files - to collect all unique files in a directory
# option to save down time file checked and boolian if updated - for analyzing the pattern of update times
# not sure how to keep the last file details without reading from disk when using cron, so using sleep

import time, datetime
import os, urllib2, urllib
#
# curTime = datetime.datetime.now()
# format = "%Y%M%D-%H:%M:%S"
# print str(curTime)




os.chdir('/Users/dion/Dropbox/_FUN/Coding/dionProjects/WebCapture/')

saveFile = True
targetUrl = 'http://www.opc.ncep.noaa.gov/P_sfc_full_ocean_color.png'
prevFileTime = ''
currFileTime = ''
logFileName = 'noaaCaptureLog-'+ str(datetime.datetime.now()) + '.csv'
logFile = open(logFileName, 'w')

for i in range(5):   # while(true)

    targetFile = urllib2.urlopen(targetUrl)
    currFileTime = targetFile.info().getdate('last-modified')
    # print currFileTime, prevFileTime
    logFile.write(str(datetime.datetime.now())+','+ str(currFileTime)+'\n')
    print (str(datetime.datetime.now()), str(currFileTime))

    if (currFileTime != prevFileTime):
        #append time and currFileTime to log file
        logFile.write('new file\n')

        if saveFile:
            saveFileName = 'png/noaa-'+ str(currFileTime) +'.png'   #yymmdd:hm:mm:ss"
            # print str(currFileTime)
            print saveFileName
            urllib.urlretrieve(targetUrl, saveFileName)

    prevFileTime = currFileTime
    targetFile.close()
    time.sleep(1)

logFile.close()
