#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
import sqlite3

root=Tk()
root.geometry("430x400")
root.resizable(0,0)
root.title("database tool")

def un_registro():
    ventana=Tk()
    ventana.geometry("400x400")
    def adios():
        ventana.destroy()
        
    mydb=sqlite3.connect("database.db")

    cursor=mydb.cursor()
    
    nombre_act=""
    apellido_act=""
    nya=nombre_apellido.get()
    cont=False
    for i in range(len(nya)):
        if nya[i]==" ":
            cont=True
        if cont==False:
            nombre_act+=nya[i]
        else:
            apellido_act+=nya[i]
    
    cursor.execute('''SELECT * FROM clientes WHERE nombre=:nombre OR apellido=:apellido''',
                  {
                      'nombre':nombre_act,
                      'apellido':apellido_act
                      
                  })
    hola=cursor.fetchall()
    for i in range(len(hola)):
        cont=Label(ventana,text=hola[i][0]).grid(row=i+1,column=0)
        cont1=Label(ventana,text=hola[i][1]).grid(row=i+1,column=1)
        cont2=Label(ventana,text=hola[i][4]).grid(row=i+1,column=2) 
    
    
    mydb.commit()
    mydb.close()
    label=Label(ventana,text="Nombre",bg="silver").grid(row=0,column=0,padx=5,pady=5)
    label1=Label(ventana,text="Apellido",bg="silver").grid(row=0,column=1,padx=5,pady=5)
    label2=Label(ventana,text="Email",bg="silver").grid(row=0,column=2,padx=5,pady=5)
    boton=Button(ventana,text="Aceptar",command=adios)
    boton.grid(row=len(hola)+1,column=0,columnspan=4)
    nombre_apellido.delete(0,END)
    ventana.mainloop()



def actu1():
    
    boton_acualizar_acep["state"]=NORMAL
    boton_acualizar["state"]=DISABLED
    
    mydb=sqlite3.connect("database.db")

    cursor=mydb.cursor()
    
    nombre_act=""
    apellido_act=""
    nya=nombre_apellido.get()
    cont=False
    for i in range(len(nya)):
        if nya[i]==" ":
            cont=True
        if cont==False:
            nombre_act+=nya[i]
        else:
            apellido_act+=nya[i]
    
    cursor.execute('''SELECT * FROM clientes WHERE nombre=:nombre OR apellido=:apellido''',
                  {
                      'nombre':nombre_act,
                      'apellido':apellido_act
                      
                  })
    consulta=cursor.fetchall()
    
    nombre_1.insert(0,consulta[0][0])
    apellido_1.insert(0,consulta[0][1])
    cp_1.insert(0,consulta[0][2])
    precio_1.insert(0,consulta[0][3])
    email_1.insert(0,consulta[0][4])
    direccion_1.insert(0,consulta[0][5])
    ciudad_1.insert(0,consulta[0][6])
    pais_1.insert(0,consulta[0][7])
    numero_1.insert(0,consulta[0][8])
    
    mydb.commit()
    mydb.close()

def actu():
    boton_acualizar_acep["state"]=DISABLED
    boton_acualizar["state"]=NORMAL
    
    mydb=sqlite3.connect("database.db")

    cursor=mydb.cursor()
    nombre_act=""
    apellido_act=""
    nya=nombre_apellido.get()
    cont=False
    for i in range(len(nya)):
        if nya[i]==" ":
            cont=True
        if cont==False:
            nombre_act+=nya[i]
        else:
            apellido_act+=nya[i]
            
    cursor.execute('''UPDATE clientes SET nombre=:nombre_nuevo,apellido=:apellido_nuevo,cp=:cp_nuevo,precio=:precio_nuevo,email=:email_nuevo,direccion=:direccion_nuevo, ciudad=:ciudad_nuevo, pais=:pais_nuevo,numero=:numero_nuevo WHERE nombre=:nombre OR apellido=:apellido''',
                  {
                      'nombre_nuevo':nombre_1.get(),
                      'apellido_nuevo':apellido_1.get(),
                      'cp_nuevo':cp_1.get(),
                      'precio_nuevo':precio_1.get(),
                      'email_nuevo':email_1.get(),
                      'direccion_nuevo':direccion_1.get(),
                      'ciudad_nuevo':ciudad_1.get(),
                      'pais_nuevo':pais_1.get(),
                      'numero_nuevo':numero_1.get(),
                      
                      'nombre':nombre_act,
                      'apellido':apellido_act
                      
                  })
    
    
    nombre_apellido.delete(0,END)
    nombre_1.delete(0,END)
    apellido_1.delete(0,END)
    cp_1.delete(0,END)
    precio_1.delete(0,END)
    email_1.delete(0,END)
    direccion_1.delete(0,END)
    ciudad_1.delete(0,END)
    pais_1.delete(0,END)
    numero_1.delete(0,END)
    mydb.commit()
    mydb.close()
    
def borrar():
    
    mydb=sqlite3.connect("database.db")

    cursor=mydb.cursor()
    
    nombre_eliminar=""
    apellido_eliminar=""
    nya=nombre_apellido.get()
    cont=False
    for i in range(len(nya)):
        if nya[i]==" ":
            cont=True
        if cont==False:
            nombre_eliminar+=nya[i]
        else:
            apellido_eliminar+=nya[i]
    
    
    
    cursor.execute('''DELETE FROM clientes WHERE nombre=:nombre OR apellido=:apellido''',
                  {
                      'nombre':nombre_eliminar,
                      'apellido':apellido_eliminar
                      
                  })
    
    nombre_apellido.delete(0,END)
    
    
    
    
    mydb.commit()
    mydb.close()

