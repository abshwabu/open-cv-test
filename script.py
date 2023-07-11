import cv2

img = cv2.imread('galaxy.jpg',0) #read the image

resize_image=cv2.resize(img,(1000,500))
show_galaxy = cv2.imshow('glaxy',resize_image) #show the image

cv2.waitKey(2000)
cv2.destroyAllWindows()