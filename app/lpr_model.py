import easyocr
import numpy as np
import cv2

reader = easyocr.Reader(['en'])  # Load sẵn để không load lại mỗi lần gọi

def normalize_plate_text(text):
    """Chuẩn hóa biển số: bỏ khoảng trắng, đổi ',' thành '.' """
    return text.replace(" ", "").replace(",", ".").replace("–", "-")

def detect_license_plate(image_bytes):
    """Nhận diện biển số từ ảnh bytes"""
    # Chuyển từ bytes → ảnh numpy
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # OCR
    results = reader.readtext(image)
    texts = [normalize_plate_text(res[1]) for res in results if res[2] > 0.4]

    # Ghép các dòng lại nếu có nhiều dòng
    if len(texts) >= 2:
        plate = texts[0] + "-" + texts[1]
    elif texts:
        plate = texts[0]
    else:
        plate = ""

    return [plate] if plate else []
