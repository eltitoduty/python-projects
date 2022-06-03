#!/usr/bin/env python
# coding: utf-8

# In[22]:


from tkinter import *
import random
root=Tk()
root.title("hello")
root.geometry("400x400")
root.config(bg="silver")
root.resizable(0,0)

lista=[]
cont=0

def alt():
    global cont
    

    random.shuffle(lista) 
    
    label.config(text=lista)
    cont+=1
    label_3.config(text="Alteraciones: "+str(cont),fg="black")
    
def responder():
    global pais_adivinar
    global lista
    global cont
    
    adivinado=entry.get()
    
    if adivinado.title()==pais_adivinar:
        label_2.config(text="Correcto!! :)",bg="green")
        entry.delete(0,END)
        lista=[]
        cont=0
        
        
    
    else:
        label_2.config(text="Incorrecto!! :(" +"\n"+"Es "+str(pais_adivinar),bg="red")
        lista=[]
        entry.delete(0,END)
        cont=0
        
        
    btn_2["state"]=NORMAL
    btn_1["state"]=DISABLED
    btn_3["state"]=DISABLED
    
        
        

def nueva():
    
    global lista
    global pais_adivinar
    
   
    paises=["Rusia","Alemania", "Inglaterra","Francia","Italia","España","Ucrania","Polonia","Holanda","Suiza","Austria","Grecia","Suecia","Finlandia","Belgica","Dinamarca","Noruega","Croacia","Irlanda"]

    indice=random.randint(0,len(paises)-1)
    pais_adivinar=paises[indice]



    for i in pais_adivinar:
        lista.append(i)
    
    #podria haber hecho lo siguiente: lista=list(pais_adivinar)
    
    random.shuffle(lista) 
    
    label.config(text=lista)
    label_2.config(text="",bg="silver")
    label_3.config(text="")
    btn_1["state"]=NORMAL
    btn_2["state"]=DISABLED
    btn_3["state"]=NORMAL




#------------widgetssssss

label=Label(root,text="",bg="white",relief="groove",bd=1)
label.pack(pady=10)

entry=Entry(root)
entry.pack(pady=10)

btn_1=Button(root,text="Responder",command=responder)
btn_1.pack(pady=10)

btn_2=Button(root,text="nueva palabra", command=nueva, state=DISABLED)
btn_2.pack(pady=10)

btn_3=Button(root,text="Alterar",command=alt)
btn_3.pack(pady=10)

label_2=Label(root,text="",bg="silver")
label_2.pack(pady=10)

label_3=Label(root,text="",bg="silver")
label_3.pack(pady=10)

nueva()

root.mainloop()


# In[6]:


palabra="hola"
print(list(palabra))


# In[43]:


word=random.choice(palabra)
print(word)


# In[ ]:





# In[ ]:




