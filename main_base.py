import cv2


capture = cv2.VideoCapture(0)

while True:
    ret, image = capture.read()

    cv2.imshow('From Camera', image)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # Escape to quit
        break

capture.release()
cv2.destroyAllWindows()