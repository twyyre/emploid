# import Scipy
# import sklearn
# import matplotlib
# import scikit-image
import numpy as np
from PIL import Image as img
import pyautogui as gui
import cv2 as cv
from emploid import Emploid
import matplotlib.pyplot as plt
import time
from statistics import mean
emp = Emploid()

image1 = cv.imread("elements/imgA.png")
image2 = cv.imread("elements/imgB.png")
image1 = emp.scale_to(image1, image2)
image1 = emp.convert_to_grayscale(image1)
image2 = emp.convert_to_grayscale(image2)
# hist = cv.calcHist(image1, [0], None, [256], [0, 256])
# print(hist)
# ssim = cv.compareHist(image1, image2, cv.CV_COMP_CHISQR  )

# print("ssim:", ssim)
# print("-------------------------------------------------------------------------------------------------------------------------------------------")
# print(image1)

# cv.imwrite("elements/imgC.png", image1)

# if(image1.shape == image2.shape):
#     pixel_count = 0
#     cell_count = 0
#     total_pixels = 0
#     total_cells = 0
#     for pixel1, pixel2, in zip(image1, image2):
#         total_pixels += 1
#         for cell1, cell2 in zip(pixel1, pixel2):
#             total_cells+=1
#             if(cell1==cell2):
#                 cell_count+=1
#                 count_pixel = True
#             else:
#                 count_pixel = False
#                 break
#         if(count_pixel):
#             pixel_count += 1    
#     print("pixel count:", pixel_count, "/", total_pixels)
#     print("cell count:", cell_count, "/", total_cells)
# else:
#     print("failure")

# image1 = cv.erode(image1)
# window = cv.namedWindow("mainWindow")

# while True:
#     cv.imshow("mainWindow", image1)
#     cv.imshow("mainWindow", image2)
#     if cv.waitKey(1) == ord('q'):
#         break
# convert the images to grayscale
# img1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
# img2 = cv.cvtColor(image3, cv.COLOR_BGR2GRAY)

# img_a_array = np.array(img1)
# img_b_array = np.array(img2)
# difference = (img_a_array == img_b_arra y).sum()
# pixel_num = img1.shape[0]*img1.shape[1]

# result = difference/pixel_num
# print(image1)
# print(image2)
# print(result)

# from PIL import Image
# import numpy as np
# ####
# import matplotlib.pyplot as plt
# ###
# i = Image.open('images/dotndot.png')

# iar = np.asarray(i)

# plt.imshow(iar)
# print(iar)
# plt.show()

# def threshold(imageArray):
#     balanceAr = []
#     newAr = imageArray
#     from statistics import mean

#     for eachPix in imageArray:
#         avgNum = mean(eachPix[:3])
#         balanceAr.append(avgNum)

#     balance = mean(balanceAr)

#     for eachPix in newAr:
#         if mean(eachPix[:3]) > balance:
#             eachPix[0] = 255
#             eachPix[1] = 255
#             eachPix[2] = 255
#             eachPix[3] = 255
#         else:
#             eachPix[0] = 0
#             eachPix[1] = 0
#             eachPix[2] = 0
#             eachPix[3] = 255
#     return newAr

# print(image1)
# image1 = threshold(image1)
# cv.imwrite("elements/imgC.png", image1)

# res = cv.matchTemplate(image2, image1, cv.TM_SQDIFF)


# image = []
# for row in image:
#     for pixel in row:
