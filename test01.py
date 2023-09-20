import cv2
import numpy as np
from PIL import Image, ImageGrab

img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
print(img.size[1], img.size[0])
img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
print(img)
cv2.imwrite('screenshot.jpg', img)
