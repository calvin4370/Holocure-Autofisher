import cv2 as cv
import numpy as np

haystack_img = cv.imread('haystack.jpg', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('needle.jpg', cv.IMREAD_UNCHANGED)