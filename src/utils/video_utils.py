```python
import cv2

def play_demo_video(video_path):
    """
    Function to play a demo video.
    """
    cap = cv2.VideoCapture(video_path)

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

def save_demo_video(frames, output_path):
    """
    Function to save a demo video.
    """
    height, width, _ = frames[0].shape
    size = (width,height)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    
    for i in range(len(frames)):
        out.write(frames[i])
    out.release()
```