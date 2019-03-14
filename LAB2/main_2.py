import numpy as np
import cv2


def get_item(arr, *args):
    indexes = []
    for i, entry in enumerate(args):
        index = entry
        if index < 0:
            index = abs(index) - 1
        if index >= arr.shape[i]:
            index = arr.shape[i] - index % arr.shape[i] - 1
        indexes.append(index)
    r = arr
    for index in indexes:
        r = r[index]
    return r


def get_w(x):
    a = -0.5
    absx = abs(x)
    if absx <= 1:
        return (a + 2) * absx**3 - (a + 3) * absx ** 2 + 1
    elif 1 < absx < 2:
        return a * absx**3 - 5 * a * absx**2 + 8 * a * absx - 4 * a
    else:
        return 0


im_mat = cv2.imread("/Users/hackintosh/Desktop/IMG_0086.jpg")
width, height, tunnel = im_mat.shape[:3]

im_mat_resized = np.empty((width*4, height*4, tunnel), dtype=np.uint8)

for r in range(im_mat_resized.shape[0]):
    for c in range(im_mat_resized.shape[1]):
        rr = (r + 1) / im_mat_resized.shape[0] * im_mat.shape[0] - 1
        cc = (c + 1) / im_mat_resized.shape[1] * im_mat.shape[1] - 1

        rr_int = int(rr)
        cc_int = int(cc)

        sum_p = np.empty(im_mat.shape[2])
        for j in range(rr_int - 1, rr_int + 3):
            for i in range(cc_int - 1, cc_int + 3):
                w = get_w(rr - j) * get_w(cc - i)
                p = get_item(im_mat, j, i) * w
                sum_p += p

        for i, entry in enumerate(sum_p):
            sum_p[i] = min(max(entry, 0), 255)

        im_mat_resized[r][c] = sum_p

cv2.imshow(cv2.namedWindow("wow",0),im_mat_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
