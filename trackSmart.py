import cv2
import numpy as np

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#stream = cv2.VideoCapture('http://10.0.0.107:port/1')

while(True):
    conectado, frame = video.read()
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()