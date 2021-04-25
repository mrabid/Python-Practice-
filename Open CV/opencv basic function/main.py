import cv2
import numpy as np

kernal = np.ones((5,5),np.int8)
print(kernal)

path = "lena.png"
# img = cv2.imread(path,0)
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDilation,kernal,iterations=2)

cv2.imshow("Lena",img)
cv2.imshow("Gray Scale",imgGray)
cv2.imshow("Img Blur",imgBlur)
cv2.imshow("Img Canny",imgCanny)
cv2.imshow("Img Dilation",imgDilation)
cv2.imshow("img Erode", imgEroded)

cv2.waitKey(0)