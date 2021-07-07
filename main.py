import cv2


def blur_face(image):
    (h, w) = image.shape[:2]
    blur_w = int(w / 3.0)
    blur_h = int(h / 3.0)
    if blur_w % 2 == 0:
        blur_w -= 1
    if blur_h % 2 == 0:
        blur_h -= 1
    return cv2.GaussianBlur(image, (blur_w, blur_h), 10)  # sigma=10


capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, image = capture.read()

    faces = face_cascade.detectMultiScale(image, scaleFactor=1.4, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)  # BRG color and width
        image[y:y+h, x:x+w] = blur_face(image[y:y+h, x:x+w])

    cv2.imshow('From Camera', image)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # Escape to quit
        break