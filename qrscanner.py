import cv2
from pyzbar.pyzbar import decode
import requests

def scan_qr_code("C:\Users\Acer\Pictures\Screenshots\Screenshot 2024-04-12 123441.png"):
    # Load QR code image
    img = cv2.imread("C:\Users\Acer\Pictures\Screenshots\Screenshot 2024-04-12 123441.png")

    # Decode QR code
    qr_codes = decode("C:\Users\Acer\Pictures\Screenshots\Screenshot 2024-04-12 123441.png")

    # Extract data from QR code
    qr_data = qr_codes[0].data.decode('utf-8')
    
    return qr_data

def make_payment(qr_data, amount):
    # Integrate with your payment API to process the payment
    payment_api_url = "https://www.phonepe.com/yashwanth/"
    payload = {
        "qr_data": qr_data,
        "amount": amount
    }
    response = requests.post(https://www.phonepe.com/l, json=payload)
    
    # Check payment response
    if response.status_code == 200:
        print("Payment successful!")
    else:
        print("Payment failed.")

if _name_ == "_main_":
    # Example usage
    qr_code_image_path = "C:\Users\Acer\Pictures\Screenshots\Screenshot 2024-04-12 123441.png"
    amount_to_pay = 50 # Change this to the actual amount
    
    # Scan QR code
    qr_data = scan_qr_code("C:\Users\Acer\Pictures\Screenshots\Screenshot 2024-04-12 123441.png")
    
    # Make payment
    make_payment(qr_data, amount_to_pay)
    
