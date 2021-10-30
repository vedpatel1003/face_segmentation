import cv2
import time
import numpy as np
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


# For static images:
IMAGE_FILES = []
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
    for idx, file in enumerate(IMAGE_FILES):
        image = cv2.imread(file)
        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    #path
    path = r'C:\Users\Admin\Desktop\projects\face_segmentation\2201.jpg'

    # Reading an image in default mode
    image = cv2.imread(path)

    # Window name in which image is displayed
    window_name = 'Image'

    # Start coordinate, here (0, 0)
    # represents the top left corner of image
    start_point = (0, 0)

    # End coordinate, here (250, 250)
    # represents the bottom right corner of image
    end_point = (150, 50)

    # Green color in BGR
    color = (0, 255, 0)

    # Line thickness of 9 px
    thickness = 9

    # Using cv2.line() method
    # Draw a diagonal green line with thickness of 9 px
    image = cv2.line(image, start_point, end_point, color, thickness)

    # Displaying the image
    cv2.imshow(window_name, image)

window_name = "preview"
cv2.namedWindow(window_name)  #, cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    # Frame change
    # Center coordinates
    center_coordinates = (120, 100)
    # center_coordinates = (int(np.random.uniform(0, 500))), int(np.random.uniform(0, 500))

    # Radius of circle
    radius = 30

    # Red color in BGR
    color = (0, 0, 255)

    # Line thickness of -1 px
    thickness = -1

    # Using cv2.circle() method
    # Draw a circle of red color of thickness -1 px
    frame = cv2.circle(frame, center_coordinates, radius, color, thickness)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")