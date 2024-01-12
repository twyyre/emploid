import cv2
import numpy as np

def match_template(_needle, _haystack, _method):
    

    def multi_scale_template_matching(main_image, template, _needle=_needle, _haystack=_haystack, _method=_method):
        # Convert images to grayscale
        main_image = cv2.imread(_haystack)
        template = cv2.imread(_needle)

        main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Initialize a list to store the results at different scales
        results = []

        # Define a range of scales to consider
        scales = np.linspace(0.2, 1.0, 10)[::-1]

        for scale in scales:
            # Resize the template
            resized_template = cv2.resize(template_gray, (0, 0), fx=scale, fy=scale)

            # Use template matching
            result = cv2.matchTemplate(main_gray, resized_template, _method)

            # Find the location of the best match
            _, _, _, max_loc = cv2.minMaxLoc(result)

            # Store the results along with the scale
            results.append((scale, max_loc, result[max_loc[1], max_loc[0]]))

        # Select the result with the highest correlation score
        best_result = max(results, key=lambda x: x[2])

        # Extract the relevant information
        best_scale, best_loc, _ = best_result

        # Calculate the size of the template in the original image
        h, w = template_gray.shape
        best_size = (int(w * best_scale), int(h * best_scale))

        # Draw a rectangle around the matched area
        cv2.rectangle(main_image, best_loc, (best_loc[0] + best_size[0], best_loc[1] + best_size[1]), (0, 255, 0), 2)

        threshold_percentage = 0.3799999999999999
        
        # Get the correlation coefficient (similarity measure)
        correlation_coefficient = result[max_loc[1], max_loc[0]]

        # Check if the correlation coefficient is above the threshold
        if correlation_coefficient <= threshold_percentage:
            print(f"Template found with similarity: {correlation_coefficient}")
            return correlation_coefficient, main_image
        else:
            raise Exception(f"threshold ({correlation_coefficient}) is higher than {threshold_percentage}")
            return None

    # Load the main image and the template
    haystack = cv2.imread('elements/haystack.png')
    needle = cv2.imread('elements/needle.png')

    percentage, result_image = multi_scale_template_matching(haystack, needle)
    # Display the result
    cv2.imshow(f'haystack01 ({percentage})', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# 3 out of 4
print("--------------------cv2.TM_CCOEFF_NORMED")
print("haystack01")
match_template(_needle='elements/needle.png', _haystack='elements/haystack01.png', _method=cv2.TM_CCOEFF_NORMED) #this should be 100% match
print("haystack02")
match_template(_needle='elements/needle.png', _haystack='elements/haystack02.png', _method=cv2.TM_CCOEFF_NORMED)
print("haystack03")
match_template(_needle='elements/needle.png', _haystack='elements/haystack03.png', _method=cv2.TM_CCOEFF_NORMED)
print("haystack04")
match_template(_needle='elements/needle.png', _haystack='elements/haystack04.png', _method=cv2.TM_CCOEFF_NORMED)
print("haystack05")
match_template(_needle='elements/needle.png', _haystack='elements/haystack05.png', _method=cv2.TM_CCOEFF_NORMED)
print("haystack06")
match_template(_needle='elements/needle.png', _haystack='elements/haystack06.png', _method=cv2.TM_CCOEFF_NORMED)
print("haystack07")
match_template(_needle='elements/needle.png', _haystack='elements/haystack07.png', _method=cv2.TM_CCOEFF_NORMED)
print("haystack08")
match_template(_needle='elements/needle.png', _haystack='elements/haystack08.png', _method=cv2.TM_CCOEFF_NORMED)
