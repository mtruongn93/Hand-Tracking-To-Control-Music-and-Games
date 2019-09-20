import numpy as np
import cv2
import pyautogui


#this is the cascade we just made. Call what you want
hand_cascade = cv2.CascadeClassifier('../cascade5.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.2, 5)

    for (x,y,w,h) in hands:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # pyautogui.moveTo(1920 - x*4, 1080 - y*2, duration = 0.5)

    cv2.imshow('img',img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
