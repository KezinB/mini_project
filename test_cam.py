import cv2

# Open the camera
cap = cv2.VideoCapture(0)  # 0 indicates the default camera (usually the camera module on a Raspberry Pi)

# Check if camera opened successfully
if not cap.isOpened():
    print("Failed to open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame was captured successfully
    if not ret:
        print("Failed to capture frame.")
        break

    # Display the captured frame
    cv2.imshow("Camera", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

