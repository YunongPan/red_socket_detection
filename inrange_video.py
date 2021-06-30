#!/usr/bin/env python
import cv2  
import numpy as np 
import time

cap = cv2.VideoCapture('2021-06-09-10-10-26_camera_color_image_raw.m4v')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('red_socket.avi',fourcc, 20.0, (width,height))


while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red_1 = np.array([170, 80, 150])
    upper_red_1 = np.array([180, 255, 255])
    mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)


    lower_red_2 = np.array([0, 80, 150])
    upper_red_2 = np.array([2, 255, 255])
    mask_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)

    mask_ges = mask_1 + mask_2

    res = cv2.bitwise_and(frame, frame, mask = mask_ges)
    img_Gaussian_res = cv2.GaussianBlur(res, (3, 3), 0)

    out.write(img_Gaussian_res)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', width, height)
    cv2.imshow('image', img_Gaussian_res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    time.sleep(.01)
cv2.destroyAllWindows()
cap.release()






