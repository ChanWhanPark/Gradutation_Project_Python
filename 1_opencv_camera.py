import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=100)
while (1):
    ret, frame = cap.read()
    frame = cv2.resize(frame, dsize=(480, 320), interpolation=cv2.INTER_AREA)
    fgmask = fgbg.apply(frame)
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(fgmask)
    for index, centroid in enumerate(centroids):
        if stats[index][0] == 0 and stats[index][1] == 0:
            continue
        if np.any(np.isnan(centroid)):
            continue
        x, y, width, height, area = stats[index]
        centerX, centerY = int(centroid[0]), int(centroid[1])
        if area > 100:
            cv2.circle(frame, (centerX, centerY), 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255))

    cv2.imshow('mask', fgmask)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30) & 0xff == 27:
        break
cap.release()
cv2.destroyAllWindows()
