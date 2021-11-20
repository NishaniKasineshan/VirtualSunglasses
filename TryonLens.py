import cv2
import  cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
num=1

while True:
    k=cv2.waitKey(100)
    if k==ord('s'):
        num=num+1
    #print(num)    
    if(num<=29):
            overlay = cv2.imread('Glasses/glass{}.png'.format(num), cv2.IMREAD_UNCHANGED)
         
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay,(w,int(h*0.8)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
    cv2.imshow('SnapLens', frame)
    if cv2.waitKey(10) == ord('q') or num>29:
        break
  
cap.release()
cv2.destroyAllWindows()
