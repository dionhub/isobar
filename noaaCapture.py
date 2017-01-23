# return a log file of when a web file is updated
# option to save down updated files - to collect all unique files in a directory
# option to save down time file checked and boolian if updated - for analyzing the pattern of update times
# not sure how to keep the last file details without reading from disk when using cron, so using sleep
# todo: (1) close logfile (2) date format from Last-Modified same as datetime (3) convert all times to Pacific time
# style questions 1) global variables 2) ''' format for commenting 3) debug info to screen
# use dtName to make it clear which vars are in date formats
# v1 saving with str versions of dates
# v2 converting url time to datetime
# v3 wholesale change of date vars to 3 in dt().str (start, prev, cur)
#  v4 keep in datetime formats and only convert to str to output
#  q is this style ok - comments, S strings? - urlopen light on server resources?
# v4 done - next project - linking png files together into a movie
import time, datetime
import os, urllib2, urllib
print '------------'

''' startup variables'''
dtFormat = "%Y-%m-%d__%H-%M-%S";
url = 'http://www.opc.ncep.noaa.gov/P_sfc_full_ocean_color.png'
os.chdir('/Users/dion/Dropbox/_FUN/Coding/dionProjects/WebCapture2/')
prevModified = datetime.datetime(1999, 1, 1, 1, 1, 1)
prevModifiedS = prevModified.strftime(dtFormat)

startTime = datetime.datetime.utcnow()
startTimeS = startTime.strftime(dtFormat)
print 'startTime:            %s' % startTimeS
logFileName = 'logs/Log_%s.txt' % startTimeS
print 'logFileName: %s' % logFileName
with open(logFileName, 'a') as f:
    f.write('Opening log file at: %s UTC\n\n' % startTimeS)
print '------------'

"""
obtain the last modified time info from a URL.
If it differs to the previous modified time then save URL content to disk.
"""
def fetch_image_from_url(prevModified, saveFile = True):
    print 'prevModified: %s' % prevModifiedS

    imageFile = urllib2.urlopen(url)
    lastModifiedTupple = imageFile.info().getdate('Last-Modified') # print 'lastModified: %s' % str(lastModifiedTupple)
    lastModified = datetime.datetime(*lastModifiedTupple[0:6])
    lastModifiedS = lastModified.strftime(dtFormat) # print repr(lastModified)
    print 'lastModified: %s' % lastModifiedS
    print '------------'
    currTime = datetime.datetime.utcnow()
    currTimeS = currTime.strftime(dtFormat)

    with open(logFileName, 'a') as f:
        f.write('currTime: %s, lastModified: %s\n' % (currTimeS, lastModifiedS))
        if lastModified != prevModified:
            # determine the time difference since the last file update
            dtDelta = lastModified - prevModified
            print (dtDelta)
            f.write('new file since %s \n\n' % dtDelta)
            if saveFile:
                urllib.urlretrieve(url, 'images/Noaa-%s.png' % str(lastModifiedS))
    return lastModified

""" run the loop at time intervals, return the last modified time """
for i in range(1000000):   # set an end date
    prevModified = fetch_image_from_url(prevModified)
    time.sleep(10*60)


'''
time variables:

startTime
prevModified
currentModified
'''
