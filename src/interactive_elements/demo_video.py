```python
import cv2

class DemoVideo:
    def __init__(self, video_path):
        self.video_path = video_path

    def play_video(self):
        cap = cv2.VideoCapture(self.video_path)

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Demo Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

demo_video = DemoVideo('path_to_demo_video.mp4')
demo_video.play_video()
```