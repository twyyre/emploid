import cv2
import numpy as np 

# load the input images
img1 = cv2.imread('velms/signin_btn.png')
img2 = cv2.imread('velms/signin_btn2.png')

# convert the images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img_a_array = np.array(img1)
img_b_array = np.array(img2)
difference = (img_a_array == img_b_array).sum()
pixel_num = img1.shape[0]*img1.shape[1]
print(difference/pixel_num)