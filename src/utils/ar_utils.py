```python
import cv2
import numpy as np

def create_ar_popup(image_path, popup_text):
    # Load the AR image
    image = cv2.imread(image_path)

    # Create the AR popup
    popup = np.zeros((300, 300, 3), dtype = "uint8")
    popup.fill(255)

    # Add the popup text
    cv2.putText(popup, popup_text, (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Display the AR popup on the image
    x_offset = 50
    y_offset = 50
    image[y_offset:y_offset+popup.shape[0], x_offset:x_offset+popup.shape[1]] = popup

    return image

def display_ar_popup(image_path, popup_text):
    # Create the AR popup
    image = create_ar_popup(image_path, popup_text)

    # Display the image with the AR popup
    cv2.imshow('AR Popup', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```