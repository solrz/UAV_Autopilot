import cv2
import time

mat = cv2.imread("/Users/hackintosh/Desktop/IMG_0086.jpg")
RESET = 0
width, height = mat.shape[:2]
for row in range(height):
    for col in range(width):
        sum_pixel = sum(mat[row,col]) / 3
        '''
        print(sum_pixel)
        print(pixel)
        print(sum(pixel))
        '''
        mat[row,col] = (sum_pixel,sum_pixel,sum_pixel)


print(mat[0][0])
window = cv2.namedWindow("wow",0)
cv2.imshow("wow", mat)
cv2.waitKey(0)
cv2.destroyAllWindows()

