import cv2
import numpy as np
import matplotlib.pyplot as plt
#orjinal görseli göstermek--------------------------------
img = cv2.imread("elmalar.jpg")
original=img.shape
cv2.imshow('orjinal resim', img)

#gri hali göstermek---------------------------------------
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('resimin gri hali', img_gray)

#döngü ile histogram hesaplamak--------------------------
Histo = np.zeros(shape=(256, 1))
for i in range(original[0]):
    for j in range(original[1]):
        k = img_gray[i, j]
        Histo[k, 0] = Histo[k, 0] + 1
plt.plot(Histo)
plt.show()
cv2.waitKey(0)