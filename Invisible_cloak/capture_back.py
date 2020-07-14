# To capture background image

import cv2

video = cv2.VideoCapture(0)

while video.isOpened():
    check, frame = video.read()
    if check:
        cv2.imshow('Invisibility Cloak', frame)
        
        if cv2.waitKey(1) == ord('n'):
            cv2.imwrite('background.jpg', frame)
            break

video.release()
cv2.destroyAllWindows()

    