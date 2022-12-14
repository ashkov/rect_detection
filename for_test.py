import cv2
import numpy as np

hsv_colors = {
    'gray': [[0, 0, 125], [0, 0, 129]],
    'black': [[0, 0, 0], [0, 0, 0]],
    'orange': [[18, 245, 245], [20, 255, 255]],
    'red': [[0, 245, 245], [5, 255, 255]],
    'pink': [[145, 245, 245], [155, 255, 255]],
    'yellow': [[28, 245, 245], [32, 255, 255]],
    'green': [[58, 245, 245], [62, 255, 255]],
    'blue': [[118, 245, 245], [122, 255, 255]],

}
if not 'img' in locals():
    home = True
    img = cv2.imread("img1.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
del img
colors = {}
for key, hc in hsv_colors.items():
    hsv_min = np.array(hc[0], np.uint8)
    hsv_max = np.array(hc[1], np.uint8)
    filtered = cv2.inRange(hsv, hsv_min, hsv_max)
    contours = cv2.findContours(filtered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
    for cnt in contours:
        if not key in colors:
            colors[key] = 1
        else:
            colors[key] += 1
color_max = None
color_min = None
count_max = None
count_min = None

for color in sorted(["gray", "black", "orange", "red", "pink", "yellow", "green", "blue"], reverse=True):
    if not color in colors:
        continue

    if count_max is None or colors[color] >= count_max:
        count_max = colors[color]
        color_max = color
    if count_min is None or colors[color] <= count_min:
        count_min = colors[color]
        color_min = color
if 'home' in locals():
    print(colors)
    print(f"color_min={color_min}, count_min={count_min}, color_max={color_max}, count_max={count_max}")