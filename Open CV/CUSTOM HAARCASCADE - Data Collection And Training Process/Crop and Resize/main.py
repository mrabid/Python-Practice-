import cv2

path = "picture.jpg"
img = cv2.imread(path)

print(img.shape)

width, height = 540, 900
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)

imgCroped = imgResize[200:440,330:380]
imCropeResize = cv2.resize(imgCroped,(img.shape[1],img.shape[0]))

cv2.imshow("Picture",img)
cv2.imshow("Picture Resize",imgResize)
cv2.imshow("Picture Croped",imgCroped)
cv2.imshow("Picture Crop Resize",imCropeResize)

cv2.waitKey(0)