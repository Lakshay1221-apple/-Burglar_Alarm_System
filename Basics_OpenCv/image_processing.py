import cv2

im1 = cv2.imread('/home/lakshay/Theft_Detection_Open_Cv/flower_images/Lotus/0a4ffd9788.jpg')

resize = cv2.resize(im1, (500, 500))
grey = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
blurring = cv2.GaussianBlur(grey, (5, 5), 0)
edges = cv2.Canny(blurring, 100, 200)

cv2.imshow('image', edges)
cv2.waitKey(0)

