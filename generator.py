import qrcode
from PIL import Image

# Prompt the user to enter the URL
url = input("Enter the URL: ")

# Prompt the user to enter the filename
filename = input("Enter the filename to save as (including extension): ")

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="paleturquoise", back_color="black")
img.save(filename)
