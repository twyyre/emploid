import cv2
import numpy as np

# Load the main image and the template
main_image = cv2.imread('haystack.png')
template = cv2.imread('needle.png')

# Convert images to grayscale
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Use template matching
result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Set a threshold to determine a match
threshold = 0.8
loc = np.where(result >= threshold)

# Draw rectangles around the matched areas
for pt in zip(*loc[::-1]):
    cv2.rectangle(main_image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

# Display the result
cv2.imshow('Matching Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
