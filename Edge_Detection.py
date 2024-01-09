import cv2
import numpy as np
from matplotlib import pyplot as plt
path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/First_Images_Contrast/21_12_Time_11;38;49_Con_2.png"
save_path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/First_Images_Segment/21_12_Time_11;38;49_Con_2_edge_1.png"
img = cv2.imread(path)

# plt.hist(img.ravel(),256,[0,256])
# plt.title('Histogram for gray scale image')
# plt.show()

dst = cv2.calcHist([img], [0], None, [256], [0,256])
max_val = 0
list_dst = list(dst)

value_list_dark = []
value_list_light = []
for i in range(90):
    value_list_dark.append(int(dst[i][0]))

for i in range(len(dst)):
     value_list_light.append(int(dst[i][0]))

final_val_dark = value_list_dark.index(max(value_list_dark))

final_val_light = value_list_light.index(max(value_list_light))

ret, binary_img = cv2.threshold(img,final_val_dark,final_val_light,cv2.THRESH_BINARY)

img_blur = cv2.GaussianBlur(binary_img, (3,3), 0)

sobelxy = cv2.Sobel(src=binary_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=13)

ret, sobelxy = cv2.threshold(sobelxy,0,256,cv2.THRESH_BINARY)

while(True):
    cv2.imshow('Test', sobelxy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.imwrite(save_path, closing_1)
        break

# plt.hist(sobelxy.ravel(),256,[0,256])
# plt.title('Histogram for gray scale image')
# plt.show()


kernel = np.ones((8,8),np.uint8)
gradient = cv2.morphologyEx(sobelxy, cv2.MORPH_GRADIENT, kernel)

while(True):
    cv2.imshow('Test', gradient)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.imwrite(save_path, closing_1)
        break

kernel_begin = np.ones((5,5),np.uint8)

closing_1 = cv2.morphologyEx(gradient, cv2.MORPH_CLOSE, kernel_begin)

kernel_erosion = np.ones((3,3),np.uint8)
erosion = cv2.erode(closing_1,kernel_erosion,iterations = 8)

while(True):
    cv2.imshow('Test', closing_1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(save_path, closing_1)
        break

while(True):
    cv2.imshow('Test', erosion)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.imwrite(save_path, erosion)
        break