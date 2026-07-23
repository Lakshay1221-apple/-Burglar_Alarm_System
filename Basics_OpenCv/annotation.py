import cv2
import numpy as np 

canvas = np.zeros((512, 512, 3), dtype="uint8")

cv2.line(canvas, (0, 0), (512, 512), (255, 0, 0), 5)

cv2.imshow("Canvas with shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()