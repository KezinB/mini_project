import cv2
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

# Initialize PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
raw_capture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

# Main loop
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    img = frame.array  # Get the captured frame as an OpenCV image

    # Convert the frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection to detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Apply HoughLines to detect lines
    lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

    if lines is not None:
        for rho, theta in lines[:, 0]:
            # Convert polar coordinates to Cartesian coordinates
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho

            # Calculate start and end points of the line segment
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            # Draw the line on the original frame
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Line Detection', img)  # Display the processed frame

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  # Press 'q' to exit
        break

    raw_capture.truncate(0)  # Clear the buffer for next frame

cv2.destroyAllWindows()  # Close all OpenCV windows

