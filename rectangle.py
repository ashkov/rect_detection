import cv2
import numpy as np

base_colors = {
    (255, 0, 0): "blue",
    (127, 127, 127): "gray",
    (0, 165, 255): "orange",
    (0, 0, 0): "black",
    (0, 255, 255): "yellow",
    (255, 0, 255): "pink",
    (0, 255, 0): "green",
    (0, 0, 255): "red"
}
img = cv2.imread("img.jpg")
threshold = 100
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("s", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("s", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
colors = {}
for cnt in contours:
    x1, y1 = cnt[0][0]
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    if len(approx) > 0:
        x, y, w, h = cv2.boundingRect(cnt)
        color = (img[y + int(h / 2), x + int(w / 2)])
        if np.array_equal([255, 255, 255], color):
            continue
        for bck in base_colors.keys():
            if all(np.isclose(np.asarray(bck), color, atol=1.0)):
                color_str = base_colors[bck]
                break
                # color_str = "_".join([str(c) for c in color])
        if not color_str in colors:
            colors[color_str] = 1
        else:
            colors[color_str] += 1
        cv2.putText(img, color_str, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        img = cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(colors)
