#!/usr/bin/env python
# coding: utf-8

# In[92]:


from tkinter import *
from tkinter import messagebox

root=Tk()

root.title("Tres en raya")
root.geometry("375x440") 
root.resizable(0,0)

figura="X"
variable_x_1=0
variable_o_1=0
variable_x_2=0
variable_o_2=0
variable_x_3=0
variable_o_3=0
variable_x_4=0
variable_o_4=0
variable_x_5=0
variable_o_5=0
variable_x_6=0
variable_o_6=0
variable_x_7=0
variable_o_7=0
variable_x_8=0
variable_o_8=0
variable_x_9=0
variable_o_9=0

def salir():
    
    root.destroy()
    
def ventana_emergente(nombre):
    
    accion=messagebox.askokcancel("GANADOR","el jugador ganador es:"+nombre)
    if accion==True:
        root.destroy()
    else:
        root.destroy()

def bot1():
    global boton1
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton1.destroy()
        boton1_=Button(root, height="8",width="16",bg="#C0C0C0",text=figura,fg="grey",font=("arial",9),state=DISABLED)
        boton1_.grid(row=2,column=0)
        variable_x_1=1
        figura="O"
        
        if variable_x_2==1 & variable_x_3==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_4==1 & variable_x_7==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_5==1 & variable_x_9==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton1.destroy()
        boton1_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton1_.grid(row=2,column=0)
        variable_o_1=1
        figura="X"
        
        if variable_o_2==1 & variable_o_3==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_4==1 & variable_o_7==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_5==1 & variable_o_9==1:
            ventana_emergente(jugador2_entry.get())
            
def bot2():
    global boton2
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton2.destroy()
        boton2_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton2_.grid(row=2,column=1)
        variable_x_2=1
        figura="O"
        
        if variable_x_1==1 & variable_x_3==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_5==1 & variable_x_8==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton2.destroy()
        boton2_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton2_.grid(row=2,column=1)
        variable_o_2=1
        figura="X"
        
        if variable_o_1==1 & variable_o_3==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_5==1 & variable_o_8==1:
            ventana_emergente(jugador2_entry.get())
            
def bot3():
    global boton3
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton3.destroy()
        boton3_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton3_.grid(row=2,column=2)
        variable_x_3=1
        figura="O"
        
        if variable_x_1==1 & variable_x_2==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_6==1 & variable_x_9==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_5==1 & variable_x_7==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton3.destroy()
        boton3_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton3_.grid(row=2,column=2)
        variable_o_3=1
        figura="X"
        
        if variable_o_1==1 & variable_o_2==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_6==1 & variable_o_9==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_5==1 & variable_o_7==1:
            ventana_emergente(jugador2_entry.get())
            
def bot4():
    global boton4
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton4.destroy()
        boton4_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton4_.grid(row=3,column=0)
        variable_x_4=1
        figura="O"
        
        if variable_x_1==1 & variable_x_7==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_5==1 & variable_x_6==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton4.destroy()
        boton4_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton4_.grid(row=3,column=0)
        variable_o_4=1
        figura="X"
        
        if variable_o_1==1 & variable_o_7==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_5==1 & variable_o_6==1:
            ventana_emergente(jugador2_entry.get())
            
def bot5():
    global boton5
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton5.destroy()
        boton5_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton5_.grid(row=3,column=1)
        variable_x_5=1
        figura="O"
        
        if variable_x_1==1 & variable_x_9==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_2==1 & variable_x_8==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_3==1 & variable_x_7==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_4==1 & variable_x_6==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton5.destroy()
        boton5_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton5_.grid(row=3,column=1)
        variable_o_5=1
        figura="X"
        
        if variable_o_1==1 & variable_o_9==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_2==1 & variable_o_8==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_3==1 & variable_o_7==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_4==1 & variable_o_6==1:
            ventana_emergente(jugador2_entry.get())
            
def bot6():
    global boton6
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton6.destroy()
        boton6_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton6_.grid(row=3,column=2)
        variable_x_6=1
        figura="O"
        
        if variable_x_3==1 & variable_x_9==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_4==1 & variable_x_5==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton6.destroy()
        boton6_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton6_.grid(row=3,column=2)
        variable_o_6=1
        figura="X"
        
        if variable_o_3==1 & variable_o_9==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_4==1 & variable_o_5==1:
            ventana_emergente(jugador2_entry.get())
            