def nuevo():
    
    mydb=sqlite3.connect("database.db")

    cursor=mydb.cursor()
    
    #cursor.execute('''CREATE TABLE clientes (nombre TEXT,apellido TEXT,cp INTEGER,precio REAL,email TEXT,direccion TEXT,ciudad TEXT, pais TEXT, numero INTEGER)''')

    cursor.execute('''INSERT INTO clientes VALUES (:nombre,:apellido,:cp,:precio,:email,:direccion,:ciudad,:pais,:numero)''',
        {
            'nombre': nombre_1.get(),
            'apellido': apellido_1.get(),
            'cp': cp_1.get(),
            'precio': precio_1.get(),
            'email': email_1.get(),
            'direccion': direccion_1.get(),
            'ciudad': ciudad_1.get(),
            'pais': pais_1.get(),
            'numero': numero_1.get()
    
        })
 
    nombre_1.delete(0,END)
    apellido_1.delete(0,END)
    cp_1.delete(0,END)
    precio_1.delete(0,END)
    email_1.delete(0,END)
    direccion_1.delete(0,END)
    ciudad_1.delete(0,END)
    pais_1.delete(0,END)
    numero_1.delete(0,END)
    
    mydb.commit()
    mydb.close()

def aceptar():
    
    ventana=Tk()
    ventana.geometry("400x400")
    def adios():
        ventana.destroy()
        
    mydb=sqlite3.connect("database.db")

    cursor=mydb.cursor()
    
    contenido=cursor.execute('''SELECT * FROM clientes''')
    hola=contenido.fetchall()
    
    for i in range(len(hola)):
        cont2=Label(ventana,text=i+1).grid(row=i+1,column=0)
        cont=Label(ventana,text=hola[i][0]).grid(row=i+1,column=1)
        cont1=Label(ventana,text=hola[i][1]).grid(row=i+1,column=2)
        cont2=Label(ventana,text=hola[i][4]).grid(row=i+1,column=3)
        
    mydb.commit()
    mydb.close()
    label3=Label(ventana,text="Id",bg="silver").grid(row=0,column=0,padx=5,pady=5)
    label=Label(ventana,text="Nombre",bg="silver").grid(row=0,column=1,padx=5,pady=5)
    label1=Label(ventana,text="Apellido",bg="silver").grid(row=0,column=2,padx=5,pady=5)
    label2=Label(ventana,text="Email",bg="silver").grid(row=0,column=3,padx=5,pady=5)
    boton=Button(ventana,text="Aceptar",command=adios)
    boton.grid(row=len(hola)+1,column=0,columnspan=4)
    ventana.mainloop()
    
nombre=Label(root,text="Nombre").grid(row=0,column=0)
apellido=Label(root,text="Apellido").grid(row=1,column=0)
cp=Label(root,text="Cp").grid(row=2,column=0)
precio=Label(root,text="Precio").grid(row=3,column=0)
email=Label(root,text="Email").grid(row=4,column=0)
direccion=Label(root,text="Direccion").grid(row=5,column=0)
ciudad=Label(root,text="Ciudad").grid(row=6,column=0)
pais=Label(root,text="Pais").grid(row=7,column=0)
numero=Label(root,text="Numero").grid(row=8,column=0)

nombre_1=Entry(root)
nombre_1.grid(row=0,column=1)
apellido_1=Entry(root)
apellido_1.grid(row=1,column=1)
cp_1=Entry(root)
cp_1.grid(row=2,column=1)
precio_1=Entry(root)
precio_1.grid(row=3,column=1)
email_1=Entry(root)
email_1.grid(row=4,column=1)
direccion_1=Entry(root)
direccion_1.grid(row=5,column=1)
ciudad_1=Entry(root)
ciudad_1.grid(row=6,column=1)
pais_1=Entry(root)
pais_1.grid(row=7,column=1)
numero_1=Entry(root)
numero_1.grid(row=8,column=1)

n_ap=Label(root,text="Identificar por N y A").grid(row=0,column=2)
nombre_apellido=Entry(root)
nombre_apellido.grid(row=1,column=2,padx=10,pady=(0,10))

boton_aceptar=Button(root,text="visualizar todos los registros", command=aceptar,bg="blue").grid(row=9,column=0)
boton_nuevo=Button(root,text="nuevo registro", command=nuevo).grid(row=9,column=1)
boton_borrar=Button(root,text="borrar registro", command=borrar,bg="red").grid(row=10,column=0)
boton_acualizar=Button(root,text="actualizar registro", command=actu1,bg="green")
boton_acualizar.grid(row=10,column=1)
boton_acualizar_acep=Button(root,text="aceptar actualizar", command=actu, state=DISABLED,bg="green")
boton_acualizar_acep.grid(row=10,column=2)
boton_un_registro=Button(root,text="Mostrar un registro",command=un_registro,bg="blue")
boton_un_registro.grid(row=11,column=0)
root.mainloop()


# In[ ]:




