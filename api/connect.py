import MySQLdb as mdb

try: 
    ssl = {'ca': 'ca.pem', 'cert': 'server-cert.pem', 'key': 'server-key.pem'}
    con = mdb.connect(
        host = 'localhost',
        user ='root',
        password = '',
        database = 'Ali_21'
    )
    print('Connection ok')
    con.close()
except Exception as ex:
    print('Connection no')
    print(ex)