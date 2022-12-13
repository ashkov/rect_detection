import resource

import cv2
import numpy as np


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


def main():
    hsv_colors = {
        'gray': [[0, 0, 120], [0, 0, 140]],
        'black': [[0, 0, 0], [0, 0, 10]],
        'orange': [[18, 40, 90], [27, 255, 255]],
        'red': [[0, 200, 200], [10, 255, 255]],
        'pink': [[140, 200, 200], [170, 255, 255]],
        'yellow': [[25, 50, 70], [35, 255, 255]],
        'green': [[40, 50, 70], [70, 255, 255]],
        'blue': [[110, 50, 70], [130, 255, 255]],

    }
    img = cv2.imread("img.png")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    del img
    colors = {}
    for key, hc in hsv_colors.items():
        print(key)
        hsv_min = np.array(hc[0], np.uint8)
        hsv_max = np.array(hc[1], np.uint8)
        filtered = cv2.inRange(hsv, hsv_min, hsv_max)
        cv2.imshow("s", filtered)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        contours = cv2.findContours(filtered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
        for cnt in contours:
            # x1, y1 = cnt[0][0]
            # approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            # if len(approx) > 0:
            #     x, y, w, h = cv2.boundingRect(cnt)
            #     color = (img[y + int(h / 2), x + int(w / 2)])
            #     if np.array_equal([255, 255, 255], color):
            #         continue

            if not key in colors:
                colors[key] = 1
            else:
                colors[key] += 1
                # cv2.putText(img, key + str(len(approx)), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                # img = cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)
    color_max = None
    color_min = None
    count_max = None
    count_min = None

    for color in sorted(["gray", "black", "orange", "red", "pink", "yellow", "green", "blue"], reverse=True):
        if count_max is None or colors[color] >= count_max:
            count_max = colors[color]
            color_max = color
        if count_min is None or colors[color] <= count_min:
            count_min = colors[color]
            color_min = color
    print(colors, color_min, count_min, color_max, count_max)


if __name__ == "__main__":
    # limit_memory(1024 * 1024 * 1024)
    main()
