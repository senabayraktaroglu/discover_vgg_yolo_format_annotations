import cv2
import numpy as np
path = 'adutta_swan.jpg'
  

def make_x_y_as_pts(x,y):
    pts_dene = []
    for i in range(len(x)):
        temp = [x[i],y[i]]
        pts_dene.append(temp) 
    pts_dene= np.asarray(pts_dene)
    return pts_dene

def draw_polyline_vgg(img,pts_dene):
    pts_dene = pts_dene.reshape((-1,1,2))
    cv2.polylines(img,[pts_dene],True,(255, 0, 0))
    return img 

#trying to draw polyline 
x = [116,94,176,343,383,385,369,406,398,364,310,297,304,244,158]
y = [157,195,264,273,261,234,222,216,155,124,135,170,188,170,175]

pts_dene = make_x_y_as_pts(x,y)


img = cv2.imread(path)

cv2.imwrite('image_dene.jpg', img) 