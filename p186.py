# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:37:14 2024

@author: Aidan
"""
#Se importan las librerias y sus funciones
from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog
import os

#Se crea la plantilla basica de tkinter
root = Tk()
root.geometry("400x250")
root.config(bg='#ADC698')

#Se crean variables vacias
file_name_entry = ''
encryption_text_data = ''
decryption_text_data = ''

#Se define la funcion de saveData
def saveData():
    #Se vuelve la variable global (se puede usar dentro y fuera de la funcion)
    global file_name_entry
    global encryption_text_data
    #en la variable file_name se guarda lo obtenido de su respectibo entry
    file_name = file_name_entry.get()
    #Se abre el archivo de la carpeta y se da el permiso de escribir sobre el
    file = open(file_name+".txt", "w")
    #Se obtiene el mensaje que se va a encriptar
    data = encryption_text_data.get("1.0",END)
    #se encripta el mensaje obtenido
    ciphercode = encrypt('XYZ', data)
    #se convierte a hexadecimal
    hex_string = ciphercode.hex()
    #se imprime la variable donde se contiene el mensaje encriptado en la consola
    print(hex_string)
    #Se guarda en el archivo el mensaje encriptado
    file.write(hex_string)
    #Se elimina lo que contiene el campo de texto
    file_name_entry.delete(0, END)
    #se elimina lo que contiene la variable
    encryption_text_data.delete(1.0, END)
    #se muestra un mensaje que indica que no hubieron errores
    messagebox.showinfo("Update", "Success")

#se define la funcion viewData
def viewData():
    global decryption_text_data
    #Se guarda el archivo en una variable
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    #se accede al explorador de archivos
    name = os.path.basename(text_file)
    #se imprime en la consola name
    print(name)
    #se abre el archivo con el permiso para leer
    text_file = open(name,'r')
    #Se lee el archivo
    paragraph=text_file.read()
    #se vuelve a hexadecimal
    byte_str = bytes.fromhex(paragraph)
    #se desencripta
    original = decrypt('XYZ', byte_str)
    #se guarda el mensaje final
    final_data = original.decode("utf-8")
    #se inserta en un nuevo archivo
    decryption_text_data.insert(END,final_data)
    #se cierra el arhcivo
    text_file.close()
   
#se define la funcion
def startDecryption():
    global file_name_entry
    global decryption_text_data
    #se cierra la ventana
    root.destroy()
 
    decryption_window = Tk()
    decryption_window.config(bg='#B2C9AB')
    decryption_window.geometry("600x500")
   
    decryption_text_data = Text(decryption_window, height=20, width=72)
    decryption_text_data.place(relx=0.5,rely=0.35, anchor=CENTER)
   
    btn_open_file = Button(decryption_window, text="Choose File..", font = 'arial 13', bg="#E8DDB5", padx=10, relief=FLAT, command=viewData)
    btn_open_file.place(relx=0.5,rely=0.8, anchor=CENTER)
   
    decryption_window.mainloop()
   
   
def startEncryption():
    global file_name_entry
    global encryption_text_data
    root.destroy()
 
    encryption_window = Tk()
    encryption_window.config(bg='#B2C9AB')
    encryption_window.geometry("600x500")
   
    file_name_label = Label(encryption_window, text="File Name: " , font = 'arial 13', bg='#B2C9AB')
    file_name_label.place(relx=0.1,rely=0.15, anchor=CENTER)
   
    file_name_entry = Entry(encryption_window, font = 'arial 15')
    file_name_entry.place(relx=0.38,rely=0.15, anchor=CENTER)
   
    btn_create = Button(encryption_window, text="Create", font = 'arial 13', bg="#E8DDB5",  padx=10, relief=FLAT, command=saveData)
    btn_create.place(relx=0.75,rely=0.15, anchor=CENTER)
   
    encryption_text_data = Text(encryption_window, height=20, width=72)
    encryption_text_data.place(relx=0.5,rely=0.55, anchor=CENTER)
   
    encryption_window.mainloop()
   
   
heading_label = Label(root, text="Encryption & Decryption" , font = 'arial 18 italic', bg ='#ADC698')
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)


btn_start_encryption = Button(root, text="Start Encryption" , font = 'arial 13' , bg="white", command=startEncryption, relief=FLAT, padx=10)
btn_start_encryption.place(relx=0.3,rely=0.6, anchor=CENTER)


btn_start_decryption = Button(root, text="Start Decryption" , font = 'arial 13' , bg="white", command=startDecryption, relief=FLAT, padx=10)
btn_start_decryption.place(relx=0.7,rely=0.6, anchor=CENTER)


root.mainloop()






