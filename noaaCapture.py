# return a log file of when a web file is updated
# option to save down updated files - to collect all unique files in a directory
# option to save down time file checked and boolian if updated - for analyzing the pattern of update times
# not sure how to keep the last file details without reading from disk when using cron, so using sleep
# todo: (1) close logfile (2) date format from Last-Modified same as datetime (3) convert all times to Pacific time

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
print 'logFileName = ' + logFileName # does print need ()?
logFile = open(logFileName, 'w')

for i in range(1000000):   # while(true)

    targetFile = urllib2.urlopen(targetUrl)
    currFileTime = targetFile.info().getdate('Last-Modified')
    # print currFileTime, prevFileTime
    logFile.write(str(i) + ' ' + str(datetime.datetime.now())+','+ str(currFileTime)+'\n')
    print (str(i) +' ' +str(datetime.datetime.now()), str(currFileTime))
    # print
    # print 'CURRENT FILE TIME'
    # print datetime(currFileTime).ctime('')
    # print datetime.datetime(int(currFileTime))
    # print time(currFileTime)
    # print


    if (currFileTime != prevFileTime):
        #append time and currFileTime to log file
        logFile.write('new file since '+ 'x' + '\n') # time diff here
        print ('new file since '+ 'x' + '\n') # time diff here
        print (str(currFileTime) + str(prevFileTime))
        logFile.write(str(currFileTime) + str(prevFileTime))

        if saveFile:
            print '\n'
            print targetFile.info()
            saveFileName = 'png/noaa-'+ str(currFileTime) +'.png'   #yymmdd:hm:mm:ss"
            # print str(currFileTime)
            print saveFileName
            print
            urllib.urlretrieve(targetUrl, saveFileName)

    prevFileTime = currFileTime
    targetFile.close()
    time.sleep(30)

logFile.close()
