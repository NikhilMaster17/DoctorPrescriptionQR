from qr_generator import generate_qr_code
from qr_reader import read_qr_code

def main():
    prescription_data = """
    Patient: John Doe
    Medicine: Paracetamol 500mg
    Dosage: 1 tablet twice a day
    Duration: 5 days
    """
    filename = "images/prescription_qr.png"
    generate_qr_code(prescription_data, filename)
    print(f"QR code saved as {filename}")

    decoded = read_qr_code(filename)
    print("Decoded QR code data:")
    print(decoded)

if __name__ == "__main__":
    main()


