import cv2

def read_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    return data or "No QR code found"


