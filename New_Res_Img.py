import cv2

img_name_con = "21_12_Time_11;38;49_Con_2"
img_name_edge = "21_12_Time_11;28;20_Con_2_edge_1"
folder_path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/First_Images_Segment/"

img_name_con_save = "21_12_Time_11;38;49_Con_2_res"
img_name_edge_save = "21_12_Time_11;28;20_Con_2_edge_res_1"
save_path = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/New_Res_Images/"

path_con = folder_path+img_name_con+".png"
path_edge = folder_path+img_name_edge+".png"

save_path_con = save_path+img_name_con_save+".png"
save_path_edge = save_path+img_name_edge_save+".png"

img_con = cv2.imread(path_con)
img_edge = cv2.imread(path_edge)

y1 = 100
y2 = 1080-y1
x1 = 250
x2 = 1920-x1

img_con_new_res = img_con[y1:y2, x1:x2]
img_edge_new_res = img_edge[y1:y2, x1:x2]


while(True):
    cv2.imshow('Test',img_con)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


while(True):
    cv2.imshow('Test',img_con_new_res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(save_path_con, img_con_new_res)
        break

while(True):
    cv2.imshow('Test',img_edge_new_res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(save_path_edge, img_edge_new_res)
        break

