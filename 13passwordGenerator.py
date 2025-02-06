from tkinter import *
from tkinter.ttk import *
import pyperclip
import random
screen = Tk()
screen.title("bob")
screen.geometry('700x150')
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$&"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&"
letnum = letters + numbers
letnumsym = letters + numbers + symbols


def Generate():
  choice = var.get()
  Password_entry.delete(0, END)
  length = int(Length_combobox.get())
  password= ''

  if choice == 1 :
    for i in range(length):
      a = random.choice(letters)
      password += a

  elif choice == 2 :
    for f in range(length):
      b = random.choice(letnum)
      password += b
  elif choice == 3 :
    for e in range(length):
      c = random.choice(letnumsym)
      password += c

  Password_entry.insert(END,password)


def Copy():
  a = Password_entry.get()

  pyperclip.copy(a)

def Encrypt():
  passw = Password_entry.get()
  Epassword_entry.delete(0,END)
  key = 3
  encrpassword = ''
  for i in passw :
    if i in characters:
      pos = characters.index(i)
      newpos = (pos + key) % len(characters)
      encrpassword += characters[newpos]
    else:
      encrpassword += i
  Epassword_entry.insert(END,encrpassword)

def Decrypt():
  passw = Epassword_entry.get()
  Dpassword_entry.delete(0,END)
  key = -3
  decrpassword = ''
  for i in passw :
    if i in characters:
      pos = characters.index(i)
      newpos = (pos + key) % len(characters)
      decrpassword += characters[newpos]
    else:
      decrpassword += i
  Dpassword_entry.insert(END,decrpassword)
#LABELS

Password_lbl = Label(screen,text = "Password",font= 'Impact 17')
Password_lbl.grid(column = 0,row = 0)

Length_lbl = Label(screen,text = "Length",font= 'Impact 17')
Length_lbl.grid(column = 0,row = 1)

Epassword_lbl = Label(screen,text = "Encrypted Password",font= 'Impact 15')
Epassword_lbl.grid(column = 0,row = 2 )

Dpassword_lbl = Label(screen,text = "Decrypted Password",font= 'Impact 15')
Dpassword_lbl.grid(column = 0,row = 3 )




#ENTRIES

Password_entry = Entry(screen,font = 'Impact 15')
Password_entry.grid(column = 1 , row = 0)

Epassword_entry = Entry(screen,font = 'Impact 15')
Epassword_entry.grid(column = 1 , row = 2)

Dpassword_entry = Entry(screen,font = 'Impact 15')
Dpassword_entry.grid(column = 1 , row = 3)




#COMBOBOX
Length_combobox = Combobox(screen,state = 'readonly',font = 'Impact 15')
Length_combobox['values']= ('8','9','10','11','12','13','14','15','16')
Length_combobox.grid(column = 1, row = 1)

#BUTTONS

Copy_button = Button(screen,text = "Copy",command = Copy)
Copy_button.grid(column = 2,row = 0)

Generate_button = Button(screen,text = "Generate",command = Generate)
Generate_button.grid(column = 3 , row = 0)

Encrypt_Button = Button(screen,text = "Encrypt",command = Encrypt)
Encrypt_Button.grid(column = 2,row = 2)

Decrypt_Button = Button(screen,text = "Decrypt",command = Decrypt)
Decrypt_Button.grid(column = 2,row = 3)


#RADIOBUTTON
var = IntVar()
low_radiobutton = Radiobutton(screen,text = "Low",variable= var,value = 1 )
low_radiobutton.grid(column = 2 ,row = 1)

mid_radiobutton = Radiobutton(screen,text = "Medium",variable=var,value = 2)
mid_radiobutton.grid(column = 3 ,row = 1)

str_radiobutton = Radiobutton(screen,text = "Strong",variable=var,value = 3)
str_radiobutton.grid(column = 4 ,row = 1)


















screen.mainloop()
