import cv2
import datetime

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Anirudh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
num = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

def detect():
    cap = cv2.VideoCapture(0)

    _, frame = cap.read(0)

    dt_tim = str(datetime.datetime.now())
    cv2.putText(frame, dt_tim[:-7], (5, 30), 5, 2, (0, 0, 0), 1, lineType = cv2.LINE_AA)

    newimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    plate = num.detectMultiScale(newimg)

    for (x, y, w, h) in plate:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2, lineType = cv2.LINE_AA)

    return frame
