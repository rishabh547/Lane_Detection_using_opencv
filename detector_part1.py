import matplotlib.pylab as plt
import cv2
import numpy as np #first we do lane detection with image and then move to videos

image = cv2.imread('C:/opencv_github_files/opencv_python/samples/data//road.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape) #gives 3 members, no of channels of colur is at index[2]
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [ #this is what we need ignoring the left lane , a triangle region
    (0, height),
    (width/2, height/2),
    (width, height)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img) #returns an array with all values as zero
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count #refer video comments or video
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image #this is the region we get 

cropped_image = region_of_interest(image,
                np.array([region_of_interest_vertices], np.int32),)

plt.imshow(cropped_image)
plt.show()