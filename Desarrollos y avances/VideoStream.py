# For more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import cv2
import numpy as np
import os

# Playing video from file:
# cap = cv2.VideoCapture('vtest.avi')
# Capturing video from webcam:
cap = cv2.VideoCapture(0)
f = '0'

for currentFrame in range(1, 49):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Handles the mirroring of the current frame
    frame = cv2.flip(frame,1)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Saves image of the current frame in jpg file
    if(currentFrame == 10):
        f = ''
    name = f + str(currentFrame) + '.jpg'
    cv2.imwrite(name, frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(42)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
os.system('mv *.jpg Capture/')    #Move file

# Potential Error:
# OpenCV: Cannot Use FaceTime HD Kamera
# OpenCV: camera failed to properly initialize!
# Segmentation fault: 11
#
# Solution:
# I solved this by restarting my computer.
# http://stackoverflow.com/questions/40719136/opencv-cannot-use-facetime/42678644#42678644