def bot7():
    global boton7
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton7.destroy()
        boton7_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton7_.grid(row=4,column=0)
        variable_x_7=1
        figura="O"
        
        if variable_x_1==1 & variable_x_4==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_5==1 & variable_x_3==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_8==1 & variable_x_9==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton7.destroy()
        boton7_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton7_.grid(row=4,column=0)
        variable_o_7=1
        figura="X"
        
        if variable_o_1==1 & variable_o_4==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_5==1 & variable_o_3==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_8==1 & variable_o_9==1:
            ventana_emergente(jugador2_entry.get())
            
def bot8():
    global boton8
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton8.destroy()
        boton8_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton8_.grid(row=4,column=1)
        variable_x_8=1
        figura="O"
        
        if variable_x_2==1 & variable_x_5==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_7==1 & variable_x_9==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton8.destroy()
        boton8_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton8_.grid(row=4,column=1)
        variable_o_8=1
        figura="X"
        
        if variable_o_2==1 & variable_o_5==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_7==1 & variable_o_9==1:
            ventana_emergente(jugador2_entry.get())
            
def bot9():
    global boton9
    global figura
    global variable_x_1
    global variable_o_1
    global variable_x_2
    global variable_o_2
    global variable_x_3
    global variable_o_3
    global variable_x_4
    global variable_o_4
    global variable_x_5
    global variable_o_5
    global variable_x_6
    global variable_o_6
    global variable_x_7
    global variable_o_7
    global variable_x_8
    global variable_o_8
    global variable_x_9
    global variable_o_9
    
    if figura=="X":
        boton9.destroy()
        boton9_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton9_.grid(row=4,column=2)
        variable_x_9=1
        figura="O"
        
        if variable_x_3==1 & variable_x_6==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_1==1 & variable_x_5==1:
            ventana_emergente(jugador1_entry.get())
        elif variable_x_7==1 & variable_x_8==1:
            ventana_emergente(jugador1_entry.get())
            
    elif figura=="O":
        boton9.destroy()
        boton9_=Button(root,height="8", width="16",bg="#C0C0C0",text=figura,state=DISABLED,fg="grey",font=("arial",9))
        boton9_.grid(row=4,column=2)
        variable_o_9=1
        figura="X"
        
        if variable_o_3==1 & variable_o_6==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_1==1 & variable_o_5==1:
            ventana_emergente(jugador2_entry.get())
        elif variable_o_7==1 & variable_o_8==1:
            ventana_emergente(jugador2_entry.get())
        
# labels de los jugadores
jugador1_label=Label(root,text="Jugador 1: (X)",bg="white",relief="groove",bd=2)
jugador1_label.grid(row=0,column=0)
jugador2_label=Label(root,text="Jugador 2: (O)",bg="white",relief="groove",bd=2)
jugador2_label.grid(row=1,column=0)

# entry de los jugadores
jugador1_entry=Entry(root)
jugador1_entry.grid(row=0,column=1,padx=(5,0))
jugador2_entry=Entry(root)
jugador2_entry.grid(row=1,column=1,padx=(5,0))

# botones
boton1=Button(root,command=bot1,height="8", width="16",bg="#C0C0C0")
boton1.grid(row=2,column=0)

boton2=Button(root,command=bot2,height="8", width="16",bg="#C0C0C0")
boton2.grid(row=2,column=1)

boton3=Button(root,command=bot3,height="8", width="16",bg="#C0C0C0")
boton3.grid(row=2,column=2)

boton4=Button(root,command=bot4,height="8", width="16",bg="#C0C0C0")
boton4.grid(row=3,column=0)

boton5=Button(root,command=bot5,height="8", width="16",bg="#C0C0C0")
boton5.grid(row=3,column=1)

boton6=Button(root,command=bot6,height="8", width="16",bg="#C0C0C0")
boton6.grid(row=3,column=2)

boton7=Button(root,command=bot7,height="8", width="16",bg="#C0C0C0")
boton7.grid(row=4,column=0)

boton8=Button(root,command=bot8,height="8", width="16",bg="#C0C0C0")
boton8.grid(row=4,column=1)

boton9=Button(root,command=bot9,height="8", width="16",bg="#C0C0C0")
boton9.grid(row=4,column=2)

boton_salir=Button(root,text="Salir",bg="white",command=salir)
boton_salir.grid(row=0,column=2)


root.mainloop()


# 

# In[ ]:




