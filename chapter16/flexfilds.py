import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        database='sarthak',
        port=3306
    )
    # conn1 = mysql.connector.connect(
    #     user='root',
    #     password='root',
    #     host='localhost',
    #     database='sarthak',
    #     port=3306
    # )
    conn2 = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        database='sarthak',
        port=3306
    )
    if (conn.is_connected()):
        if (conn2.is_connected()):
            if (conn2.is_connected()):
                print("connected")
        print('conn1 connected')
    elif (conn2.is_connected()):
        print("conn2 connected")
    else:
        print('connection failed')
except:
    print('unable to connect')

sql= "SELECT PRODID FROM PRODUCTS"
sql1= "SELECT DESCRIPTION FROM PRODUCTS"

# InvID="select ID_ from codeinsightr4.PSE_INVENTORY_GROUPS";
# LicData="select TEXT_ from codeinsightr4.pdl_license";

data1="this is written by sarthak"
data2="this is written by sarthak"
data2="257533213583541351"
data3= "www.google.com"
data4= "this is hell"

myc= conn.cursor()
# myc1=conn1.cursor()
myc2=conn2.cursor()
try:
    myc.execute(sql)
    row=myc.fetchone()
    # print(row)
    while row is not None:
        print(row[0])
        if row[0]%2==0:
            sql2="insert into orders values ({},{})".format(row[0],data1)
        elif row[0]%3==0:
            sql2="insert into orders values ({},{})".format(row[0],data2)
        elif row[0]%5==0:
            sql2="insert into orders values ({},{})".format(row[0],data3)
        else:
            sql2="insert into orders values ({},{})".format(row[0],data4)
        myc2.execute(sql2)
        conn2.commit()




            

        # row=myc.fetchone()
# try:
#     myc.execute(sql)
#     myc1.execute(sql1)
#     row=myc.fetchone()
    
#     while row is not None:
#         print(row[1][0])
#         row=myc.fectchone()
    # row1=myc1.fetchall()
    
    # print(row)
    # print(row[1][0])
    # print(row1[1][0])
    # sql2="insert into orders values ("+{row[1][0]}+","+{row1[1][0]}+")"
    # sql2="insert into orders values ({},{})".format(row[1][0],row1[1][0])
    # print(sql2)

    # print(sql2)
    # sql2="INSERT INTO orders(PRODID, DESCRIPTION) VALUES({},'{}')".format(row[2][0],row1[2][0])
    # values=("106","this is sarthak")
    
    # myc2.execute(sql2)
    # conn2.commit()

    # print('Total rows :', myc.rowcount)
except:
    # conn.rollback()
    print("unable to show data")
# myc1.close()
myc.close()
myc2.close()
# conn.close()