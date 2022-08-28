import qrcode 
import os 

qr_code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 50,
    border = 10,
)

qr_code.add_data('Some data')
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')