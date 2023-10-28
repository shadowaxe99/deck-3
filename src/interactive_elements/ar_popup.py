```python
import cv2
import numpy as np

class ARPopup:
    def __init__(self):
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        self.parameters = cv2.aruco.DetectorParameters_create()

    def create_marker(self):
        marker_image = np.zeros((200, 200), dtype=np.uint8)
        marker_image = cv2.aruco.drawMarker(self.aruco_dict, 33, 200, marker_image, 1)
        cv2.imwrite("marker33.png", marker_image)

    def detect_marker(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, self.aruco_dict, parameters=self.parameters)
        return corners, ids

    def draw_popup(self, frame, corners, ids):
        if np.all(ids != None):
            for i in range(0, ids.size):
                if ids[i] == 33:
                    cv2.aruco.drawDetectedMarkers(frame, corners)
                    rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, self.camera_matrix, self.dist)
                    self.draw_vault(frame, rvec, tvec)
        return frame

    def draw_vault(self, frame, rvec, tvec):
        # Load the vault 3D model
        vault = cv2.imread('vault.png', -1)
        # Draw the vault model on the frame
        frame = cv2.warpPerspective(vault, rvec, (frame.shape[1], frame.shape[0]), frame, borderMode=cv2.BORDER_TRANSPARENT)
        return frame

    def run(self):
        self.create_marker()
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            corners, ids = self.detect_marker(frame)
            frame = self.draw_popup(frame, corners, ids)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    ar_popup = ARPopup()
    ar_popup.run()
```