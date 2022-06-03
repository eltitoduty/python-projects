#!/usr/bin/env python
# coding: utf-8

# In[13]:


from tkinter import *
from tkinter import filedialog
import os

root=Tk()
root.title("Abrir programas")
root.geometry("250x200")
root.resizable(0,0)

def ventana():
    
    ruta=filedialog.askopenfilename()
    os.system('"%s"'% ruta)
    root.destroy()

label=Label(root,text="Elige el programa que deseas abrir").pack(pady=10,padx=10)
btn=Button(root,text="Pinchame",command=ventana,bg="skyblue").pack(pady=10,padx=10)


root.mainloop()


# In[ ]:




