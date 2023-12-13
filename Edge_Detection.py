import cv2

path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1_Con_3.png"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

img_blur = cv2.GaussianBlur(img, (3,3), 0)

sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=15)

while(True):
    cv2.imshow('Test', sobelxy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break