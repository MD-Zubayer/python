import os
os.environ["QT_QPA_PLATFORM"] = "offscreen"

import cv2

image = cv2.imread('images.png')

print('original shape: ', image.shape)
print('data type: ', type(image))

resized_img = cv2.resize(image, (600,400))
cv2.imshow('resized',resized_img)
