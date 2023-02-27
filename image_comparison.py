#https://www.tutorialspoint.com/how-to-compare-two-images-in-opencv-python#:~:text=To%20compare%20two%20images%2C%20we,width%20and%20number%20of%20channels.
import cv2
import numpy as np
img1 = cv2.imread('velms/signin_btn.png')
img2 = cv2.imread('velms/signin_btn2.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Define a function to compute the Mean Squared Error between two images.
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse

#Compute the Mean Squared Error (Matching error) between the images.
error = mse(img1, img2)

#Print the image matching error (mse) and display the image difference.
print("Image matching Error between the two images:", mse)
cv2.imshow("Contour", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Print the result value, the image shape matching metric. The lower the value, the better matching it is.
print("Matching Image 1 with Image 2:", error)

