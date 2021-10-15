import re
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="Username",
  database="Email",
  passwd="Password"
)


file = open('path\filename.LOG', 'r' ,encoding='utf-8')
file_content = file.read()
email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_content)
print(email)
mycursor = mydb.cursor()
for i in email :
    sql = f"INSERT INTO emails (emails) VALUES ('{i}')"
    mycursor.execute(sql)
mydb.commit()
file.close()
