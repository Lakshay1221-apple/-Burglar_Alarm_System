import cv2
import os
from datetime import datetime

"""
Burglar Presence Detection using Frame Differencing

Algorithm:
1. Capture frames from webcam.
2. Convert each frame to grayscale.
3. Blur the image to reduce noise.
4. Compare the oldest and newest frame in a buffer.
5. Threshold the difference.
6. Find contours.
7. If a large contour is found, declare motion.
"""

CAMERA_INDEX = 0
FRAME_GAP = 10
MIN_CONTOUR_AREA = 1000
THRESHOLD = 30

SAVE_DIR = "detections"
os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 25)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

frames = []
frame_count = 0
motion_detected = False

print("Press 'q' to quit.")


while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame.")
        break

    display = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    frames.append(gray)

    if len(frames) > FRAME_GAP:
        frames.pop(0)

    cv2.putText(
        display,f"Frame: {frame_count}",(10, 30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0, 255, 0),2,)
    
    if len(frames) == FRAME_GAP:
        diff = cv2.absdiff(frames[0], frames[-1])
        _, thresh = cv2.threshold(diff,THRESHOLD,255,cv2.THRESH_BINARY,)

        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE,)

        motion = False

        for contour in contours:

            if cv2.contourArea(contour) < MIN_CONTOUR_AREA:
                continue

            motion = True

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(display,(x, y),(x + w, y + h),(0, 0, 255),2,)

        if motion:

            cv2.putText(display,"BURGLAR DETECTED!",(10, 70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,225),2,)

            if not motion_detected:

                filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")

                path = os.path.join(SAVE_DIR, filename)

                cv2.imwrite(path, display)

                print(f"[ALERT] Motion detected. Saved: {path}")

                motion_detected = True

        else:
            motion_detected = False

        cv2.imshow("Difference", diff)
        cv2.imshow("Threshold", thresh)

    cv2.imshow("Burglar Presence Detection", display)

    frame_count += 1

    key = cv2.waitKey(1)

    if key & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()