import cv2
import time

mat = cv2.imread("/Users/hackintosh/Desktop/IMG_0086.jpg")
window = cv2.namedWindow("wow",0)
cv2.imshow("wow", mat)
cv2.waitKey(0)
cv2.destroyAllWindows()

