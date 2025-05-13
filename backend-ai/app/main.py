from fastapi import FastAPI, UploadFile, File
from app.lpr_model import detect_license_plate
from app.db_utils import check_registration
from datetime import datetime
import re

def normalize_plate_text(plate: str) -> str:
    plate = plate.upper()
    plate = plate.replace(',', '.')
    plate = re.sub(r'[^A-Z0-9.-]', '', plate)  # Loại bỏ ký tự không hợp lệ
    return plate

app = FastAPI()

@app.post("/recognize/")
async def recognize_plate(file: UploadFile = File(...)):
    image_bytes = await file.read()
    plates = detect_license_plate(image_bytes)

    results = []
    for plate in plates:
        clean_plate = normalize_plate_text(plate)
        results.append({
            "plate": clean_plate,
            "status": check_registration(clean_plate),
            "timestamp": datetime.now().isoformat()
        })

    return {"results": results}
