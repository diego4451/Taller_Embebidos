import os
import cv2

i = 1
Current = 'From/'
Next = 'To/'

while(True):
    img = cv2.imread(Current + str(i) + '.png', 1)    
    try:
        img.any()
        cv2.imshow('Image', img)    #Show Image
        os.system('mv ' + Current + str(i) + '.png ' + Next)    #Move file

    except:                         #Error Handling
        print('Can\'t find file path:', Current + str(i) + '.png')

    if cv2.waitKey(1000)==27:       # Esc key to stop
        exit()

    if(i == 10):                    #Loop through files
        i = 1
        temp = Current              #Swap To/ and From/
        Current = Next
        Next = temp
    else:
        i += 1
    

