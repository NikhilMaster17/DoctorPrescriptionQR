import qrcode

def generate_prescription_qr(prescription_text, file_name="prescription_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(prescription_text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Example usage
prescription = "Patient: John Doe\nMedicine: Paracetamol 500mg\nDosage: Twice a day for 5 days\nDoctor: Dr. Nikhil"
generate_prescription_qr(prescription)
