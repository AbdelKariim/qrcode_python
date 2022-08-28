import qrcode 
import os 
import sqlite3

qr_code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 50,
    border = 10,
)

if os.path.exists('product.db'):
    print("Database exists")

database = sqlite3.connect('product.db', timeout=1000)
print("Connected succesfully !")

database.execute(''' CREATE TABLE IF NOT EXISTS PRODUCT 
                 (ID     INT     PRIMARY KEY     NOT NULL,
                 NAME   TEXT                    NOT NULL,
                 UNIQUE(ID, NAME));
                 ''')

database.execute("INSERT OR IGNORE INTO PRODUCT (ID, NAME) \
                VALUES (1, 'iPhone XS')")

database.execute("INSERT OR IGNORE INTO PRODUCT (ID, NAME) \
                VALUES (2, 'iPhone Xr')")

database.execute("INSERT OR IGNORE INTO PRODUCT (ID, NAME) \
                VALUES (3, 'Samsung Galaxy S22 Ultra')")

database.execute("INSERT OR IGNORE INTO PRODUCT (ID, NAME) \
                VALUES (4, 'Google Pixel 6')")

database.commit()
print("Record commited successfully")

database.close()


qr_code.add_data('Some data')
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')
