import cv2
import numpy as np
from matplotlib import pyplot as plt
path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1_Con_3.png"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

img_blur = cv2.GaussianBlur(img, (3,3), 0)

sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=15)

ret, sobelxy = cv2.threshold(sobelxy,0,256,cv2.THRESH_BINARY)

plt.hist(sobelxy.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
plt.show()

kernel_begin = np.ones((9,9),np.uint8)
#dilation = cv2.dilate(sobelxy,kernel,iterations = 1)
closing_1 = cv2.morphologyEx(sobelxy, cv2.MORPH_CLOSE, kernel_begin)

kernel_middle = np.ones((7,7),np.uint8)
closing_2 = cv2.morphologyEx(closing_1, cv2.MORPH_CLOSE, kernel_middle)

kernel_end = np.ones((10,10),np.uint8)
closing_3 = cv2.morphologyEx(closing_1, cv2.MORPH_CLOSE, kernel_end)


while(True):
    cv2.imshow('Test', closing_3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break