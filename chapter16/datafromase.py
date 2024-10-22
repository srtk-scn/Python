# with open('file1.txt','r') as rf:
#     with open('file2.txt','w') as wf:
#         wf.write(rf.read())



import mysql.connector
import string
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="fnci"
)

mycursor = mydb.cursor()
# sql="SELECT * FROM products"
# myc= conn.cursor()
mycursor.execute("SELECT INVENTORY_ID_ FROM pas_inventory_flex_field")
# print(O)
# print(twent20)

# sql="SELECT * FROM products"
# myc= conn.cursor()


try:
    myc.execute(sql)
    row=myc.fetchone()
# for each in range(100,200):
#   Fiveh1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
#   Fiveh2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=100))
#   Fiveh3 = ''.join(random.choices(string.ascii_uppercase + string.punctuation, k=100))
#   twent20 = ''.join(random.choices(string.ascii_uppercase, k=100))
#   simple = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits, k=10))
#   sql = "INSERT INTO pas_inventory_flex_fields (INVENTORY_ID_,FLEX_FIELD_1_,FLEX_FIELD_2_,FLEX_FIELD_3_,FLEX_FIELD_4_,FLEX_FIELD_5_) VALUES (%s, %s,%s, %s,%s, %s)"
#   val = (each , Fiveh1,Fiveh2,Fiveh3,twent20,simple)
#   mycursor.execute(sql, val)
#   # Fiveh2, Fiveh3, twent20, simple)
#   mydb.commit()
#   if each%10==0:
#     print(mycursor.rowcount, "record inserted. {}".format(each))