import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        database='sarthak',
        port=3306
    )
    if (conn.is_connected()):
        print('connected')
except:
    print('unable to connect')

sql="SELECT * FROM products WHERE PRODID=101"
myc= conn.cursor()


try:
    myc.execute(sql)
    row=myc.fetchone()
    print(row)
    print(myc.rowcount)
except:
    conn.rollback()
    print("unable to show data")
myc.close()
conn.close()

