#!/usr/bin/env python
# coding: utf-8

# In[21]:


from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api


root=Tk()
root.geometry("1200x650")

ruta=False
ruta_sa=False
seleccion=False

def oscuro():
    
    color_global="black"
    color_sec="grey"
    
    root.config(bg=color_global)
    barra_estado.config(bg=color_global,fg=color_sec)
    texto.config(bg=color_global,fg=color_sec)
    file.config(bg=color_global)
    barra_herr.config(bg=color_global)
    btn_neg.config(bg=color_global,fg=color_sec)
    btn_cur.config(bg=color_global,fg=color_sec)
    btn_des.config(bg=color_global,fg=color_sec)
    btn_re.config(bg=color_global,fg=color_sec)
    btn_color_txt.config(bg=color_global,fg=color_sec)
    btn_color_bg.config(bg=color_global,fg=color_sec)
    btn_oscuro.config(bg=color_global,fg=color_sec)
    btn_claro.config(bg=color_global,fg=color_sec)
    btn_color_fg.config(bg=color_global,fg=color_sec)
    
    
def claro():
    
    
    color_global="SystemButtonFace"
    color_sec="black"
    
    root.config(bg=color_global)
    barra_estado.config(bg=color_global,fg=color_sec)
    texto.config(bg="white",fg=color_sec)
    file.config(bg=color_global)
    barra_herr.config(bg=color_global)
    btn_neg.config(bg=color_global,fg=color_sec)
    btn_cur.config(bg=color_global,fg=color_sec)
    btn_des.config(bg=color_global,fg=color_sec)
    btn_re.config(bg=color_global,fg=color_sec)
    btn_color_txt.config(bg=color_global,fg=color_sec)
    btn_color_bg.config(bg=color_global,fg=color_sec)
    btn_oscuro.config(bg=color_global,fg=color_sec)
    btn_claro.config(bg=color_global,fg=color_sec)
    btn_color_fg.config(bg=color_global,fg=color_sec)
    

def todo(e):
    
    texto.tag_add("sel", "1.0", "end")

def limpiar():
    
    texto.delete(1.0, END)


def printer():
    
    #impresora=win32.GetDefaultPrinter() 
    #barra_estado.config(text=impresora)
    ruta_imp=filedialog.askopenfilename(initialdir="C:/Users/es02741742G/Desktop/Endesa/PERSONAL/", title="Abrir txt", filetypes=(("texto","*.txt"),("python","*.py")))
    
    if ruta_imp:
        
        win32api.ShellExecute(0, "print", ruta_imp, None, ".", 0)
        

def color_bg():
    
    mi_color=colorchooser.askcolor()
    
    if mi_color:
        
        texto.config(bg=mi_color[1])
    
def color_fg():
    
    mi_color=colorchooser.askcolor()
    
    if mi_color:
        
        texto.config(fg=mi_color[1])    

def color_txt():
    
    
    mi_color=colorchooser.askcolor()
    
    if mi_color:
        
        color_texto=font.Font(texto, texto.cget("font"))
    
        texto.tag_configure("color", font=color_texto, foreground=mi_color[1])
    
        tags=texto.tag_names("sel.first")
    
        if "color" in tags:
            texto.tag_remove("color","sel.first","sel.last")
    
        else:
            texto.tag_add("color","sel.first","sel.last")

def negrita():
    
    negritas=font.Font(texto, texto.cget("font"))
    negritas.config(weight="bold")
    
    texto.tag_configure("bold", font=negritas)
    
    tags=texto.tag_names("sel.first")
    
    if "bold" in tags:
        texto.tag_remove("bold","sel.first","sel.last")
    
    else:
        texto.tag_add("bold","sel.first","sel.last")
    

def cursiva():
    
    cursivas=font.Font(texto, texto.cget("font"))
    cursivas.config(slant="italic")
    
    texto.tag_configure("italic", font=cursivas)
    
    tags=texto.tag_names("sel.first")
    
    if "italic" in tags:
        texto.tag_remove("italic","sel.first","sel.last")
    
    else:
        texto.tag_add("italic","sel.first","sel.last")

def cortar(e):
    
    global seleccion
    
    if e != 0:
        
        seleccion=root.clipboard_get()
    
    else:
        if texto.selection_get():
        
            seleccion=texto.selection_get()
            root.clipboard_clear()
            root.clipboard_append(seleccion)
        
            texto.delete("sel.first","sel.last")

def copiar(e):
    
    global seleccion
    
    if e != 0:
        
        seleccion=root.clipboard_get()
    
    else:
        if texto.selection_get():
        
            seleccion=texto.selection_get()
            root.clipboard_clear()
            root.clipboard_append(seleccion)

def pegar(e):
    
    global seleccion
    
    if e != 0:
        seleccion=root.clipboard_get()
        
    
    else:
        
        if seleccion:
            posicion_cursor=texto.index(INSERT)
            texto.insert(posicion_cursor, seleccion)



