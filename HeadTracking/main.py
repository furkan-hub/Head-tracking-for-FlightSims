import cv2
import pyautogui
import threading

pyautogui.FAILSAFE = False

# Load the CascadeClassifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the camera (0 represents the built-in camera)
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()

# Move the mouse cursor to a specific point
target_x = screen_width // 2
target_y = screen_height // 2
pyautogui.moveTo(target_x, target_y, duration=0)  # Movement duration is 1 second
pyautogui.mouseDown(button='right')

x_0 = 0
y_0 = 0 
x = 0
y = 0
counter = False
counter2 = False

def calc_x_y():
    global x_0, y_0, x, y, counter2
    while True:
        pyautogui.move(-x+x_0, y-y_0, duration=0)
        if counter2:
            break

t1 = threading.Thread(target=calc_x_y)
t1.start()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        if counter == False:
            x_0 = x
            y_0 = y
            counter = True
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the results
    cv2.imshow('Face Tracking', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        counter2 = True
        break

# Perform necessary cleanup
cap.release()
cv2.destroyAllWindows()
