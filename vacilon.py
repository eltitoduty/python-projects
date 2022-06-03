#!/usr/bin/env python
# coding: utf-8

# In[46]:


from tkinter import *
import random
root=Tk()
root.geometry("500x500")
root.title("te vasilooo")

frame=Frame(root,width=50,bg="white")
frame.pack(fill=BOTH,expand=True)


def aleatorio(event):
    global btn
    btn.destroy()
    n_r=random.randint(0,20)
    n_c=random.randint(0,20)
    
    for i in range(n_r):
        label_r=Label(frame,text="",bg="white")
        label_r.grid(row=i,column=0)
    for i in range(n_c):
        label_c=Label(frame,text="",bg="white")
        label_c.grid(row=0,column=i)
    
    
    btn=Button(frame,text="estoy aquii jajaj",bg="green",relief="groove",bd=5,fg="white")
    btn.bind("<Enter>",aleatorio)
    btn.grid(row=n_r,column=n_c)
    

btn=Button(frame,text="pulsame",bg="green",relief="groove",bd=5,fg="white")
btn.bind("<Enter>",aleatorio)
btn.grid(row=50,column=50)
root.mainloop()


# In[ ]:





# In[ ]:




