from skimage import io
import cv2
import json
bear_url = "https://www.wildlifeworldwide.com/images/categories/bearwatching_brown-bear-backlit_finland.jpg"
bear_image = io.imread(bear_url)

#cv2.imshow("bear_image",bear_image )
#cv2.waitKey()

vgg_format_label_bear = '{"x":99,"y":191,"width":405,"height":373}'


vgg_format_label_bear  = json.loads(vgg_format_label_bear ) 

print(vgg_format_label_bear["x"])