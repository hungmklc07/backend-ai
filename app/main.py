from fastapi import FastAPI, UploadFile, File
from app.lpr_model import detect_license_plate
from app.db_utils import check_registration
from datetime import datetime
import re
app = FastAPI()

@app.post("/recognize/")
async def recognize_plate(file: UploadFile = File(...)):
    image_bytes = await file.read()
    plates = detect_license_plate(image_bytes)

    results = []
    for plate in plates:
        results.append({
            "plate": plate,
            "status": check_registration(plate),
            "timestamp": datetime.now().isoformat()
        })

    return {"results": results}
