#!/usr/bin/env python
# coding: utf-8

# In[15]:


from tkinter import *
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("400x400")

def times():
    conti=continente_e.get()
    ciudad=entry.get()
    home=pytz.timezone(conti.title()+"/"+ciudad.title())
    local_time=datetime.now(home)
    actual=local_time.strftime("%H:%M:%S")
    reloj.config(text=actual)
    nombre.config(text=ciudad.title())

# creamos los labels
nombre=Label(root,font=("times",15))
nombre.grid(row=0,column=0,columnspan=2)

reloj=Label(root,font=("times",15))
reloj.grid(row=1,column=0,columnspan=2)

descrip=Label(root,text="Horas Minutos Segundos",font=("times",15))
descrip.grid(row=2,column=0,columnspan=2)

continente=Label(root,text="continente")
continente.grid(row=3,column=0)

ciudad=Label(root,text="ciudad")
ciudad.grid(row=3,column=1)

# entry box
entry=Entry(root)
entry.grid(row=4,column=1)
continente_e=Entry(root)
continente_e.grid(row=4,column=0)

# boton aceptar
boton=Button(root,text="Aceptar",command=times)
boton.grid(row=5,column=0,columnspan=2)



root.mainloop()




# In[ ]:





# In[ ]:




