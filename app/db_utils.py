# Tạm thời mô phỏng danh sách đã đăng ký
registered_plates = {"51F-123.45", "29A-456.78"}

def check_registration(plate):
    return "registered" if plate in registered_plates else "unknown"
