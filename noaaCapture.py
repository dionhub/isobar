# return a log file of when a web file is updated
# option to save down updated files - to collect all unique files in a directory
# option to save down time file checked and boolian if updated - for analyzing the pattern of update times
# not sure how to keep the last file details without reading from disk when using cron, so using sleep
# todo: (1) close logfile (2) date format from Last-Modified same as datetime (3) convert all times to Pacific time

import time, datetime
import os, urllib2, urllib

def fetch_image_from_url(prevModified, saveFile = True):
    """obtains last modified info from a URL. If it
    differs to the previous modified time URL content
    will be saved to disk.
    """

    url = 'http://www.opc.ncep.noaa.gov/P_sfc_full_ocean_color.png'
    imageFile = urllib2.urlopen(url)
    logFileName = 'noaaCaptureLog-%s.csv' % str(datetime.datetime.now())
    lastModified = imageFile.info().getdate('Last-Modified')
    currentModified = '%s_%s' % ('-'.join(str(x) for x in lastModified[:3]), ':'.join(str(x) for x in lastModified[3:]))

    with open(logFileName, 'a') as f:
        f.write('%s,%s\n' % (str(datetime.datetime.now()), str(currentModified)))

        if currentModified != prevModified:
            f.write('new file since %s \n' % 'time diff here')

            if saveFile:
                urllib.urlretrieve(url, 'png-noaa-%s.png' % str(currentModified))

    return currentModified

#os.chdir('/Users/dion/Dropbox/_FUN/Coding/dionProjects/WebCapture/')
prevModified = None
for i in range(1000000):   # while(true)
    prevModified = fetch_image_from_url(prevModified)
    time.sleep(30)
