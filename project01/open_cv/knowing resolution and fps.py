import cv2

# Open the camera (0 is usually the default camera)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
else:
    # Get the width and height of the video frame
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    # Get the frames per second (FPS)
    fps = camera.get(cv2.CAP_PROP_FPS)
    
    print(f"Resolution: {int(width)}x{int(height)}")
    print(f"FPS: {fps}")

# Release the camera
camera.release()
cv2.destroyAllWindows()