def guardar():
    
    global ruta
    global ruta_sa
    
    if ruta or ruta_sa:
        ruta=ruta_sa
        nombre=""
        for i in ruta[::-1]:
            if i!="/":
                nombre+=i
            else:
                break
        
        barra_estado.config(text="archivo guardado: "+nombre[::-1])
        archivo=open(ruta,"w")
        leido=archivo.write(texto.get(1.0,END))
        archivo.close()
    
    else:
        guardar_como()
        
    
def guardar_como():
    
    global ruta_sa
    ruta_sa=filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:/Users/es02741742G/Desktop/Endesa/PERSONAL/", title="Guardar txt", filetypes=(("texto","*.txt"),("python","*.py")))
    
    if ruta_sa:
        nombre=""
        for i in ruta_sa[::-1]:
            if i!="/":
                nombre+=i
            else:
                break
        
        barra_estado.config(text="archivo guardado como: "+nombre[::-1])
        archivo=open(ruta_sa,"w")
        leido=archivo.write(texto.get(1.0,END))
        archivo.close()
    
    
    
    
def nuevo():
    texto.delete("1.0",END)
    barra_estado.config(text="Nuevo archivo")
    

def abrir():
    texto.delete("1.0",END)
    global ruta
    ruta=filedialog.askopenfilename(initialdir="C:/Users/es02741742G/Desktop/Endesa/PERSONAL/", title="Abrir txt", filetypes=(("texto","*.txt"),("python","*.py")))
    archivo=open(ruta,"r")
    nombre=""
    for i in ruta[::-1]:
        if i!="/":
            nombre+=i
        else:
            break
        
    barra_estado.config(text="archivo abierto: "+nombre[::-1])
    leido=archivo.read()
    
    texto.insert(END,leido)
    archivo.close()
    

barra_herr=Frame(root)
barra_herr.pack(fill=X)

    
frame=Frame(root)
frame.pack(pady=5)

scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)

scroll_h=Scrollbar(frame, orient=HORIZONTAL)
scroll_h.pack(side=BOTTOM, fill=X)


texto=Text(frame, width=97, height=25, font=("Helvetica",16), selectbackground="yellow", selectforeground="black", undo=True, xscrollcommand=scroll_h.set, yscrollcommand=scroll.set, wrap="none")
texto.pack()

scroll.config(command=texto.yview)
scroll_h.config(command=texto.xview)

menu_1=Menu(root)
root.config(menu=menu_1)

file=Menu(menu_1,tearoff=0)
menu_1.add_cascade(label="Archivo", menu=file)
file.add_command(label="nuevo", command=nuevo)
file.add_command(label="abrir", command=abrir)
file.add_command(label="guardar", command=guardar)
file.add_command(label="guardar como", command=guardar_como)
file.add_separator()
file.add_command(label="imprimir", command=printer)
file.add_separator()
file.add_command(label="salir", command=root.destroy)

edit=Menu(menu_1, tearoff=0)
menu_1.add_cascade(label="Editar", menu=edit)
edit.add_command(label="cortar", command=lambda: cortar(0))
edit.add_command(label="copiar", command=lambda: copiar(0))
edit.add_command(label="pegar", command=lambda: pegar(0))
edit.add_separator()
edit.add_command(label="deshacer", command=texto.edit_undo)
edit.add_command(label="rehacer", command=texto.edit_redo)
edit.add_separator()
edit.add_command(label="Todo", command=lambda: todo(0))
edit.add_command(label="Limpiar", command=limpiar)

barra_estado=Label(root, text="Listo", anchor=CENTER)
barra_estado.pack(fill=X,side=BOTTOM, ipady=5)

root.bind("<Control-x>",cortar)
root.bind("<Control-c>", copiar)
root.bind("<Control-v>",pegar)
root.bind("<Control-A>", todo)

btn_neg=Button(barra_herr, text="negrita", command=negrita)
btn_neg.grid(row=0, column=0, sticky=W)

btn_cur=Button(barra_herr, text="cursiva", command=cursiva)
btn_cur.grid(row=0, column=1)

btn_des=Button(barra_herr, text="deshacer", command=texto.edit_undo)
btn_des.grid(row=0,column=2)

btn_re=Button(barra_herr, text="rehacer", command=texto.edit_redo)
btn_re.grid(row=0,column=3)

btn_color_txt=Button(barra_herr, text="color texto", command=color_txt)
btn_color_txt.grid(row=0, column=4)

btn_color_bg=Button(barra_herr, text="color fondo", command=color_bg)
btn_color_bg.grid(row=0, column=5)

btn_color_fg=Button(barra_herr, text="color todo texto", command=color_fg)
btn_color_fg.grid(row=0, column=6)

btn_oscuro=Button(barra_herr, text="modo oscuro", command=oscuro)
btn_oscuro.grid(row=0, column=7)

btn_claro=Button(barra_herr, text="modo claro", command=claro)
btn_claro.grid(row=0, column=8)



root.mainloop()


# In[ ]:




