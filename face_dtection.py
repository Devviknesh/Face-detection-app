import cv2
import datetime

def detect_faces():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(frame, timestamp, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
        cv2.imshow('Face Detection', frame)
        
        key = cv2.waitKey(1)
        if key == ord('s'):
            filename = f"face_capture_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Image saved: {filename}")
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_faces()
