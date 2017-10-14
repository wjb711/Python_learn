import numpy as np
import cv2
from matplotlib import pyplot as plt

#scaling:
img = cv2.imread('lufugong.jpg')
rows, cols, channels = img.shape
res = cv2.resize(img, (cols/2, rows/2))

#Translation:

# 1.shift
M_shift = np.float32([[1,0,100],[0,1,50]])
img_shift = cv2.warpAffine(img, M_shift, (cols, rows))

# 2.rotate
M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
img_rotate = cv2.warpAffine(img, M_rotate, (cols, rows))

# 3.affine
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M_affine = cv2.getAffineTransform(pts1,pts2)
img_affine = cv2.warpAffine(img, M_affine, (cols, rows))

# 4.perspective
pts3 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts4 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M_perspective = cv2.getPerspectiveTransform(pts3,pts4)
img_perspective = cv2.warpPerspective(img, M_perspective, (cols, rows))

print 'shift:\n', M_shift
print 'rotate:\n', M_rotate
print 'affine:\n', M_affine
print 'perspective:\n', M_perspective

plt.subplot(231),plt.imshow(img),plt.title('src')
plt.subplot(232),plt.imshow(res),plt.title('scale')
plt.subplot(233),plt.imshow(img_shift),plt.title('shift')
plt.subplot(234),plt.imshow(img_rotate),plt.title('rotate')
plt.subplot(235),plt.imshow(img_affine),plt.title('affine')
plt.subplot(236),plt.imshow(img_perspective),plt.title('perspective')

plt.show()
