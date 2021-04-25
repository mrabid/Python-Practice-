import cv2

frameWidth = 1080
frameHeight = 720

cap = cv2.VideoCapture("islamicSong.mp4")

while True:
    sucess,img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
