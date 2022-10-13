# %% - virstual drawing

import cv2
import numpy as np

print('starting video capture...')
cap = cv2.VideoCapture(0)

# screen dimensions
w, h = cap.get(3), cap.get(4)
print('video shape', w, h)

# calibrated from a color picker.
lower_blue = np.array([100,150,0])
upper_blue = np.array([140,255,255])
lower_green = np.array([40,150,0])
upper_green = np.array([80,255,255])

my_colors = {
    'blue':{'lower':lower_blue, 'upper':upper_blue, 'value':[255,0,0]},
    'green':{'lower':lower_green, 'upper':upper_green, 'value':[0,255,0]}}

my_points = []

def find_color(img, my_colors:dict):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    new_points = []
    for color in my_colors.keys():
        lower = np.array(my_colors[color]['lower'])
        upper = np.array(my_colors[color]['upper'])
        mask = cv2.inRange(img_hsv, lower, upper)
        x, y = get_contours(mask)
        c = my_colors[color]['value']
        cv2.circle(img_result, (x,y), 10 , c, cv2.FILLED)
        if x!=0 and y!=0:
            new_points.append([x,y,c])
        # cv2.imshow('image:'+color, mask)
    return new_points


def get_contours(img):
    contours, hierachy = cv2.findContours(img, 
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(img_result, cnt, -1, (0,0,255), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2, y + h//10

def draw_on_canvas(my_points):
    for p in my_points:
        cv2.circle(img_result, (p[0], p[1]), 10, p[2], cv2.FILLED)

    

while True:

    # break at the end
    done, img = cap.read()
    if done == False:
        break
    
    img_result = img.copy()
    new_points = find_color(img, my_colors)
    if len(new_points)!=0:
        for newp in new_points:
            my_points.append(newp)
    if len(my_points)!=0:
        draw_on_canvas(my_points)
    cv2.imshow('Video', img_result)

    # break if 'esc' or 'q' is pressed
    key = cv2.waitKey(1)
    if key==27 or key==113:
        break

print('done')
