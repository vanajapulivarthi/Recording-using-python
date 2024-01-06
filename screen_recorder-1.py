import pyautogui
import cv2
import numpy as np
from win32api import GetSystemMetrics

 #specify resolution
width= GetSystemMetrics(0)
height=GetSystemMetrics(1)
name=input("Enter the file name:-")
file_name=f'{name}.mp4'

fourcc=cv2.VideoWriter_fourcc(*"XVID") # specify video codec
            
captured_video=cv2.VideoWriter(file_name,fourcc,20.0,(width,height)) #creating a video writer object

#create an empty window
#cv2.namedWindow("Live",cv2.WINDOW_NORMAL)

#resize this window
#cv2.resizeWindow("Live",480,270)


#webCam
webcam=cv2.VideoCapture(0)


while True :

    img=pyautogui.screenshot()
    img_final=np.array(img)
    img_final=cv2.cvtColor(img_final,cv2.COLOR_BGR2RGB) 
    
    
    #webcam code
    _ , frame=webcam.read()   
    fr_height,fr_width,_=frame.shape
    cv2.imshow("webcam",frame)
    
    captured_video.write(img_final)
   
    
   
    if cv2.waitKey(1)==ord('q'):
        break

captured_video.release()  # release the video writer

cv2.destroyAllWindows() #destroy all the windows
