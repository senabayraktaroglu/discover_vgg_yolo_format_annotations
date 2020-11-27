import cv2

path = 'adutta_swan.jpg'
  
# Using cv2.imread() method 
img = cv2.imread(path) 

cv2.imwrite('image_dene.jpg', img) 
