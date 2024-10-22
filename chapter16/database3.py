import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        database='fnci',
        port=3306
    )
    if (conn.is_connected()):
        print('connected')
except:
    print('unable to connect')

sql="SELECT INVENTORY_ID_ FROM pas_inventory_flex_field"
myc= conn.cursor()


try:
    myc.execute(sql)
    row=myc.fetchall()
    print(row)
    # while row is not None:
        # print(row)
        # row=myc.fetchone()
    print('Total rows :', myc.rowcount)
except:
    conn.rollback()
    print("unable to show data")
myc.close()
conn.close()