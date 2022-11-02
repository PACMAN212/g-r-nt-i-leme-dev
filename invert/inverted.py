import cv2
import numpy as np
original_resim = cv2.imread("elmalar.jpg")
cv2.imshow("Orjinal Resim",original_resim)
gri_resim = cv2.imread('elmalar.jpg',0)
cv2.imshow("Gri Format",gri_resim)
[h,w] = gri_resim.shape
invert_resim = np.zeros([h,w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        invert_resim[i,j] = 255 - gri_resim[i,j]
cv2.imshow("Ters Cevirilmis",invert_resim)
cv2.waitKey()