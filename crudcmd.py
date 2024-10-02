import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="belajar_laravel"
)


def insert_data(db):

  pegawai_nama = input("Masukan nama: ")
  pegawai_jabatan  = input("Masukan jabatan: ")
  pegawai_umur = input("Masukan umur: ")
  pegawai_alamat = input("Masukan alamat: ")
  
  
  
  val = (pegawai_nama, pegawai_jabatan, pegawai_umur, pegawai_alamat)
  cursor = db.cursor()
  sql = "INSERT INTO pegawai (pegawai_nama, pegawai_jabatan,pegawai_umur,pegawai_alamat) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM pegawai"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  pegawai_id = input("pilih id pegawai> ")
  pegawai_nama = input("Masukan nama: ")
  pegawai_jabatan  = input("Masukan jabatan: ")
  pegawai_umur = input("Masukan umur: ")
  pegawai_alamat = input("Masukan alamat: ")
 

  sql = "UPDATE pegawai SET pegawai_nama=%s, pegawai_jabatan=%s, pegawai_umur=%s, pegawai_alamat=%s WHERE pegawai_id=%s"
  val = (pegawai_nama, pegawai_jabatan, pegawai_umur, pegawai_alamat, pegawai_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  pegawai_id = input("pilih id pegawai> ")
  sql = "DELETE FROM pegawai WHERE pegawai_id=%s"
  val = (pegawai_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM pegawai WHERE pegawai_nama LIKE %s OR pegawai_jabatan LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)