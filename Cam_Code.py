import cv2
import random

# define a video capture object
vid = cv2.VideoCapture(0)
Image_Name = ""
for i in range(10):
    Image_Name = Image_Name + str(random.randint(1,100))
Image_Name = "Image_"+Image_Name+".png"

#Change depending on if you're not using my (Jeroen) laptop
File_Pathing = "C:/Users/20202619/OneDrive - TU Eindhoven (1)/Documents/TUe/Vakken/test/"

#Filepath where image is written
file_path = File_Pathing + Image_Name

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    frame = cv2.resize(frame, (1920, 1080))
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', grayFrame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(file_path, grayFrame)
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()