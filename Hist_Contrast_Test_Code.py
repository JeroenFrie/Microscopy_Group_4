import cv2
from matplotlib import pyplot as plt

path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1.png"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
while(True):
    cv2.imshow('Test',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
plt.show()

equ = cv2.equalizeHist(img)

plt.hist(equ.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
plt.show()

File_Path_Con_1 = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1_Con_1.png"

while(True):
    cv2.imshow('Test', equ)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(File_Path_Con_1, equ)
        break

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

File_Path_Con_2 = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1_Con_2.png"

while(True):
    cv2.imshow('Test', cl1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(File_Path_Con_2, cl1)
        break


clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(8, 8))
cl2 = clahe.apply(img)

File_Path_Con_2 = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/test_1_Con_3.png"

while(True):
    cv2.imshow('Test', cl2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(File_Path_Con_2, cl2)
        break