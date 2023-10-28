```python
import cv2
import numpy as np

class EyeTracking:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    def detect_eyes(self, img, cascade):
        gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = cascade.detectMultiScale(gray_frame, 1.3, 5) 
        for (x,y,w,h) in eyes:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        return img

    def detect_faces(self, img, cascade):
        gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray_frame, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        return img

    def capture_video(self):
        while True:
            ret, frame = self.cap.read()
            frame = self.detect_faces(frame, self.face_cascade)
            frame = self.detect_eyes(frame, self.eye_cascade)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    eye_tracking = EyeTracking()
    eye_tracking.capture_video()

if __name__ == "__main__":
    main()
```