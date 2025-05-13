import easyocr
import cv2
import numpy as np

reader = easyocr.Reader(['en', 'vi'], gpu=False)

def detect_license_plate(image_bytes):
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    results = reader.readtext(image)
    plates = [text for (_, text, prob) in results if prob > 0.5]
    return plates