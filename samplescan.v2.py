#Code to run the microscope and scan the entire sample, including making pictures

#Import necessary libraries
import uc2rest as uc2
import cv2
import random

#Make a connection with the board
serialport = "COM5" # for Windows - change accordingly

if 'ESP32' not in locals():
    ESP32 = uc2.UC2Client(serialport=serialport)
_state = ESP32.state.get_state()
print(_state)

# we don't want to change the configuration now
# OR setup motors individually (according to WEMOS R32 D1)
if 0:
    ESP32.motor.set_motor(stepperid = 1, position = 0, stepPin = 26, dirPin=16, enablePin=12, maxPos=None, minPos=None, acceleration=None, isEnable=1)
    ESP32.motor.set_motor(stepperid = 2, position = 0, stepPin = 25, dirPin=27, enablePin=12, maxPos=None, minPos=None, acceleration=None, isEnable=1)
    ESP32.motor.set_motor(stepperid = 3, position = 0, stepPin = 17, dirPin=14, enablePin=12, maxPos=None, minPos=None, acceleration=None, isEnable=1)
    ESP32.motor.set_motor(stepperid = 0, position = 0, stepPin = 19, dirPin=18, enablePin=12, maxPos=None, minPos=None, acceleration=None, isEnable=1)

#DEFINING DIFFERENT FUNCTIONS

def Move_X(steps):
    ESP32.motor.move_xyz(
    steps=(-steps, 2*steps, -steps),
    speed=(10000, 10000, 10000),
    acceleration=None,
    is_blocking=False,
    is_absolute=False,
    is_enabled=True
)
    
def Move_Y(steps):
    ESP32.motor.move_xyz(
    steps=(steps, 0, -steps),
    speed=(10000, 10000, 10000),
    acceleration=None,
    is_blocking=False,
    is_absolute=False,
    is_enabled=True
)

def Move_Z(steps):
    ESP32.motor.move_xyz(
    steps=(steps, steps, steps),
    speed=(10000, 10000, 10000),
    acceleration=None,
    is_blocking=False,
    is_absolute=False,
    is_enabled=True
)


def file_generation(max_columns, row_nr, column_nr):
    if (column_nr == max_columns - 1) and (
            (row_nr % 2) == 0):  # check if row has already been shifted down and change direction to right
        column_nr += 1
        row_nr += 1

    if (column_nr == 0) and (
            (row_nr % 2) != 0):  # check if row has already been shifted down and change direction to right
        column_nr -= 1
        row_nr += 1

    if ((row_nr % 2) == 0):  # one col to the right
        column_nr += 1

    if ((row_nr % 2) != 0):  # one col to the left
        column_nr -= 1

    return ((str(row_nr) + ";" + str(column_nr)), row_nr, column_nr)
def take_image(vid,max_colums,row,column):
    y1 = 100
    y2 = 1080 - y1
    x1 = 250
    x2 = 1920 - x1
    Image_Name,row,column = file_generation(max_colums,row,column)
    Image_Name = "Image_" + Image_Name + ".png"
    file_path = File_Pathing + Image_Name
    while (True):
        ret, frame = vid.read()
        frame = cv2.resize(frame, (1920, 1080))
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        FrameNewRes = grayFrame[y1:y2, x1:x2]
        cv2.imwrite(file_path, FrameNewRes)
        break
    return row,column

Original_filename = str(row) + ";" + str(column)

File_Pathing = "C:/Users/20202619/OneDrive - TU Eindhoven/Vakken/CBL Microscopy/Python_Code_Microscope_Redux/Test_Folder/"

file_path = File_Pathing + Original_filename + ".png" #Filepath where image is written
max_rows = 6  #number of rows
max_colums = 6 #number of columns
row = 0
column = 0
#START SCANNING & MAKING PICTURES
    
#First set the micro up to go to the left top of the sample 
Move_X(-36000)
Move_Y(79050)

vid = cv2.VideoCapture(0)
#take image
take_image(vid)
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


#Big bulk scanning 
j=0
while j<3:
    
    #Start scanning the first row (move right)
    i=0
    while i<5:
        Move_X(24000)

        vid = cv2.VideoCapture(0)
        #take image
        row, column = take_image(vid,max_colums,row,column)
        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        i=i+1


    #Move one row down
    Move_Y(-52700)

    vid = cv2.VideoCapture(0)
    #take image
    row, column = take_image(vid,max_colums,row,column)
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


    #Start scanning the second row (move left)
    k=0
    while k<5:
        Move_X(-24000)

        vid = cv2.VideoCapture(0)
        #take image
        row, column = take_image(vid,max_colums,row,column)
        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        k=k+1

    #Move one row down
    Move_Y(-52700)

    vid = cv2.VideoCapture(0)
    #take image
    take_image(vid)
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    #Move one row down
    Move_Y(-52700)

    j=j+1



#Move back to the middle of the sample (depends on where we end)
Move_X(36000)
Move_Y(131750)

