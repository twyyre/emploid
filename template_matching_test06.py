import cv2 as cv
import numpy as np

def find_template(template_path, main_image_path, threshold=0.8):
    # Load images
    template = cv.imread(template_path, cv.IMREAD_GRAYSCALE)
    main_image = cv.imread(main_image_path)

    # Convert main image to grayscale if it's in color
    if len(main_image.shape) > 2:
        main_image_gray = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
    else:
        main_image_gray = main_image

    # Perform template matching
    result = cv.matchTemplate(main_image_gray, template, cv.TM_CCOEFF_NORMED)

    # Find the location of the best match
    _, max_val, _, max_loc = cv.minMaxLoc(result)

    print("accuracy:", max_val)

    # Check if the match is above the threshold
    if max_val >= threshold:
        return max_loc, result, template
    else:
        return None
    
haystacks = [
    "haystack.png",
    "haystack02.png",
    "haystack03.png",
    "haystack04.png",
    "haystack05.png",
    "haystack06.png",
]

# Example usage
for haystack_path in haystacks:
    print("--------------------------------------haystack:", haystacks.index(haystack_path))
    template_path = 'needle.png'
    main_image_path = haystack_path
    threshold = 0.9
    unpacked = find_template(template_path, main_image_path, threshold=threshold)
    if(unpacked is not None):
        template_location, result, template = unpacked
        if template_location is not None and result is not None and template is not None:
            print("Template found at (x, y):", template_location)

            # Draw a rectangle around the detected template
            h, w = template.shape[:2]
            top_left = template_location
            bottom_right = (top_left[0] + w, top_left[1] + h)

            # Read the image again in color to draw rectangles
            haystack = cv.imread(main_image_path)

            # Draw rectangle on the image
            cv.rectangle(haystack, top_left, bottom_right, (0, 0, 255), 2)

            # Show the image
            cv.imshow("Detected Template", haystack)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            pass
            #raise Exception("Template not found or below accuracy threshold.")

        
