import tkinter as tk 
from tkinter import *

app=tk.Tk() 
app.title("Blood Glucose and Health Assistant App/ Kan Şekeri ve Sağlık Asistanı Uygulaması") 

frame_ust=Frame(app, bg="#d4ebf2") 
frame_ust.place(relx=0, rely=0, relwidth=4,relheight=3) 

frame_alt_sol=Frame(app,bg="#d4ebf2") 
frame_alt_sol.place(relx=0.05, rely=0.242, relwidth=4,relheight=3) 


app.geometry("400x300") 
app.resizable(width=FALSE,height=FALSE)
a1="Aleyna" 
a2="Çabuk" 


isim= tk.Label(text="Adı:",font="Calibri 10 bold") 
isim.place(x=10, y=10) 

y=tk.StringVar() 
isim_girisi=tk.Entry(textvariable=y) 
isim_girisi.place(x=130,y=10) 

isim=tk.Label(text="Soyadı:",font="Calibri 10 bold") 
isim.place(x=10, y=35) 

x=tk.StringVar() 
soyadı_girisi=tk.Entry(textvariable=x) 
soyadı_girisi.place(x=130, y=35) 

dogru_yanlis=tk.Label(text="", font="Calibri 10 bold") 
dogru_yanlis.place(x=100,y=100) 


def onay_komut(): 
    adı=y.get() 
    soyadı=x.get() 
    if adı==a1 and soyadı==a2: 
        print("Doğru") 
        dogru_yanlis.config(text="Hoşgeldiniz " +a1 , fg="green" ) 

 
############################################### 
 
        gender_label=tk.Label(text="Cinsiyet",font="Calibri 10 bold", fg="dark blue") 
        gender_label.place(x=70 ,y=170) 

         
       
        from tkinter import messagebox
 
        master1 = tk.Tk()
        master1.geometry("300x300")
        

        def button1Callback():
            messagebox.showinfo("Sonuç", "Değerler: \n Açlıkta; \n Hipoglisemi(Şeker Düşük); 50-70 mg/dl \n Normal; 70-100 mg/dl \n Gizli Şeker; 100-125 mg/dl \n Diyabet;126 mg/dl<  \n \n Toklukta; \n Normal;100-140 mg/dl \n Gizli Şeker;140-199 mg/dl \n Diyabet;200 mg/dl< \n \n Gebelikte Normal Değerler: \n Açlıkta;  60-105 mg/dl \n Toklukta; 120-130 mg/dl")
        def button2Callback():
            messagebox.showinfo("Sonuç", "Değerler: \n Açlıkta; \n Hipoglisemi(Şeker Düşük); 50-70 mg/dl \n Normal; 70-100 mg/dl \n Gizli Şeker; 100-125 mg/dl \n Diyabet;126 mg/dl< \n \n Toklukta; \n Normal;100-140 mg/dl \n Gizli Şeker;140-199 mg/dl \n Diyabet;200 mg/dl<")
        def button3Callback():
            messagebox.showinfo("Sonuç", "Değerler: \n Açlıkta; \n Hipoglisemi(Şeker Düşük); 50-70 mg/dl \n Normal; 70-100 mg/dl \n Gizli Şeker; 100-125 mg/dl \n Diyabet;126 mg/dl< \n \n Toklukta; \n Normal;100-140 mg/dl \n Gizli Şeker;140-199 mg/dl \n Diyabet;200 mg/dl< ")
  

        button1 = tk.Button(master1, text="Kadın", command=button1Callback)
        button2 = tk.Button(master1, text="Erkek", command=button2Callback)
        button3 = tk.Button(master1, text="Belirtmek İstemiyorum", command=button3Callback)
 

        label_1 = tk.Label(master1, text="Cinsiyet Seçimi")
        label_2 = tk.Label(master1, text="Cinsiyet Seçimi")
        label_3 = tk.Label(master1, text="Cinsiyet Seçimi")
 

        label_1.grid(row=0, column=0)
        label_2.grid(row=0, column=0)
        label_3.grid(row=0, column=0)

        button1.grid(row=1, column=0)
        button2.grid(row=2, column=0)
        button3.grid(row=3, column=0)
 

        tk.mainloop()

############################################### 
        
        boy= tk.Label(text="Boyu (m):",font="Calibri 10 bold") 
        boy.place(x=10, y=10) 


        t=tk.DoubleVar() 
        boy_girisi=tk.Entry(textvariable=t) 
        boy_girisi.place(x=80,y=10) 

        kilo=tk.Label(text="Kilosu (kg):",font="Calibri 10 bold") 
        kilo.place(x=10, y=40) 

        z=tk.IntVar() 
        kilo_girisi=tk.Entry(textvariable=z) 
        kilo_girisi.place(x=80, y=40) 

        boy_kilo=tk.Label(text="", font="Calibri 10 bold") 
        boy_kilo.place(x=20,y=70) 
        boy_kilo.config(text="VKİ: ") 

###############################################
        
        def indeks_komut(): 
            boy=float(t.get()) 
            kilo=int(z.get()) 
            indeks = float(kilo/(boy**2))
            endeks=tk.Label(text="VKİ:", font="Calibri 10 bold") 
            endeks.place(x=500,y=415)
            
            if indeks<=18: 
                boy_kilo.config(text="Zayıf ", fg="orange" ) 
            
            elif 18<indeks<25: 
                boy_kilo.config(text="Normal ", fg="green")            
            
            elif 25<=indeks<30:
                boy_kilo.config(text="Kilolu",fg="red")
            
            elif 30<=indeks<35: 
                boy_kilo.config(text="Obez",fg="brown") 
            
            else: 
                boy_kilo.config(text="Ciddi Obez",fg="black") 
      
        hesapla=tk.Button(text="Hesapla",command=indeks_komut) 
        hesapla.place(x=120, y=70) 


    else: 
        print("Yanlış") 
        dogru_yanlis.config(text="Girilen bilgileri kontrol edip yeniden deneyiniz",fg="red") 

onay=tk.Button(text="Onayla",command=onay_komut) 
onay.place(x=270, y=50) 


app.mainloop()