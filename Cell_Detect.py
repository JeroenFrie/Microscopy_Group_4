import cv2
import numpy as np

img_name = "21_12_Time_11;28;20_Con_2_edge_res_1"
save_name = "28;20_Detect_Test_1"

folder_path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/New_Res_Images/"
save_path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/Detect_image/"

path = folder_path+img_name+".png"
save_path = save_path+save_name+".png"

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
white_list = np.zeros(img.shape)

connectivity = 8
output = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_32S)
centroids = np.array(output[3])

centroids_rounded = (np.rint(centroids)).astype(int)
for coords in centroids_rounded:
    x = coords[0]
    y = coords[1]
    white_list[y,x] = 255
white_list = white_list.astype(np.uint8)

kernel_dilate = np.ones((4,4),np.uint8)
dilated = cv2.dilate(white_list, kernel_dilate, iterations = 3)


while(True):
    cv2.imshow('Test', dilated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(save_path, dilated)
        break

print(centroids_rounded.shape)