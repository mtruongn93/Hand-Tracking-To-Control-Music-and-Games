import vlc
import cv2
from imutils.video import WebcamVideoStream

player = vlc.MediaPlayer("song.mp3")
hand_cascade = cv2.CascadeClassifier('../cascade5.xml')
# cap = cv2.VideoCapture(0)
cap = WebcamVideoStream(src = 0).start()


player.play()
while True:
    # ret, img = cap.read()
    img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.1, 7)

    for (x,y,w,h) in hands:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if x < 510/4 and player.is_playing() !=0:
            player.pause()
        elif x >=510/4:
            player.play()

    cv2.imshow('img',img)
    k = cv2.waitKey(1)
    if k == 27:
        break

# cap.release()
cv2.destroyAllWindows()
cap.stop()
