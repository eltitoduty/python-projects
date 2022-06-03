#!/usr/bin/env python
# coding: utf-8

# In[8]:


from tkinter import *
import time

root=Tk()
root.geometry("400x400")
root.title("Reloj")

def reloj():
    hora=time.strftime("%H")
    minu=time.strftime("%M")
    seg=time.strftime("%S")
    
    label.config(text=hora+" "+":"+" "+minu+" "+":"+" "+seg)
    label.after(1000,reloj)

label_1=Label(root,text="Horas, Minutos y Segundos").pack()

label=Label(root, text="XX:XX:XX")
label.pack()

label.after(2000,reloj)

root.mainloop()


# In[ ]:




