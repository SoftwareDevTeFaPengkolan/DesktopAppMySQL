import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="belajar_laravel"
)

cursor = db.cursor()
sql = "SELECT * FROM pegawai"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)
