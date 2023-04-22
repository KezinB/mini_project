import cv2

cap = cv2.VideoCapture(0)  # Initialize camera capture

while True:
    ret, frame = cap.read()  # Capture a frame from the camera

    if ret:  # If a frame was successfully captured
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale

       # cv2.imshow('Original', frame)  # Display the original frame
        cv2.imshow('Grayscale', gray)  # Display the grayscale frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all windows

