import cv2
from PIL import Image

from util import get_limits


colors = {
    'yellow': [0, 255, 255],
    'blue': [255, 0, 0],
    'green': [0, 255, 0]
}
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, color_bgr in colors.items():
        lowerLimit, upperLimit = get_limits(color=color_bgr)

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox

            # Draw rectangle in the detected color
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), color_bgr, 5)
            
            # Put text label above the rectangle
            cv2.putText(frame, color_name.capitalize(), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color_bgr, 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

