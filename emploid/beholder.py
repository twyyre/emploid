import numpy as np
import cv2 as cv
import pyautogui as pa
# from emp_taskman import Taskman

class Beholder:

    def __init__(self):
        # self.taskman = Taskman()
        self.beheld = None
        self.pause = False

    def behold(self):
        import pyautogui as pa
        import cv2 as cv
        import numpy as np

        SCREEN_SIZE = tuple(pa.size())
        # importing the required packages

        # Specify resolution
        resolution = (SCREEN_SIZE)

        # Specify video codec
        codec = cv.VideoWriter_fourcc(*"XVID")

        # Specify name of Output file
        from tools import get_time
        filename = f"recordings/{get_time()}.avi"

        # Specify frames rate. We can choose any
        # value and experiment with it
        fps = 30.0

        # Creating a VideoWriter object
        self.beheld = cv.VideoWriter(filename, codec, fps, resolution)

        # Create an Empty window
        # cv.namedWindow("Live", cv.WINDOW_NORMAL)

        # Resize this window
        # cv.resizeWindow("Live", 480, 270)

        while True:
            
            if(self.pause):
                continue
            
            img = pa.screenshot()
            # Convert the screenshot to a numpy array
            frame = np.array(img)
            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            # Write it to the output file
            self.beheld.write(frame)
            # Optional: Display the recording screen
            # cv.imshow('Live', frame)
            
            # Stop recording when we press 'q'
            # if cv.waitKey(1) == ord('q'):
            #     break

    def blink(self_):
        pass

    def hold(self):
        self.pause = True

    def resume(self):
        self.pause = False

    def shut(self):
        # Release the Video writer
        self.beheld.release()

        # Destroy all windows
        cv.destroyAllWindows()
        pass