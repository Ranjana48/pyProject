import qrcode as qr
from PIL import Image
import os

url = input("Enter the URL to generate QR code: ").strip()
file_path = r"C:\\Users\\user\\Desktop\\pyProject\\Image\\qr.png"

qr_code = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=15,
    border=5,
)

qr_code.add_data(url)
qr_code.make(fit=True)

img = qr_code.make_image(
    fill_color="lightblue",
    back_color="white"
)

logo_path = "logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    logo_size = 100
    logo = logo.resize((logo_size, logo_size))


    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size)  //2)
    img.paste(logo, pos)
    print("logo added successfully! 😁")




img.save(file_path)
print(f"custom QR saved : {file_path}")