import cv2
import numpy as np

line_shapce = 550
min_width = 80
min_height = 80

def circle(x, y, w, h):
    cx = x + w // 2
    cy = y + h // 2
    return cx, cy

detect = []
offset = 6
counter = 0

cap = cv2.VideoCapture("video.mp4")
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't read frame or end of video.")
        break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (25, line_shapce), (1200, line_shapce), (255, 127, 0), 3)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w < min_width or h < min_height:
            continue

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = circle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame, center, 4, (0, 0, 255), -1)

    for (x, y) in detect[:]:
        if line_shapce - offset < y < line_shapce + offset:
            counter += 1
            detect.remove((x, y))

    cv2.putText(frame, "VEHICLE COUNTER: " + str(counter),
                (350, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow("videos", frame)

    if cv2.waitKey(30) == 13:  # Enter key
        break

cap.release()
cv2.destroyAllWindows()
