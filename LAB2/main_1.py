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


intensity_list = {}

for row in range(height):
    for col in range(width):
        pixel = mat[row,col][0]
        if intensity_list.get(pixel,None):
            intensity_list[pixel] += 1
        else:
            intensity_list[pixel] = 1
for intensity in range(256):
    print("{}:{}".format(intensity,intensity_list.get(intensity,0)))


n = width*height
accum_func = {-1:0}
for x in range(256):
    accum_func[x] = (accum_func[x-1] + intensity_list.get(x,0))
for intensity in range(256):
    print("{}:{}".format(intensity, accum_func.get(intensity,0)/n))

for row in range(height):
    for col in range(width):
        new_intensity = mat[row][col][0]
        new_intensity = accum_func[new_intensity]*255/n
        mat[row,col] = (new_intensity,new_intensity,new_intensity)
window = cv2.namedWindow("wow",0)
cv2.imshow("wow", mat)
cv2.waitKey(0)
cv2.destroyAllWindows()
