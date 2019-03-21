import cv2
import os

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Start capturing video
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('E:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')

# For each person, one face id
face_id = 1

assure_path_exists("E:\\projects\\python-ai-scripts\\Face_Recognition\\dataset\\" +str(face_id)+ "\\") 

# Initialize sample face image
count = len(os.listdir("E:\\projects\\python-ai-scripts\\Face_Recognition\\dataset\\" + str(face_id)))
initcount=count

# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    # Loops for each faces
    for (x, y, w, h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("E:\\projects\\python-ai-scripts\\Face_Recognition\\dataset\\"+str(face_id)+"\\User." + str(face_id) + '.' +
                    str(count) + ".jpg", gray[y:y+h, x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count > initcount + 100:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
