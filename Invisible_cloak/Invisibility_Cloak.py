# Program for the Invisibility cloak
import cv2
import numpy as np

video = cv2.VideoCapture(0)
background = cv2.imread('./background.jpg')

while video.isOpened():
    check, frame = video.read()
    if check:
        # converts bgr to hsv
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow('Invisibility Cloak', hsv_frame)

        # for hsv value of red
        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        
        lred = np.array([0,100,90])
        hred = np.array([10,255,255])

        mask = cv2.inRange(hsv_frame, lred, hred)
        # cv2.imshow('mask', mask)        #showing the red portion in white
        kernel = np.ones((5,5),np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        first = cv2.bitwise_and(background, background, mask=mask)
        # cv2.imshow("first", first)          #showing background inside red

        mask = cv2.bitwise_not(mask)
        # cv2.imshow('mask', mask)              #showing exactly opposite of mask

        second = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("second", second)              #shows black instead of red

        cv2.imshow('cloak', first+second)

        if cv2.waitKey(1) == ord('n'):
            break

video.release()
cv2.destroyAllWindows()