import cv2

img = cv2.imread('galaxy.jpg',0) #read the image

hight = img.shape[1]
width = img.shape[0]

resize_image=cv2.resize(img,(int(hight/2),int(width/2)))
show_galaxy = cv2.imshow('glaxy',resize_image) #show the image

cv2.waitKey(2000)
cv2.destroyAllWindows()