import qrcode 
import os 
import sqlite3

qr_code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 50,
    border = 10,
)

database = sqlite3.connect('product.db')
print("Connected succesfully !")

database.execute(''' CREATE TABLE PRODUCT 
                 (ID     INT     PRIMARY KEY     NOT NULL,
                 NAME   TEXT                    NOT NULL);
                 ''')

database.close()


qr_code.add_data('Some data')
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')
