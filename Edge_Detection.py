import cv2
import numpy as np
from matplotlib import pyplot as plt
path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1_Con_1.png"
save_path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1_Con_1_edge.png"
img = cv2.imread(path)

img_blur = cv2.GaussianBlur(img, (3,3), 0)

sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=13)

ret, sobelxy = cv2.threshold(sobelxy,0,256,cv2.THRESH_BINARY)

plt.hist(sobelxy.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
#plt.show()


kernel = np.ones((10,10),np.uint8)
gradient = cv2.morphologyEx(sobelxy, cv2.MORPH_GRADIENT, kernel)

kernel_begin = np.ones((3,3),np.uint8)
#dilation = cv2.dilate(sobelxy,kernel,iterations = 1)
closing_1 = cv2.morphologyEx(gradient, cv2.MORPH_CLOSE, kernel_begin)

kernel_middle = np.ones((2,2),np.uint8)
dilation = cv2.dilate(gradient,kernel_middle,iterations = 3)


kernel_second = np.ones((3,3),np.uint8)
closing_2 = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel_second)

#kernel_end = np.ones((2,2),np.uint8)
#closing_3 = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel_end)


while(True):
    cv2.imshow('Test', dilation)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(save_path, dilation)
        break