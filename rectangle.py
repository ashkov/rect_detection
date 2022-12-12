import cv2

img = cv2.imread("img.jpg")
threshold = 100
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("s", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
cv2.imshow("s", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x1, y1 = cnt[0][0]
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        ratio = float(w) / h
        if ratio >= 0.9 and ratio <= 1.1:
            img = cv2.drawContours(img, [cnt], -1, (0, 255, 255), 3)
            cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        else:
            cv2.putText(img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            img = cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
