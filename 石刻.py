import numpy as np
import cv2
from scipy import ndimage


cap=cv2.VideoCapture(0)
while cv2.waitKey(1)!=ord('s'):
    ret, img=cap.read()
    #img = cv2.imread('apple.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    data = np.array(gray, dtype=float)


    kernel = np.array([[-9, 9, -9, ],
                       [ 9, 0,  9, ],
                       [-9, 9, -9, ]])
    highpass_5x5 = ndimage.convolve(data, kernel)

    cv2.imshow('Gambar Asli',img)
    cv2.imshow('High Pass Filter',highpass_5x5)

#cv2.waitKey(0)
cv2.destroyAllWindows()
