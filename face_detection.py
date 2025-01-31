import cv2  # OpenCV library for computer vision

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the image (change 'test_image.jpg' to your image file)
image = cv2.imread("test_image.jpg")

# Convert image to grayscale (needed for better face detection)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the output image with detected faces
cv2.imshow("Face Detection", image)
cv2.waitKey(0)  # Wait for user input before closing
cv2.destroyAllWindows()
