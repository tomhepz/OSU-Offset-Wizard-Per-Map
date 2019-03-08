import time

import cv2
import mss
import numpy
import matplotlib.pyplot as plt
import scipy.stats as stats

def printRow(img):
    rowString = ""
    for pixel in img[0]:
        rowString += str(pixel).rjust(2)
    print(rowString)

def checkHit(img):
    for n, pixel in enumerate(img[0]):
        if pixel > 50:
            return n
    return False

with mss.mss() as sct:
    # Part of the screen to capture
    width = 2560
    height = 1440
    bar_width = 900
    bar_height = 1
    monitor = {"top": (height-bar_height), "left": int((width/2)-(bar_width/2)), "width": bar_width, "height": bar_height}
    oldimg = None
    img = None
    count = 0
    error = []
    while "Screen capturing":
        last_time = time.time()
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        deltaimg = (oldimg if oldimg is not None else img) - img
        oldimg = numpy.copy(img)
        #print("Old:")
        #printRow(oldimg)
        #print("New:")
        #printRow(img)
        #print("Delta:")
        #printRow(deltaimg)
        if checkHit(deltaimg) and img[0][int(bar_width/2)]==255:
            cgit adount += 1
            error.append(-((bar_width/2)-checkHit(deltaimg)))
        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            ######
            h = sorted(error)  #sorted

            fit = stats.norm.pdf(h, numpy.mean(h), numpy.std(h))  #this is a fitting indeed

            plt.plot(h,fit,'-o')

            plt.hist(h,normed=True)      #use this to draw histogram of your data

            plt.show()                   #use may also need add this 
            #####
            cv2.destroyAllWindows()
            break