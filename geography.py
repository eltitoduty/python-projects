#!/usr/bin/env python
# coding: utf-8

# In[119]:


from tkinter import *
from random import randint
import random

root=Tk()
root.geometry("400x400")
root.title("geography app")
root.resizable(0,0)


# creamos un frame
frame_pais=Frame(root, width=500, height=500)
frame_capital=Frame(root, width=500, height=500)

def responder_capital():
    
    label_win=Label(frame_capital)
    label_win.pack(pady=10)
   
    if radio_capital.get()==respuesta_correcta:
        label_win.config(text="ganaste")
    else:
        label_win.config(text="no ganaste") 
       

    
def comprobar():
    
    label_win=Label(frame_pais)
    label_win.pack(pady=10)
    
    if respuesta.get().lower()==paises_1[rand]:
        label_win.config(text="ganaste")
        respuesta.delete(0,END)
    else:
        label_win.config(text="Incorrecto, es:"+" "+paises_1[rand].title())
        respuesta.delete(0,END)
    
    #paises() 
    
    '''no sale la respuesta porque al llamar a paises, te esta borrando inmediatamente el label_win porque en paises llamas
    a esconder_frames()
    
    para solucionarlo ponemos un boton para pasar a la siguiente
    '''
    btn["state"]=NORMAL
    btn_aceptar["state"]=DISABLED
        

def esconder_frames():
    
    for i in frame_pais.winfo_children():
        i.destroy()
    
    for i in frame_capital.winfo_children():
        i.destroy()
    
    frame_pais.pack_forget()
    frame_capital.pack_forget()
    

def paises():
    
    esconder_frames()
    frame_pais.pack(fill=BOTH, expand=True)
    global paises_1
    global rand
    paises_1=["españa","reino unido","argentina","rusia","italia","brasil"]
    rand=randint(0,len(paises_1)-1)
    
    '''
    global imagen
    
    label_imagen=Label(frame_pais)
    label_imagen.pack()
    imagen=PhotoImage(file=paises[rand]+".png")
    label_imagen.config(image=imagen)
    '''
    label_pais=Label(frame_pais,text=paises_1[rand])
    label_pais.pack(pady=10)
    
    global respuesta
    respuesta=Entry(frame_pais)
    respuesta.pack(pady=10)
    
    global btn_aceptar
    btn_aceptar=Button(frame_pais,text="aceptar",command=comprobar, state=NORMAL)
    btn_aceptar.pack(pady=10)
    
    global btn
    btn=Button(frame_pais,text="Siguiente",command=paises,state=DISABLED)
    btn.pack(pady=10)
    
    

def capital():
    
    esconder_frames()
    frame_capital.pack(fill=BOTH, expand=True)
    global paises_1
    global rand
    paises_2=["españa","reino unido","argentina","rusia","italia","brasil"]
    rand=randint(0,len(paises_2)-1)
    
    '''
    global imagen
    
    label_imagen=Label(frame_pais)
    label_imagen.pack()
    imagen=PhotoImage(file=paises[rand]+".png")
    label_imagen.config(image=imagen)
    '''
        
    label=Label(frame_capital,text=paises_2[rand])
    label.pack()
    
    dicc={
        'españa':'madrid',
        'reino unido':'londres',
        'argentina':'buenos aires',
        'rusia':'moscu',
        'italia':'roma',
        'brasil':'brasilia'      
    }
    
    lista_vacia=[]
    #3 random
    global respuesta_correcta
    respuesta_correcta=dicc[paises_2[rand]]
    lista_vacia.append(respuesta_correcta)
    paises_2.remove(paises_2[rand])
    
    rand2=randint(0,len(paises_2)-1)
    lista_vacia.append(dicc[paises_2[rand2]])
    paises_2.remove(paises_2[rand2])
    
    rand3=randint(0,len(paises_2)-1)
    lista_vacia.append(dicc[paises_2[rand3]])
    paises_2.remove(paises_2[rand3])
    
    random.shuffle(lista_vacia)
    
    global radio_capital
    
    random_3=randint(0,2)
    radio_capital=StringVar()
    radio_capital.set(lista_vacia[random_3])
    
    btn_rad1=Radiobutton(frame_capital,text=lista_vacia[0],variable=radio_capital,value=lista_vacia[0])
    btn_rad1.pack()
    btn_rad2=Radiobutton(frame_capital,text=lista_vacia[1],variable=radio_capital,value=lista_vacia[1])
    btn_rad2.pack()
    btn_rad3=Radiobutton(frame_capital,text=lista_vacia[2],variable=radio_capital,value=lista_vacia[2])
    btn_rad3.pack()
    
    global btn_sig
    btn_sig=Button(frame_capital,text="Siguiente",command=capital)
    btn_sig.pack(pady=10)
    
    btn_responder=Button(frame_capital,text="Aceptar",command=responder_capital)
    btn_responder.pack(pady=10)
    
   
    
def salir():
    root.destroy()



# creamos el menu
menu_1=Menu(root)
root.config(menu=menu_1)

# creamos un submenu
pais=Menu(menu_1,tearoff=0)
menu_1.add_cascade(label="Adivinar", menu=pais)
pais.add_command(label="paises", command=paises)
pais.add_command(label="capitales", command=capital)
pais.add_separator()
pais.add_command(label="salir", command=salir)



root.mainloop()


# In[ ]:





# In[ ]:




