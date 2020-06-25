from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", default='/bin/vigilante/Avistamientos', help="path to images directory")
args = vars(ap.parse_args())

imagesPaths = list(paths.list_images(args["images"]))

for imagePath in imagesPaths :
	image = cv2.imread(imagePath)
	cv2.imshow("Avistamientos", image)
	cv2.waitKey(0)
