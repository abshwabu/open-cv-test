import cv2

img = cv2.imread('galaxy.jpg',0) #read the image

show_galaxy = cv2.imshow('glaxy',img) #show the image

cv2.waitKey(2000)
cv2.destroyAllWindows()