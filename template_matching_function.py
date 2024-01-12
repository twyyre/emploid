import cv2 as cv
def detect_template(_needle, _haystack, _method=cv.TM_CCOEFF_NORMED, _threshold = 0.5):
    template = _needle
    haystack = _haystack
    method= _method
    threshold = _threshold
    # Convert main image to grayscale if it's in color
    # if len(main_image.shape) > 2:
    #     main_image_gray = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
    # else:
    #     main_image_gray = main_image

    # Perform template matching
    result = cv.matchTemplate(haystack, _needle, method)

    # Find the location of the best match
    _, max_val, _, max_loc = cv.minMaxLoc(result)

    print("accuracy:", max_val)

    # Check if the match is above the threshold
    if max_val >= threshold:
        # return max_loc, result, template
        return_template = True
    else:
        return_template = False
    
    if(return_template):
        template_location = max_loc
        result = result
        template = template
        if template_location is not None and result is not None and template is not None:
            print("Template found at (x, y):", template_location)

            # Draw a rectangle around the detected template
            h, w = template.shape[:2]
            top_left = template_location
            bottom_right = (top_left[0] + w, top_left[1] + h)
        else:
            pass
            #raise Exception("Template not found or below accuracy threshold.")
    

template = cv.imread("needle.png", cv.IMREAD_GRAYSCALE)
main_image = cv.imread("haystack.png", cv.IMREAD_GRAYSCALE)

detect_template(template, main_image)