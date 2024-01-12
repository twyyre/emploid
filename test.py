import win32gui
import win32con
from PIL import ImageGrab
import time

# Function to draw an image on the screen
def draw_image(image_path, x, y):
    # Load the image
    image = ImageGrab.grab(bbox=(0, 0, 800, 600))  # Adjust the coordinates as needed
    image = image.convert("RGB")

    # Get the screen device context
    hdc = win32gui.GetDC(0)

    # Create a compatible DC
    mem_dc = win32gui.CreateCompatibleDC(hdc)

    # Create a bitmap compatible with the screen DC
    bmp = win32gui.CreateCompatibleBitmap(hdc, image.width, image.height)

    # Select the bitmap into the memory DC
    win32gui.SelectObject(mem_dc, bmp)

    # Draw the image onto the memory DC
    win32gui.BitBlt(mem_dc, 0, 0, image.width, image.height, hdc, x, y, win32con.SRCCOPY)

    # Clean up resources
    win32gui.DeleteObject(bmp)
    win32gui.DeleteDC(mem_dc)
    win32gui.ReleaseDC(0, hdc)

# Example usage
try:
    while True:
        draw_image("path/to/your/image.png", 100, 100)  # Adjust the image path and coordinates
        time.sleep(1)  # Adjust the delay based on your preference
except KeyboardInterrupt:
    pass
