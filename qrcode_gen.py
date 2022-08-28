import qrcode 
import sqlite3

def init_qrcode():
    qr_code = qrcode.QRCode(version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 50,
                    border = 10,
    )
    return qr_code 

def connect_db(database_name, timeout=1000):
    database = sqlite3.connect(database_name, timeout=1000)
    print("Database {} created".format(database))
    return database
    
def close_db(database_name):
    database_name.close()
    
def create_table(database, table_name):    
    database.execute(f"CREATE TABLE IF NOT EXISTS {table_name} \
                        (ID     INT     PRIMARY KEY     NOT NULL, \
                         NAME   TEXT                    NOT NULL, \
                         UNIQUE(ID, NAME));")
    print("Table {} created".format(table_name))
    database.commit()
    
    
def insert_into_db(database, table_name, values):
    print(values)
    columns = ', '.join(values.keys())
    placeholders = ', '.join('?' * len(values))
    sql = 'INSERT OR IGNORE INTO {} ({}) VALUES ({})'.format(table_name, columns, placeholders)
    values = [int(x) if isinstance(x, bool) else x for x in values.values()]
    database.execute(sql, values)
    print("Insert done")
    database.commit()
    
def select_from_db(database, table_name, values):
    values = ', '.join(values)
    sql = 'SELECT {} from {}'.format(values, table_name)
    cursor = database.execute(sql)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        
        
        

database = connect_db("product.db")
    
print("Connected succesfully !")

create_table(database, "cars")    

# insert_into_db(database, 'cars')    

# select_from_db(database, 'product', ['id', 'name'])

close_db(database)


# qr_code = init_qrcode()
# qr_code.add_data('Some data')
# qr_code.make(fit=True)

# img = qr_code.make_image(fill_color="black", back_color="white")
# img.save('qrcode.png')
