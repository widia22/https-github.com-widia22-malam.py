import cv2
imgrgb =cv2.imread('yunanda.jpg')
imggray = cv2.imread('yunanda.jpg',0)
cv2.imshow ('Gambar RGB',imgrgb)

cv2.imshow('Gambar Gray',imggray)
cv2.waitKey()
