import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306
    )
    if (conn.is_connected()):
        print('connected')
except:
    print('unable to connect')

sql="SHOW DATABASES"
myc= conn.cursor()
myc.execute(sql)
for d in myc:
    print(d)
    
myc.close()
conn.close()