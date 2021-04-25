import cv2

frameWidth = 1080
frameHeight = 720

cap = cv2.VideoCapture(0)
cap.set(5,frameWidth)
cap.set(6,frameHeight)

while True:
    sucess,img = cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
