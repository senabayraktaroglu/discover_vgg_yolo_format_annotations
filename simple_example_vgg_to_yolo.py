from skimage import io
import cv2
import json
bear_url = "https://www.wildlifeworldwide.com/images/categories/bearwatching_brown-bear-backlit_finland.jpg"
bear_image = io.imread(bear_url)

#cv2.imshow("bear_image",bear_image )
#cv2.waitKey()

vgg_format_label_bear = '{"x":99,"y":191,"width":405,"height":373}'
vgg_format_label_bear  = json.loads(vgg_format_label_bear ) 

##VGG format bbox can be described as 
# bbox[0]: top right x_coordinate(in pixels) of label 
# bbox[1]: top right y_coordinate(in pixels) of label 
# bbox[2]: width of label 
# bbox[3]: height of label 

vgg_format_bbox = [vgg_format_label_bear["x"],vgg_format_label_bear["y"],vgg_format_label_bear["width"],vgg_format_label_bear["height"]]

##Desired format of new bbox 
# bbox[0]: top right x_coordinate(in pixels) of label 
# bbox[1]: top right y_coordinate(in pixels) of label 
# bbox[2]: bottom left x_coordinate(in pixels) of label 
# bbox[3]: bottom left y_coordinate(in pixels) of label 
def convert_to_desired_type_bbox(vgg_bbox):
    bbox_new = [0,0,0,0]
    bbox_new[2] = vgg_bbox[0] + vgg_bbox[2]
    bbox_new[0] =  vgg_bbox[0]
    bbox_new[3] =  vgg_bbox[1] + vgg_bbox[3]
    bbox_new[1] = vgg_bbox[1] 
    return bbox_new

print(vgg_format_bbox)

desired_bbox = convert_to_desired_type_bbox(vgg_format_bbox)


print(desired_bbox)

def simple_visualization_vgg(image,bbox):
    max_x = bbox[2]
    min_x = bbox[0]
    max_y = bbox[3]
    min_y = bbox[1]
    x_rect= [min_x ,max_x ,max_x,min_x ]
    y_rect= [max_y,max_y,min_y,min_y]
    img= cv2.rectangle(image,(int(min_x),int(min_y)),(int(max_x),int(max_y)),(0,255,0),3)
    return img


### Convert it to yolo format 
# Desired bbox: x1,y1 (top right coordinate of bbox), x2,y2 (bottom left coordinate of bbox) 
# 1) Get center of image in terms of pixel values, (x_center,y_center)(in pixels)
#    - x1,y1 (top right coordinate of bbox), x2,y2 (bottom left coordinate of bbox)  
#    - x_center: x1 + ((x2-x1)/2), y_center: y1 + ((y2-y1)/2)   
#    - width_of_label : ((x2-x1)/2) , height_of_label : ((y2-y1)/2)  
#    - bbox_yolo =  x_center/image_width,y_center/image_height, width_of_label/image_width,height_of_label/image_height

def vgg_to_yolo_format_convert(desired_bbox,image_width,image_height):
    max_x = desired_bbox[2]
    min_x = desired_bbox[0]
    max_y = desired_bbox[3]
    min_y = desired_bbox[1]
    width_of_label = max_x-min_x
    height_of_label = max_y-min_y
    x_center = min_x+(width_of_label/2)
    y_center = min_y+(height_of_label/2)
    x_center_norm = x_center/image_width
    y_center_norm = y_center/image_height
    width_norm = width_of_label/image_width 
    height_norm = height_of_label/image_height

    return x_center_norm,y_center_norm,width_norm,height_norm

image_width,image_height,channels = bear_image.shape
yolo_label_bbox = vgg_to_yolo_format_convert(desired_bbox,image_width,image_height)
print(yolo_label_bbox)
img_vgg_labeled = simple_visualization_vgg(bear_image,desired_bbox)
cv2.imshow("with_label",img_vgg_labeled )
cv2.waitKey(0)
