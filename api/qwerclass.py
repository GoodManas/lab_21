import MySQLdb as mdb

ssl = {'ca': 'ca.pem', 'cert': 'server-cert.pem', 'key': 'server-key.pem'}
db = mdb.connect(host = 'localhost',user= 'root', password= '',database= 'Ali_21', ssl=ssl)


class QwerSql():
    def auth(self, login, password):
        cur = db.cursor()
        rows = cur.execute(f"select * from Patients where Login ='{login}' and Password = '{password}'")
        data = cur.fetchall()
        print('avtarizovan')
        cur.close()
        return data
    
    def get_data():
        cur = db.cursor()
        cur.execute("SELECT PatientID, LastName, Photo FROM Patients")
        return cur.fetchall() 