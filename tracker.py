# ------------------------------------------------------------------------------
# Imports
import cv2
import HandTrackingModule as htm
import time

# ------------------------------------------------------------------------------
# Camera Setup

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

hand_detector = htm.handDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    img = hand_detector.findHands(img)
    hands = hand_detector.findPosition(img, draw=False)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
