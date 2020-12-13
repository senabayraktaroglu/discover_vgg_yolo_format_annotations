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

bbox_new = convert_to_desired_type_bbox(vgg_format_bbox)


print(bbox_new)

def simple_visualization_vgg(image,bbox):
    max_x = bbox[2]
    min_x = bbox[0]
    max_y = bbox[3]
    min_y = bbox[1]
    x_rect= [min_x ,max_x ,max_x,min_x ]
    y_rect= [max_y,max_y,min_y,min_y]
    img= cv2.rectangle(image,(int(min_x),int(min_y)),(int(max_x),int(max_y)),(0,255,0),3)
    return img

img_vgg_labeled = simple_visualization_vgg(bear_image,bbox_new)
cv2.imshow("with_label",img_vgg_labeled )
cv2.waitKey(0)