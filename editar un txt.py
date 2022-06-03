#!/usr/bin/env python
# coding: utf-8

# In[14]:


from tkinter import *
from tkinter import filedialog
from tkinter import font

root=Tk()
root.title("editor texto")
root.geometry("700x700")

def bold():
    
    fuente_neg=font.Font(texto, texto.cget("font"))
    fuente_neg.config(weight="bold")
    
    texto.tag_configure("bold", font=fuente_neg)
    
    tag_actuales=texto.tag_names("sel.first")
    
    if "bold" in tag_actuales:
        texto.tag_remove("bold","sel.first","sel.last")
    else:
        texto.tag_add("bold","sel.first","sel.last")

def cursiva():
    
    fuente_cur=font.Font(texto, texto.cget("font"))
    fuente_cur.config(slant="italic")
    
    texto.tag_configure("italic", font=fuente_cur)
    
    tag_actuales=texto.tag_names("sel.first")
    
    if "italic" in tag_actuales:
        texto.tag_remove("italic","sel.first","sel.last")
    else:
        texto.tag_add("italic","sel.first","sel.last")
        
def select():
    
    seleccion=texto.selection_get()
    
    label_select.config(text=seleccion)

def save():
    global ruta
    archivo=open(ruta,"w")
    leido=archivo.write(texto.get(1.0,END))
    
    archivo.close()
    texto.delete(1.0,END)
    
    
def abrir_text():
    
    global ruta
    ruta=filedialog.askopenfilename(initialdir="C:/Users/es02741742G/Desktop/Endesa/PERSONAL/", title="abrir texto", filetypes=(("texto","*.txt"),))
    texto.config(width=80, height=20,)
    archivo=open(ruta,"r")
    leido=archivo.read()
    
    texto.insert(END,leido)
    archivo.close()
    
    
    
texto=Text(root, width=20, height=20, selectbackground="yellow", selectforeground="black", undo=True)
texto.pack(pady=10)

abrir=Button(root, text="abrir txt", command=abrir_text)
abrir.pack(pady=10)

guardar=Button(root, text="guardar", command=save)
guardar.pack(pady=10)

selection=Button(root, text="seleccionar", command=select)
selection.pack(pady=10)

label_select=Label(root, text="")
label_select.pack(pady=10)

negrita=Button(root, text="negrita", command=bold)
negrita.pack(pady=10)

cursi=Button(root, text="cursiva", command=cursiva)
cursi.pack(pady=10)

btn_uo=Button(root, text="deshacer", command=texto.edit_undo)
btn_uo.pack(pady=10)
btn_ro=Button(root, text="rehacer", command=texto.edit_redo)
btn_ro.pack(pady=10)


root.mainloop()


# In[ ]:




