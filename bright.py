# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())
 
# load the images and convert them to grayscale
image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# initially applied a Gaussian blur to the images, removed this later. Identifying the brightest region
#gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = orig.copy()

if maxVal>230:
	cv2.circle(image, maxLoc, args["radius"], (255, 0, 0), 4)

# you can print these images or make new images with marker on them or just print the csv file
#cv2.imshow("Robust", image)
#cv2.waitKey(0)

cv2.imwrite( "/home/adu/Documents/final/results1/DSC02426.jpg", image )

