import cv2

# Connect to laptop webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera not detected!")
    exit()

print("Camera connected successfully!")

while True:

    # Capture video frame
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture video")
        break

    # Display live camera
    cv2.imshow("AI Attendance System - Camera Test", frame)

    # Press Q to close camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
camera.release()
cv2.destroyAllWindows()

print("Camera disconnected!")