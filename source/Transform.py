import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(img_gray, 128, 255,
                                    cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.resizeWindow("frame", 200, 200)
    cv2.imshow('frame', im_bw)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
