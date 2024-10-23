from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="belajar_laravel"
)
mycursor = mydb.cursor()
root = Tk()
root.title("tabel pegawai laravel")
root.geometry("750x350")

label1 = Label(root, text="Nama", width=20,
               height=2).grid(row=1, column=0)
label2 = Label(root, text="jabatan", width=20,
               height=2).grid(row=2, column=0)
label3 = Label(root, text="umur", width=20,
               height=2).grid(row=3, column=0)
label4 = Label(root, text="Alamat", width=20, height=2
               ).grid(row=4, column=0)
label8 = Label(root, width=10, height=2).grid(row=7, column=2)
label9 = Label(root, width=10, height=2).grid(row=7, column=4)

e1 = Entry(root, width=30, borderwidth=5)
e1.grid(row=1, column=2)
e2 = Entry(root, width=30, borderwidth=5)
e2.grid(row=2, column=2)
e3 = Entry(root, width=30, borderwidth=5)
e3.grid(row=3, column=2)
e4 = Entry(root, width=30, borderwidth=5)
e4.grid(row=4, column=2)


def Register():
    pegawai_nama = e1.get()
    dbFirst_Name = ""
    Select = "select count(*) from pegawai where pegawai_nama='%s'" % (pegawai_nama)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    for i in result:
        dbFirst_Name = i[0]
    if(str(pegawai_nama) != str(dbFirst_Name)):
        Insert = "INSERT INTO pegawai (pegawai_nama,pegawai_jabatan,pegawai_umur,pegawai_alamat) VALUES (%s, %s, %s, %s)"
        pegawai_nama = e1.get()
        pegawai_jabatan = e2.get()
        pegawai_umur = e3.get()
        pegawai_alamat = e4.get()
        if(pegawai_nama != "" and pegawai_jabatan != "" and pegawai_umur != ""and pegawai_alamat != ""):
            Value = (pegawai_nama,pegawai_jabatan,pegawai_umur,pegawai_alamat)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.askokcancel("Information", "Record inserted")
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
        else:
            if (pegawai_nama == "" and pegawai_jabatan == "" and pegawai_umur == "" and pegawai_alamat == ""):
                messagebox.askokcancel(
                    "Information", "New Entery Fill All Details")
            else:
                messagebox.askokcancel("Information", "Some fields left blank")
    else:
        messagebox.askokcancel("Information", "Record Already exists")


def ShowRecord():
    pegawai_nama = e1.get()
    cari = ""
    Select = "select count(*) from pegawai where pegawai_nama='%s'" % (pegawai_nama)
    mycursor.execute(Select)
    result1 = mycursor.fetchall()
    for i in result1:
        dbFirst_Name = i[0]

    if int(pegawai_nama) == int(cari):
        Select1 = "select pegawai_nama,pegawai_jabatan,pegawai_umur,pegawai_alamat from pegawai where pegawai_nama='%s'" % (
            pegawai_nama)
        mycursor.execute(Select1)
        result2 = mycursor.fetchall()
        pegawai_nama = ""
        pegawai_jabatan = ""
        pegawai_umur = ""
        pegawai_alamat = ""
        for i in result2:
            pegawai_nama = i[0]
            pegawai_jabatan = i[1]
            pegawai_umur = i[2]
            pegawai_alamat = i[3]
        e2.insert(0, pegawai_jabatan)
        e3.insert(0, pegawai_umur)
        e4.insert(0, pegawai_alamat)

        #messagebox.showinfo("Info", pegawai_nama)
    else:
        messagebox.askokcancel("Information", "No Record exists")


def Delete():
    pegawai_nama = e1.get()
    Delete = "delete from pegawai where pegawai_nama='%s'" % (pegawai_nama)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information", "Record Deleted")
    e1.delete(0,  'end')
    e2.delete(0,  'end')
    e3.delete(0,  'end')
    e4.delete(0,  'end')


button1 = Button(root, text="Register", width=10, height=2,
                 command=Register).grid(row=5, column=1)
button2 = Button(root, text="Delete", width=10, height=2,
                 command=Delete).grid(row=5, column=0)
button4 = Button(root, text="Show record", width=10, height=2,
                 command=ShowRecord).grid(row=5, column=2)

root.mainloop()
