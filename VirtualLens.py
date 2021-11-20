import cv2
import  cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

num=1
count=0
while True:  
    if(num<=29):
            overlay = cv2.imread('Glasses/glass{}.png'.format(num), cv2.IMREAD_UNCHANGED)
         
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        roi_gray=gray_scale[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        overlay_resize = cv2.resize(overlay,(w,int(h*0.8)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
        if(len(eyes)>=2):
            continue
        else:
            count+=1
            print(str(count)+": Blink Detected")
            if(count==5):
                num+=1
                count=0
            cv2.waitKey(1000)
            break
            
            
    cv2.imshow('SnapLens', frame)
    if cv2.waitKey(10) == ord('q') or num>29:
        break   
cap.release()
cv2.destroyAllWindows()
