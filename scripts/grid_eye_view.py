#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from GridEye import GridEye

myeye = GridEye()

temp_min = 20.
temp_max = 30.

img_edge = 256
img = np.zeros((img_edge, img_edge * 2, 3), np.uint8)

# np.set_printoptions(precision=1)

while(True):
    # print 'Thermistor Temp:', myeye.thermistorTemp()

    pixel = np.array(myeye.pixelOut())
    pixel.resize((8, 8))

    temp_min = temp_min * 0.9 + pixel.min() * 0.1
    temp_max = temp_max * 0.9 + pixel.max() * 0.1
    if temp_max < 30:
        temp_max = 30

    # print 'Pixel Out(Temp):'
    # print pixel

    pixel = pixel.clip(temp_min, temp_max)
    pixel = (pixel - temp_min) / (temp_max - temp_min) * 255.0
    pixel = pixel.astype(np.uint8)

    # print 'Pixel Out(0-255):'
    # print pixel

    pixel = cv2.applyColorMap(pixel, cv2.COLORMAP_JET)

    # 左側にコピー
    roi = img[:, :img_edge]
    cv2.resize(pixel, roi.shape[0:2], roi,
               interpolation=cv2.INTER_CUBIC)

    # 右側にコピー
    roi = img[:, img_edge:]
    cv2.resize(pixel, roi.shape[0:2], roi,
               interpolation=cv2.INTER_NEAREST)

    cv2.imshow('GridEyeView', img)
    if cv2.waitKey(100) == 27:  # ESC
        break

cv2.destroyAllWindows()
