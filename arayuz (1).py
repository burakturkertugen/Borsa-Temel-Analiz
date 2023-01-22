import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Image
from tkinter import Label
from tkinter import LabelFrame
from tkinter import font
from tkinter.ttk import Style
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from tkinter import messagebox

#anapencere objesi tanımlama
anapencere=tk.Tk() #anapencere objesi oluştu
anapencere.geometry("1000x500") #anapencerenin boyutları
anapencere.title("Temel Analiz Programı")



######################################################################################################################################################
"""SEKMELER OLUŞTURULUYOR..."""
######################################################################################################################################################
                                                                

#birincil sekme objesi tanımlama(içindekiler;Giriş,Hesaplama,Hakkında&İletişim)
tabs1=ttk.Notebook(anapencere,width=1000,height=550)
tabs1.place(x=50,y=50)
#birincil sekme oluşturma
tab1=ttk.Frame(tabs1,width=300,height=300)
tab2=ttk.Frame(tabs1,width=300,height=300)
tab3=ttk.Frame(tabs1,width=300,height=300)
#birincil sekmeleri ekleme
tabs1.add(tab1,text="Giriş")
tabs1.add(tab2,text="Hesaplama")
tabs1.add(tab3,text="Hakkında & İletişim")

##ikincil sekme objesi tanımlama(bağlı olduğu sekme;tab2       İçindekiler;Faiz hesaplama,Hisse senedi getiri hesaplama,Temel analiz)
tabs2=ttk.Notebook(tab2,width=1000,height=550)
tabs2.place(x=0,y=0)
##ikincil sekmeleri oluşturma
tab4=ttk.Frame(tabs2,width=300,height=300)
tab5=ttk.Frame(tabs2,width=300,height=300)  
tab6=ttk.Frame(tabs2,width=300,height=300)
##ikincil sekmeleri ekleme
tabs2.add(tab4,text="Faiz Hesaplama")
tabs2.add(tab5,text="Hisse Senedi Getiri Hesaplama")
tabs2.add(tab6,text="Temel Analiz")
###üçüncül sekme objesi tanımlama(bağlı olduğu sekme;tab4      İçindekiler;Fisher denklemiyle reel basit hesaplama,basit faiz,bileşik faiz)
tabs3=ttk.Notebook(tab6,width=1000,height=550)
tabs3.place(x=0,y=0)
###üçüncül sekme oluşturma
tab7=ttk.Frame(tab6,width=300,height=300)
tab8=ttk.Frame(tab6,width=300,height=300)
tab9=ttk.Frame(tab6,width=300,height=300)
tab10=ttk.Frame(tab6,width=300,height=300)
tab11=ttk.Frame(tab6,width=300,height=300)
tab12=ttk.Frame(tab6,width=300,height=300)
tab13=ttk.Frame(tab6,width=300,height=300)
###üçüncül sekmeleri ekleme
tabs3.add(tab7,text="Piyasa Göstergeleri")
tabs3.add(tab8,text="Likidite Oranları")
tabs3.add(tab9,text="Borçluluk Oranları")
tabs3.add(tab10,text="Faaliyet Oranları")
tabs3.add(tab11,text="Kârlılık Oranları")
tabs3.add(tab12,text="Büyüme Oranları")
tabs3.add(tab13,text="Yardımcı Değerler")
####dördüncül sekme objesi tanımlama(bağlı olduğu sekme;tab7    İçindekiler;Defter değeri,Fiyat/Kazanç oranı,Piyasa değeri/Defter değeri,Temettü verimi)
tabs4=ttk.Notebook(tab7,width=1000,height=550)
tabs4.place(x=0,y=0)
####dördüncül sekmeleri oluşturma
tab14=ttk.Frame(tabs4,width=300,height=300) #Defter Değeri
tab15=ttk.Frame(tabs4,width=300,height=300) #Fiyat/Kazanç oranı
tab16=ttk.Frame(tabs4,width=300,height=300) #Piyasa değeri/Defter değeri
tab17=ttk.Frame(tabs4,width=300,height=300) #Temettü verimi
####dördüncül sekmeleri ekleme
tabs4.add(tab14,text="Defter Değeri")
tabs4.add(tab15,text="Fiyat/Kazanç Oranı")
tabs4.add(tab16,text="PD/DD")
tabs4.add(tab17,text="Temettü Verimi")
#####besincil sekme objesi tanımlama(bağlı olduğu sekme;tab8    İçindekiler;Cari oran,Asit-test oranı,Nakit oranı,Stok bağımlılık oranı,net işletme sermayesi/aktif oranı,likit aktifler/aktifler oranı)
tabs5=ttk.Notebook(tab8,width=1000,height=550)
tabs5.place(x=0,y=0)
#####besincil sekmeleri oluşturma
tab18=ttk.Frame(tabs5,width=300,height=300) #Cari Oran
tab19=ttk.Frame(tabs5,width=300,height=300) #Asit-test Oranı
tab20=ttk.Frame(tabs5,width=300,height=300) #Nakit Oranı
tab21=ttk.Frame(tabs5,width=300,height=300) #Stok Bağımlılık Oranı
tab22=ttk.Frame(tabs5,width=300,height=300) #Net işletme sermayesi/aktif oranı
tab23=ttk.Frame(tabs5,width=300,height=300) #Likit Aktifler/Toplam Aktifler
#####besincil sekmeleri ekleme
tabs5.add(tab18,text="Cari Oran")
tabs5.add(tab19,text="Asit-test Oranı")
tabs5.add(tab20,text="Nakit Oranı")
tabs5.add(tab21,text="Stok Bağımlılık Oranı")
tabs5.add(tab22,text="Net İşletme Sermayesi/Aktif Oranı")
tabs5.add(tab23,text="Likit Aktifler/Aktifler Oranı")
######altıncıl sekme objesi tanımlama(bağlı olduğu sekme;tab9    İçindekiler;Kaldıraç oranı,Finansman oranı,Toplam borçlar/Özsermaye oranı,Otofinansman Oranı,Maddi duran varlıklar/Özsermaye oranı,Duran varlıklar/Devamlı özsermaye oranı)
tabs6=ttk.Notebook(tab9,width=1000,height=550)
tabs6.place(x=0,y=0)
######altıncıl sekmeleri oluşturma
tab24=ttk.Frame(tabs6,width=300,height=300) #Kaldıraç Oranı
tab25=ttk.Frame(tabs6,width=300,height=300) #Finansman Oranı
tab26=ttk.Frame(tabs6,width=300,height=300) #Toplam Borçlar/Özsermaye Oranı
tab27=ttk.Frame(tabs6,width=300,height=300) #Otofinansman Oranı
tab28=ttk.Frame(tabs6,width=300,height=300) #Maddi Duran Varlıklar/Özsermaye Oranı
tab29=ttk.Frame(tabs6,width=300,height=300) #Duran Varlıklar/Devamlı Özsermaye Oranı
######altıncıl sekmeleri ekleme
tabs6.add(tab24,text="Kaldıraç Oranı")
tabs6.add(tab25,text="Finansman Oranı")
tabs6.add(tab26,text="Toplam Borçlar/Özsermaye Oranı")
tabs6.add(tab27,text="Otofinansman Oranı")
tabs6.add(tab28,text="Maddi Duran Varlıklar/Özsermaye Oranı")
tabs6.add(tab29,text="Duran Varlıklar/Devamlı Özsermaye Oranı")
#######yedincil sekme objesi tanımlama(bağlı olduğu sekme;tab10    İçindekiler;Alacak devir hızı,Ortalama tahsilat süresi,Maddi duran varlıklar devir hızı,Stok devir hızı,Stok değişim hızı,Aktif devir hızı,Ticari borç devir hızı)
tabs7=ttk.Notebook(tab10,width=1000,height=550)
tabs7.place(x=0,y=0)
#######yedincil sekmeleri oluşturma
tab30=ttk.Frame(tabs7,width=300,height=300) #Alacak Devir Hızı
tab31=ttk.Frame(tabs7,width=300,height=300) #Ortalama Tahsilat Süresi
tab32=ttk.Frame(tabs7,width=300,height=300) #Maddi Duran Varlıklar Devir Hızı
tab33=ttk.Frame(tabs7,width=300,height=300) #Stok Devir Hızı
tab34=ttk.Frame(tabs7,width=300,height=300) #Stok Değişim Hızı
tab35=ttk.Frame(tabs7,width=300,height=300) #Aktif Devir Hızı
tab36=ttk.Frame(tabs7,width=300,height=300) #Ticari Borç Devir Hızı
#######yedincil sekmeleri ekleme
tabs7.add(tab30,text="Alacak Devir Hızı")
tabs7.add(tab31,text="Ortalama Tahsilat Süresi")
tabs7.add(tab32,text="Maddi Duran Varlıklar Devir Hızı")
tabs7.add(tab33,text="Stok Devir Hızı")
tabs7.add(tab34,text="Stok Değişim Hızı")
tabs7.add(tab35,text="Aktif Devir Hızı")
tabs7.add(tab36,text="Ticari Borç Devir Hızı")
########sekizincil sekme objesi tanımlama(bağlı olduğu sekme;tab11    İçindekiler;Özsermaye kâr marjı,Ekonomik Kârlılık,Brut kâr marjı,Net kâr marjı,Esas faaliyet kârlılığı,Faaliyet kârlılığı,Faiz ve vergi öncesi kâr marjı,Ödenecek vergi ve yasal yükümlülükler/Net satışlar oranı,Devamlı sermaye kârlılığı,Aktif kârlılığı,Finansal giderler/stoklar oranı)
tabs8=ttk.Notebook(tab11,width=1000,height=550)
tabs8.place(x=0,y=0)
########sekizincil sekmeleri oluşturma
tab37=ttk.Frame(tabs8,width=300,height=300)
tab38=ttk.Frame(tabs8,width=300,height=300)
tab39=ttk.Frame(tabs8,width=300,height=300)
tab40=ttk.Frame(tabs8,width=300,height=300)
tab41=ttk.Frame(tabs8,width=300,height=300)
tab42=ttk.Frame(tabs8,width=300,height=300)
tab43=ttk.Frame(tabs8,width=300,height=300)
tab44=ttk.Frame(tabs8,width=300,height=300)
tab45=ttk.Frame(tabs8,width=300,height=300)
tab46=ttk.Frame(tabs8,width=300,height=300)
tab47=ttk.Frame(tabs8,width=300,height=300)
########sekizincil sekmeleri ekleme
tabs8.add(tab37,text="Özsermaye Kâr Marjı")
tabs8.add(tab38,text="Ekonomik Kârlılık")
tabs8.add(tab39,text="Brüt Kâr Marjı")
tabs8.add(tab40,text="Net Kâr Marjı")
tabs8.add(tab41,text="E.F.K.")
tabs8.add(tab42,text="Faaliyet Kârlılığı")
tabs8.add(tab43,text="F.V.Ö.K.M.")
tabs8.add(tab44,text="Ö.V.Y.Y./N.S.O.") #Ödenecek Vergi ve Yasal Yükümlülükler/Net Satışlar Oranı
tabs8.add(tab45,text="Devamlı Sermaye Kârlılığı")
tabs8.add(tab46,text="Aktif Kârlılığı")
tabs8.add(tab47,text="F.G./S.O.")
########sekizincil sekmeleri AÇIKLAMA İÇİN LABEL
label2=tk.Label(tab41,text="EFK:Esas Faaliyet Kârlılığı",font="Times 16",fg="red")
label2.pack(side=tk.TOP,pady=10)
label3=tk.Label(tab43,text="FVÖKM:Faiz ve Vergi Öncesi Kâr Marjı",font="Times 16",fg="red")
label3.place(x=400,y=10)
label4=tk.Label(tab44,text="ÖVYY:Ödenecek Vergi ve Yasal Yükümlülükler\nNSO:Net Satışlar Oranı",font="Times 16",fg="red")
label4.place(x=400,y=10)
label5=tk.Label(tab47,text="FG / SO:Finansal Giderler / Stoklar Oranı",font="Times 16",fg="red")
label5.place(x=400,y=10)
#label5.pack(side=tk.TOP,pady=10)
#########dokuzuncul sekme objesi tanımlama(bağlı olduğu sekme;12    İçindekiler;Devamlı sermaye büyüme oranı,Net kâr büyüme oranı,Net satışlar büyüme oranı,Net işletme sermayesi büyüme oranı,Aktifler büyüme oranı,Özsermaye büyüme oranı)
tabs9=ttk.Notebook(tab12,width=1000,height=550)
tabs9.place(x=0,y=0)
#########dokuzuncul sekmeleri oluşturma
tab48=ttk.Frame(tabs9,width=300,height=300)
tab49=ttk.Frame(tabs9,width=300,height=300)
tab50=ttk.Frame(tabs9,width=300,height=300)
tab51=ttk.Frame(tabs9,width=300,height=300)
tab52=ttk.Frame(tabs9,width=300,height=300)
tab53=ttk.Frame(tabs9,width=300,height=300)
#########dokuzuncul sekmeleri ekleme
tabs9.add(tab48,text="Devamlı Sermaye Büyüme Oranı")
tabs9.add(tab49,text="Net Kâr Büyüme Oranı")
tabs9.add(tab50,text="Net Satışlar Büyüme Oranı")
tabs9.add(tab51,text="Net İşletme Sermayesi Büyüme Oranı")
tabs9.add(tab52,text="Aktifler Büyüme Oranı")
tabs9.add(tab53,text="Özsermaye Büyüme Oranı")
##########onuncul sekme objesi tanımlama(bağlı olduğu sekme;13    İçindekiler;Net İşletme Sermayesi,Likit Aktifler,Devamlı Sermaye,Faiz ve Vergi Öncesi Kâr)
tabs10=ttk.Notebook(tab13,width=1000,height=550)
tabs10.place(x=0,y=0)
##########onuncul sekmeleri oluşturma
tab54=ttk.Frame(tabs10,width=300,height=300)
tab55=ttk.Frame(tabs10,width=300,height=300)
tab56=ttk.Frame(tabs10,width=300,height=300)
tab57=ttk.Frame(tabs10,width=300,height=300)
##########onuncul sekmeleri ekleme
tabs10.add(tab54,text="Net İşletme Sermayesi")
tabs10.add(tab55,text="Likit Aktifler")
tabs10.add(tab56,text="Devamlı Sermaye")
tabs10.add(tab57,text="Faiz ve Vergi Öncesi Kâr")
###########onbir sekme objesi tanımlama(bağlı olduğu sekme;tab4    İçindekiler;Fisher Denklemiyle Reel Faiz Hesaplama,Basit Faiz Hesaplama,Bileşik Faiz Hesaplama)
tabs11=ttk.Notebook(tab4,width=1000,height=550)
tabs11.place(x=0,y=0)
###########onbir sekmeleri oluşturma
tab58=ttk.Frame(tabs11,width=300,height=300)
tab59=ttk.Frame(tabs11,width=300,height=300)
tab60=ttk.Frame(tabs11,width=300,height=300)
###########onbir sekmeleri ekleme
tabs11.add(tab58,text="Basit Faiz Hesaplama")
tabs11.add(tab59,text="Bileşik Faiz Hesaplama")
tabs11.add(tab60,text="Fisher Denklemiyle Reel Faiz Hesaplama")
############oniki sekme objesi tanımlama(bağlı olduğu sekme;tab5    İçindekiler;Getiri Hesaplama,Hisse Senedi Değerleme Modeli)
tabs12=ttk.Notebook(tab5,width=1000,height=550)
tabs12.place(x=0,y=0)
############oniki sekmeleri oluşturma
tab61=ttk.Frame(tabs12,width=300,height=300)
tab62=ttk.Frame(tabs12,width=300,height=300)
############oniki sekmeleri ekleme
tabs12.add(tab61,text="Getiri Hesaplama")
tabs12.add(tab62,text="Hisse Senedi Değerleme Modeli")


######################################################################################################################################################
"""TEMALAR OLUŞTURULUYOR"""
######################################################################################################################################################
backround100="gray22"
foreground100="DeepSkyBlue2"  #"DeepPink4"
background101="sky blue4"
foreground101="gray80"
background102="lemon chiffon2"
tema1=ttk.Style()
tema1.configure("BW.TLabel", foreground=foreground100, background="gray22",font=("Arial",12,"bold"))

######################################################################################################################################################
"""KANVASLAR OLUŞTURULUYOR"""
######################################################################################################################################################
tema_kanvas1=tk.Canvas(tab1,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas3=tk.Canvas(tab3,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas14=tk.Canvas(tab14,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas15=tk.Canvas(tab15,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas16=tk.Canvas(tab16,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas17=tk.Canvas(tab17,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas18=tk.Canvas(tab18,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas19=tk.Canvas(tab19,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas20=tk.Canvas(tab20,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas21=tk.Canvas(tab21,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas22=tk.Canvas(tab22,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas23=tk.Canvas(tab23,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas24=tk.Canvas(tab24,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas25=tk.Canvas(tab25,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas26=tk.Canvas(tab26,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas27=tk.Canvas(tab27,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas28=tk.Canvas(tab28,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas29=tk.Canvas(tab29,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas30=tk.Canvas(tab30,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas31=tk.Canvas(tab31,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas32=tk.Canvas(tab32,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas33=tk.Canvas(tab33,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas34=tk.Canvas(tab34,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas35=tk.Canvas(tab35,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas36=tk.Canvas(tab36,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas37=tk.Canvas(tab37,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas38=tk.Canvas(tab38,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas39=tk.Canvas(tab39,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas40=tk.Canvas(tab40,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas41=tk.Canvas(tab41,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas42=tk.Canvas(tab42,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas44=tk.Canvas(tab44,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas45=tk.Canvas(tab45,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas46=tk.Canvas(tab46,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas47=tk.Canvas(tab47,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas49=tk.Canvas(tab49,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas50=tk.Canvas(tab50,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas51=tk.Canvas(tab51,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas52=tk.Canvas(tab52,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas53=tk.Canvas(tab53,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas54=tk.Canvas(tab54,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas55=tk.Canvas(tab55,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas56=tk.Canvas(tab56,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas57=tk.Canvas(tab57,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas58=tk.Canvas(tab58,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas59=tk.Canvas(tab59,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas61=tk.Canvas(tab61,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas62=tk.Canvas(tab62,width=1000,height=550,background=backround100).place(x=0,y=0)

######################################################################################################################################################
"""(3) BASİT FAİZ İÇİNDEKİ OBJELER OLUŞTURULUYOR""" 
######################################################################################################################################################
#Formülü görmek için tıklayınız
def bbf1():
    ap=tk.Tk()
    ap.geometry("300x70")
    ap.title("Standart Formül")
    label1=tk.Label(ap,text="Basit Faiz=Anapara * Faiz Oranı * Süre ").place(x=40,y=30)
#Açıklama
def bbf2():
    ap=tk.Tk()
    ap.geometry("500x120")
    ap.title("Geliştirilmiş Basit Faiz")
    label1=tk.Label(ap,text="""Bu fonksiyon basit faizi hesaplar. Basit faizi reel faiz üzerinden hesaplar.
Yatırılan para, belirli bir süre aylık enflasyona maruz kalır. Ayrıca faiz getirisi üzerinden
    stopaj kesintisi yapılır.""").place(x=30,y=30)
def bbf3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=8,y=15)
#Pencere açma butonları ekleniyor    
bbf1=tk.Button(tab58,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bbf1).place(x=10,y=25)
bbf2=tk.Button(tab58,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bbf2).place(x=350,y=25)
bbf3=tk.Button(tab58,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bbf3).place(x=350,y=400)
#kullanıcıdan input için label ekleniyor
bbf_label1=ttk.Label(tab58,text="Nominal Faiz :",style="BW.TLabel").place(x=10,y=70)
bbf_label2=ttk.Label(tab58,text="Enflasyon Oranı :",style="BW.TLabel").place(x=10,y=105)
bbf_label3=ttk.Label(tab58,text="Anapara :",style="BW.TLabel").place(x=10,y=140)
bbf_label4=ttk.Label(tab58,text="Anaparayı Yatıracağınız Süre(Ay) :",style="BW.TLabel").place(x=10,y=175)
bbf_label5=ttk.Label(tab58,text="Stopaj Oranı :",style="BW.TLabel").place(x=10,y=210)
bbf_label6=ttk.Label(tab58,text="Süre(Ay) :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=245)
bbf_label7=ttk.Label(tab58,text="Basit Faiz Getirisi :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=280)
bbf_label8=ttk.Label(tab58,text="Stopaj Kesintisi :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=315)
bbf_label9=ttk.Label(tab58,text="Yeni Anapara :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=350)
#Sonucu yazdıracağımız Labeli oluşturuyoruz
bbf_label_sure=ttk.Label(tab58,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bbf_label_getiri=ttk.Label(tab58,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bbf_label_stopaj=ttk.Label(tab58,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bbf_label_yenianapara=ttk.Label(tab58,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
bbf_label_sure.place(x=310,y=245)
bbf_label_getiri.place(x=310,y=280)
bbf_label_stopaj.place(x=310,y=315)
bbf_label_yenianapara.place(x=310,y=350)

#input alanı oluşturuyoruz
bbf_entry1=tk.Entry(tab58,width=15,background=background102)#.place(x=400,y=75)
bbf_entry2=tk.Entry(tab58,width=15,background=background102)#.place(x=215,y=110)
bbf_entry3=tk.Entry(tab58,width=15,background=background102)#.place(x=215,y=145)
bbf_entry4=tk.Entry(tab58,width=15,background=background102)#.place(x=215,y=180)
bbf_entry5=tk.Entry(tab58,width=15,background=background102)#.place(x=215,y=215)
#input box'ları yerleştiriyoruz
bbf_entry1.place(x=310,y=73)
bbf_entry2.place(x=310,y=108)
bbf_entry3.place(x=310,y=143)
bbf_entry4.place(x=310,y=178)
bbf_entry5.place(x=310,y=213)

######################################################################################################################################################
"""(4) BİLEŞİK FAİZ İÇİNDEKİ OBJELER OLUŞTURULUYOR"""
######################################################################################################################################################
#Formül
def bif_1():
    ap=tk.Tk()
    ap.geometry("375x130")
    ap.title("Bileşik Faiz Formülü")
    label1=tk.Label(ap,text="""
    Bileşik Faiz=pv*(1+i)**n    >>>**(sayının üssünü almak)
    Bileşik Faiz=s
    pv=Anapara
    i=Nominal faiz
    n=Ay""").place(x=40,y=30)
#Açıklama
def bif_2():
    ap=tk.Tk()
    ap.geometry("450x100")
    ap.title("Bileşik Faiz Hakkında Açıklama")
    label1=tk.Label(ap,text="""Bu fonksiyon bileşik faiz hesaplar. Bileşik faizi reel faiz üzerinden hesaplar.
    Ayrıca faiz getirisi üzerinden stopaj kesintisi yapar.""").place(x=30,y=30)
def bif_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=8,y=15)
#Pencere açma butonları ekleniyor    
bif1=tk.Button(tab59,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bif_1).place(x=10,y=25)
bif2=tk.Button(tab59,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bif_2).place(x=250,y=25)
bif3=tk.Button(tab59,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bif_3).place(x=352,y=400)

#kullanıcıdan input için label ekleniyor
bif_label1=ttk.Label(tab59,text="Nominal Faiz :",style="BW.TLabel").place(x=10,y=70)
bif_label2=ttk.Label(tab59,text="Enflasyon Oranı :",style="BW.TLabel").place(x=10,y=105)
bif_label3=ttk.Label(tab59,text="Anapara :",style="BW.TLabel").place(x=10,y=140)
bif_label4=ttk.Label(tab59,text="Anaparayı Yatıracağınız Süre(Ay) :",style="BW.TLabel").place(x=10,y=175)
bif_label5=ttk.Label(tab59,text="Stopaj Oranı :",style="BW.TLabel").place(x=10,y=210)
bif_label6=ttk.Label(tab59,text="Süre(Ay) :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=245)
bif_label7=ttk.Label(tab59,text="Bileşik Faiz Getirisi :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=280)
bif_label8=ttk.Label(tab59,text="Stopaj Kesintisi :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=315)
bif_label9=ttk.Label(tab59,text="Yeni Anapara :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=350)
#Sonucu yazdıracağımız Labeli oluşturuyoruz
bif_label_sure=ttk.Label(tab59,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bif_label_getiri=ttk.Label(tab59,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bif_label_stopaj=ttk.Label(tab59,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bif_label_yenianapara=ttk.Label(tab59,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
bif_label_sure.place(x=200,y=245)
bif_label_getiri.place(x=200,y=280)
bif_label_stopaj.place(x=200,y=315)
bif_label_yenianapara.place(x=200,y=350)

#input alanı oluşturuyoruz
bif_entry1=tk.Entry(tab59,width=15,background=background102)#.place(x=215,y=75)
bif_entry2=tk.Entry(tab59,width=15,background=background102)#.place(x=215,y=110)
bif_entry3=tk.Entry(tab59,width=15,background=background102)#.place(x=215,y=145)
bif_entry4=tk.Entry(tab59,width=15,background=background102)#.place(x=215,y=180)
bif_entry5=tk.Entry(tab59,width=15,background=background102)#.place(x=215,y=215)
#input box'ları yerleştiriyoruz
bif_entry1.place(x=200,y=70)
bif_entry2.place(x=200,y=105)
bif_entry3.place(x=200,y=140)
bif_entry4.place(x=200,y=175)
bif_entry5.place(x=200,y=210)

######################################################################################################################################################
"""(2) FİSHER DENKLEMİYLE REEL FAİZ HESAPLAMA İÇİNDEKİ OBJELER OLUŞTURULUYOR""" 
######################################################################################################################################################
#Paned window oluşturuluyor

fdrfh_pw1=ttk.Panedwindow(tab60,orient=tk.HORIZONTAL)
fdrfh_pw1.pack(fill=tk.BOTH,expand=True)
fdrfh_pw2=ttk.Panedwindow(tab60,orient=tk.HORIZONTAL)
#Paned window için frame oluşturuluyor
fdrfh_frame1=ttk.Frame(fdrfh_pw1,width=400,height=300,relief=tk.RIDGE)
fdrfh_frame2=ttk.Frame(fdrfh_pw2,width=400,height=300,relief=tk.RAISED)
fdrfh_pw2.add(fdrfh_frame2)
fdrfh_pw1.add(fdrfh_frame1)

fdrfh_pw1.add(fdrfh_pw2)
#KANVASLAR
tema_kanvas60_1=tk.Canvas(fdrfh_frame1,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas60_2=tk.Canvas(fdrfh_frame2,width=1000,height=550,background=backround100).place(x=0,y=0)
#Formülü görmek için tıklayınız
def fdrfh_1():
    ap=tk.Tk()
    ap.geometry("325x150")
    ap.title("Yüksek Enflasyon varken")
    label1=tk.Label(ap,text="""
                            r=((1+i)/(1+p))-1
                            r:reel faiz oranı
                            i:nominal faiz oranı
                            p:beklenen enflasyon oranı
                            """).place(x=0,y=30)
def fdrfh_11():
    ap=tk.Tk()
    ap.geometry("325x150")
    ap.title("Düşük Enflasyon varken")
    label1=tk.Label(ap,text="""
                            r=i-p
                            r:reel faiz oranı
                            i:nominal faiz oranı
                            p:beklenen enflasyon oranı
                            """).place(x=0,y=30)
#Açıklama
def fdrfh_2():
    ap=tk.Tk()
    ap.geometry("500x120")
    ap.title("Yüksek Enflasyon varken")
    label1=tk.Label(ap,text="""
                                Bu fonksiyon ekonomide düşük enflasyon veya yüksek enflasyon
                                olduğu sürede reel faiz oranını hesaplar.""").place(x=0,y=30)
def fdrfh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=8,y=15)
#Pencere açma butonları ekleniyor    
fdrfh1=tk.Button(fdrfh_frame1,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=fdrfh_11).place(x=10,y=25)
fdrfh2=tk.Button(fdrfh_frame1,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=fdrfh_2).place(x=250,y=25)
fdrfh3=tk.Button(fdrfh_frame1,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=fdrfh_3).place(x=325,y=175)

fdrfh4=tk.Button(fdrfh_frame2,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=fdrfh_1).place(x=10,y=25)
fdrfh5=tk.Button(fdrfh_frame2,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=fdrfh_2).place(x=250,y=25)
fdrfh6=tk.Button(fdrfh_frame2,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=fdrfh_3).place(x=325,y=175)

#kullanıcıdan input için label ekleniyor
fdrfh_label1=ttk.Label(fdrfh_frame1,text="Nominal Faiz :",style="BW.TLabel").place(x=10,y=70)
fdrfh_label2=ttk.Label(fdrfh_frame1,text="Beklenen Enflasyon Oranı :",style="BW.TLabel").place(x=10,y=105)
fdrfh_label3=ttk.Label(fdrfh_frame1,text="Fisher Denklemiyle Reel Faiz :",style="BW.TLabel").place(x=10,y=140)

fdrfh_label4=ttk.Label(fdrfh_frame2,text="Nominal Faiz :",style="BW.TLabel").place(x=10,y=70)
fdrfh_label5=ttk.Label(fdrfh_frame2,text="Beklenen Enflasyon Oranı :",style="BW.TLabel").place(x=10,y=105)
fdrfh_label6=ttk.Label(fdrfh_frame2,text="Fisher Denklemiyle Reel Faiz :",style="BW.TLabel").place(x=10,y=140)
#input alanı oluşturuyoruz
fdrfh_entry1=tk.Entry(fdrfh_frame1,width=15,background=background102)
fdrfh_entry2=tk.Entry(fdrfh_frame1,width=15,background=background102)
fdrfh_entry3=tk.Entry(fdrfh_frame2,width=15,background=background102)
fdrfh_entry4=tk.Entry(fdrfh_frame2,width=15,background=background102)
#input box'ları yerleştiriyoruz
fdrfh_entry1.place(x=200,y=70)
fdrfh_entry2.place(x=200,y=105)
fdrfh_entry3.place(x=200,y=70)
fdrfh_entry4.place(x=200,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
fdrfh_label_sonuc=ttk.Label(fdrfh_frame1,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
fdrfh_label_sonuc2=ttk.Label(fdrfh_frame2,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))

#Sonucu yazdıracağımız label'i ekliyoruz
fdrfh_label_sonuc.place(x=200,y=140)
fdrfh_label_sonuc2.place(x=200,y=140)
#Düşük Enflasyon Durumu Label
fdrfh_label_7=ttk.Label(fdrfh_frame1,text="Ekonomide Düşük Enflasyon Varken",style="BW.TLabel",width=30,).place(x=3,y=245)
#Yüksek Enflasyon Durumu Label
fdrfh_label_8=ttk.Label(fdrfh_frame2,text="Ekonomide Yüksek Enflasyon Varken",style="BW.TLabel",width=30).place(x=3,y=245)



######################################################################################################################################################
"""(1) HİSSE SENEDİ GETİRİ HESAPLAMA İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab61)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def hsgh_1():
    ap=tk.Tk()
    ap.geometry("400x120")
    ap.title("Hisse Senedi Getiri Hesaplama")
    label1=tk.Label(ap,text="""
                            r=[(dsf-dbf)+t]/dbf
                            r=hisse senedinin bir dönemdeki getirisi
                            dbf=dönem başındaki hisse senedi fiyatı
                            dsf=dönem sonundaki hisse senedi fiyatı
                            t=dönem içinde tahsil edilen temettü
                            """).place(x=0,y=15)
#Açıklama
def hsgh_2():
    ap=tk.Tk()
    ap.geometry("500x90")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Bu fonksiyon hisse senedinin bir dönemdeki getirisini hesaplar.""").place(x=0,y=15)
def hsgh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
hsgh1=tk.Button(tab61,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=hsgh_1).place(x=10,y=25)
hsgh2=tk.Button(tab61,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=hsgh_2).place(x=275,y=25)
hsgh3=tk.Button(tab61,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=hsgh_3).place(x=275,y=225)
#kullanıcıdan input için label ekleniyor
hsgh_label1=ttk.Label(tab61,text="Dönem Başı Hisse Senedi Fiyatı :",style="BW.TLabel").place(x=10,y=70)
hsgh_label2=ttk.Label(tab61,text="Dönem Sonu Hisse Senedi Fiyatı :",style="BW.TLabel").place(x=10,y=105)
hsgh_label3=ttk.Label(tab61,text="Dönem İçinde Tahsil Edilen Temettü :",style="BW.TLabel").place(x=10,y=140)
hsgh_label4=ttk.Label(tab61,text="Hisse Senedinin Bir Dönemdeki Getirisi: :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
hsgh_entry1=tk.Entry(tab61,width=15,background=background102)
hsgh_entry2=tk.Entry(tab61,width=15,background=background102)
hsgh_entry3=tk.Entry(tab61,width=15,background=background102)
#input box'ları yerleştiriyoruz
hsgh_entry1.place(x=275,y=70)
hsgh_entry2.place(x=275,y=105)
hsgh_entry3.place(x=275,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
hsgh_label_sonuc=ttk.Label(tab61,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
hsgh_label_sonuc.place(x=275,y=175)

######################################################################################################################################################
"""(5) HİSSE SENEDİ DEĞERLEME MODELİ İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab62)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def hsdm_1():
    ap=tk.Tk()
    ap.geometry("440x120")
    ap.title("Hisse Senedi Değerleme Modeli")
    label1=tk.Label(ap,text="""
                            p=(t+f)/(1+k)
                            p:hisse senedinden elde edilecek nakit akımlarının bugünkü değeri
                            t:bir yıl sonunda ödenen temettü
                            k:hisseye yapılan yatırımdan beklenen getirinin oranı
                            f:hissenin dönem sonunda beklenen fiyatı
                            """).place(x=0,y=15)
#Açıklama
def hsdm_2():
    ap=tk.Tk()
    ap.geometry("600x150")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Örneğin;
                    %20 getiri hedefi olsun. Şirket 50 kuruş temettü versin. Hisse fiyatı şu an 20 tl olsun.
                    Yıl sonunda hissenin 23 tl olacağını varsayalım. O halde:
                    p=(0.50+23)/(1+0.20)
                    p=19.58
                    Bu analize göre hisse senedinden elde edilecek nakit akımlarının bugünkü değeri 19.58 tldir.
                    Bugünkü satış fiyatı 20 tl olduğundan bu hissenin alınması önerilmez.""").place(x=0,y=15)
def hsdm_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
hsdm1=tk.Button(tab62,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=hsdm_1).place(x=10,y=25)
hsdm2=tk.Button(tab62,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=hsdm_2).place(x=285,y=25)
hsdm3=tk.Button(tab62,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=hsdm_3).place(x=285,y=245)
#kullanıcıdan input için label ekleniyor
hsdm_label1=ttk.Label(tab62,text="Hisse Senedinin Bugünkü Fiyatı :",style="BW.TLabel").place(x=10,y=70)
hsdm_label2=ttk.Label(tab62,text="Bir Yıl Sonunda Ödenmesi Beklenen Temettü :",style="BW.TLabel").place(x=10,y=105)
hsdm_label3=ttk.Label(tab62,text="Yapılan Yatırımdan Beklenen Getiri Oranı :",style="BW.TLabel").place(x=10,y=140)
hsdm_label4=ttk.Label(tab62,text="Hisse Senedinin Dönem Sonunda Beklenen Fiyatı :",style="BW.TLabel").place(x=10,y=175)
hsdm_label5=ttk.Label(tab62,text="Hisse Senedinden Elde Edilecek Değer :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=210)
#input alanı oluşturuyoruz
hsdm_entry1=tk.Entry(tab62,width=15,background=background102)
hsdm_entry2=tk.Entry(tab62,width=15,background=background102)
hsdm_entry3=tk.Entry(tab62,width=15,background=background102)
hsdm_entry4=tk.Entry(tab62,width=15,background=background102)
#input box'ları yerleştiriyoruz
hsdm_entry1.place(x=285,y=70)
hsdm_entry2.place(x=285,y=105)
hsdm_entry3.place(x=285,y=140)
hsdm_entry4.place(x=285,y=175)
#Sonucu yazdıracağımız label'i oluşturuyoruz
hsdm_label_sonuc=ttk.Label(tab62,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
hsdm_label_sonuc.place(x=285,y=210)

######################################################################################################################################################
"""(6) PİYASA GÖSTERGESİ DEFTER DEĞERİ İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab14)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def pgdd_1():
    ap=tk.Tk()
    ap.geometry("450x120")
    ap.title("Defter Değeri")
    label1=tk.Label(ap,text="""
                    Defter değeri = Özkaynaklar
                    1.Hisse Başına Defter Değeri (HBDD) = Özsermaye / Hisse Sayısı
                    2.Hisse Defter Değeri=Özsermaye/Ödenmiş Sermaye
                            """).place(x=0,y=15)
#Açıklama
def pgdd_2():
    ap=tk.Tk()
    ap.geometry("550x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Örneğin;
                    Defter değeri(net varlık değeri)
                    Piyasa defteri değeri bir şirketin birikmiş amortisman ve zararları çıkarıldıktan sonra
                    mali ve finansal tablolarına yansıtılan değerdir.Defter değeri şirketlerin varlıkları ve
                    borçları arasındaki farka eşittir.""").place(x=0,y=15)
def pgdd_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
pgdd1=tk.Button(tab14,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=pgdd_1).place(x=10,y=25)
pgdd2=tk.Button(tab14,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=pgdd_2).place(x=285,y=25)
pgdd3=tk.Button(tab14,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=pgdd_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
pgdd_label1=ttk.Label(tab14,text="Şirketin Özsermayesi :",style="BW.TLabel").place(x=10,y=70)
pgdd_label2=ttk.Label(tab14,text="Şirketin Ödenmiş Sermayesi :",style="BW.TLabel").place(x=10,y=105)
pgdd_label3=ttk.Label(tab14,text="Defter Değeri :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)

#input alanı oluşturuyoruz
pgdd_entry1=tk.Entry(tab14,width=15,background=background102)
pgdd_entry2=tk.Entry(tab14,width=15,background=background102)
#input box'ları yerleştiriyoruz
pgdd_entry1.place(x=285,y=70)
pgdd_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
pgdd_label_sonuc=ttk.Label(tab14,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
pgdd_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(7) PİYASA GÖSTERGESİ FİYAT/KAZANÇ ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab15)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def pgfko_1():
    ap=tk.Tk()
    ap.geometry("450x120")
    ap.title("Fiyat/Kazanç Oranı")
    label1=tk.Label(ap,text="""
    Hisse Başına Kâr (HBK) = Yıllık Kâr / Hisse Sayısı 
    Hisse Sayısı (HS) = Ödenmiş Sermaye / Bir Hissenin Nominal Değeri 
    Fiyat/Kazanç Oranı(F/K) = Borsa Fiyatı / Hisse Başına Kâr
                            """).place(x=0,y=15)
#Açıklama
def pgfko_2():
    ap=tk.Tk()
    ap.geometry("790x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    F/K oranı şirketin elde edeceği kâr için yatırımcının ne kadar ödeme yaptığını gösterir. Örneğin F/K oranı 10 olan bir işletmenin  yatırımcıları,
    işletmenin elde edeceği her 1 tl kâr için 10 tl ödemeyi kabul eder. F/K oranının yüksek olması hisse senedinin fiyatının yüksek olduğu, düşük
    olması ise  hisse fiyatının ucuz kaldığı şeklinde yorumlanacağı gibi, şirketin piyasada işlem gören hisse senedi fiyatı ile elde ettiği kârın
    doğru orantılı olması gerektiği fikrine dayanır. Hisse senetlerindeki F/K oranı bize yatırımımızın kendisini amorti edeceği süreyi verir ve bu
    oran ne kadar düşük olursa hisse için ödenen paranın geri dönüşünün o kadar kısa olduğunu gösterir.""").place(x=0,y=15)
def pgfko_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
pgfko1=tk.Button(tab15,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=pgfko_1).place(x=10,y=25)
pgfko2=tk.Button(tab15,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=pgfko_2).place(x=285,y=25)
pgfko3=tk.Button(tab15,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=pgfko_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
pgfko_label1=ttk.Label(tab15,text="Borsa Fiyatı :",style="BW.TLabel").place(x=10,y=70)
pgfko_label2=ttk.Label(tab15,text="Hisse Başına Kâr :",style="BW.TLabel").place(x=10,y=105)
pgfko_label3=ttk.Label(tab15,text="Fiyat/Kazanç Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)

#input alanı oluşturuyoruz
pgfko_entry1=tk.Entry(tab15,width=15,background=background102)
pgfko_entry2=tk.Entry(tab15,width=15,background=background102)
#input box'ları yerleştiriyoruz
pgfko_entry1.place(x=285,y=70)
pgfko_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
pgfko_label_sonuc=ttk.Label(tab15,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
pgfko_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(8) PİYASA GÖSTERGESİ PD/DD İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab16)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def pgpddd_1():
    ap=tk.Tk()
    ap.geometry("350x120")
    ap.title("Piyasa Değeri/Defter Değeri")
    label1=tk.Label(ap,text="""
    PD/DD= Hisse senedi fiyatı/(Özsermaye/Ödenmiş sermaye)
                            """).place(x=0,y=15)
#Açıklama
def pgpddd_2():
    ap=tk.Tk()
    ap.geometry("865x265")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Düşük PD/DD oranı bir işletmenin piyasada olması gerekenden düşük değerlendiği konusunda ipucu verebilir. Düşük PD/DD oranına sahip işletmelere yatırım
    yapıldığında yüksek getiri elde edilmesi beklenebilir, fakat aynı zamanda düşük  PD/DD oranı  işletmenin düşük değerlenmesine neden olan önemli bir
    sorunu olduğu konusunda ipucu verebilir.
    Bir işletmenin hisse senedi fiyatının defter değerinin altında olması, diğer bir ifadeyle pd/dd oranının 1’in altında olması, işletmenin tüm borçları
    ödendikten sonra kalan net varlıklarından dahi düşük değerlendiğini gösterir. Bu da normal bir durum değildir. İşletmenin bu durumda olmasını
    gerektirecek bir sorun görülmüyorsa ya da düşük performansa yol açacak sorunun çözüldüğü düşünülüyorsa yatırımcılar tarafından bu işletme kazanç getirme
    potansiyeli yüksek bir yatırım fırsatı olarak görülmektedir.

    PD/DD oranının düşük mü yoksa yüksek mi olduğu konusunda yorum yapabilmek için işletmenin bulunduğu sektör içinde değerlendirilmesi gerekir.
    PD/DD oranı sermaye  yoğun sektörlerde işe yarayan  bir analiz aracıdır, fakat hizmet sektörü gibi duran varlık ihtiyacı düşük, emek yoğun sektörlerde
    doğru sonuçlar vermeyebilir. Bir işletmenin patent,şerefiye,marka gibi maddi olmayan duran varlıklarının  muhasebe değeri ile gerçek değeri arasında
    oldukça büyük farklar olabilir. Böyle bir işletmenin defter değeri düşük olacağından pd/dd oranı yüksek hesaplanacaktır, bu da hisse senedinin  defter
    değerinin çok üzerinde  bir fiyattan işlem gördüğü şeklinde hatalı bir yorum yapılmasına neden olabilir. Özetle, PD/DD oranının sanayi sektörlerinde
    ya da yüksek dönen varlıklar ile  faaliyet gösteren finans sektöründe kullanılması daha doğrudur.""").place(x=0,y=15)
def pgpddd_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
pgpddd1=tk.Button(tab16,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=pgpddd_1).place(x=10,y=25)
pgpddd2=tk.Button(tab16,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=pgpddd_2).place(x=285,y=25)
pgpddd3=tk.Button(tab16,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=pgpddd_3).place(x=285,y=210)
#kullanıcıdan input için label ekleniyor
pgpddd_label1=ttk.Label(tab16,text="Borsa Fiyatı :",style="BW.TLabel").place(x=10,y=70)
pgpddd_label2=ttk.Label(tab16,text="Ödenmiş Sermaye :",style="BW.TLabel").place(x=10,y=105)
pgpddd_label3=ttk.Label(tab16,text="Özsermaye Sermaye :",style="BW.TLabel").place(x=10,y=140)
pgpddd_label4=ttk.Label(tab16,text="Piyasa Değeri/Defter Değeri :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)

#input alanı oluşturuyoruz
pgpddd_entry1=tk.Entry(tab16,width=15,background=background102)
pgpddd_entry2=tk.Entry(tab16,width=15,background=background102)
pgpddd_entry3=tk.Entry(tab16,width=15,background=background102)
#input box'ları yerleştiriyoruz
pgpddd_entry1.place(x=285,y=70)
pgpddd_entry2.place(x=285,y=105)
pgpddd_entry3.place(x=285,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
pgpddd_label_sonuc=ttk.Label(tab16,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
pgpddd_label_sonuc.place(x=285,y=175)

######################################################################################################################################################
"""(9) PİYASA GÖSTERGESİ TEMETTÜ VERİMİ İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab17)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def pgtm_1():
    ap=tk.Tk()
    ap.geometry("380x120")
    ap.title("Temettü Verimi")
    label1=tk.Label(ap,text="""
        Temettü verimi=Hisse başı ödenen temettü/Hisse senedi fiyatı
        veya
        Temettü verimi=Toplam ödenen temettü/Şirketin piyasa değeri
                            """).place(x=0,y=15)
#Açıklama
def pgtm_2():
    ap=tk.Tk()
    ap.geometry("465x100")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Bir şirketin hisse senedi fiyatına göre ne kadar temettü dağıttığını gösteren orandır.""").place(x=0,y=15)
def pgtm_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
pgtm1=tk.Button(tab17,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=pgtm_1).place(x=10,y=25)
pgtm2=tk.Button(tab17,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=pgtm_2).place(x=285,y=25)
pgtm3=tk.Button(tab17,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=pgtm_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
pgtm_label1=ttk.Label(tab17,text="Toplam Ödenen Temettü :",style="BW.TLabel").place(x=10,y=70)
pgtm_label2=ttk.Label(tab17,text="Şirketin Piyasa Değeri :",style="BW.TLabel").place(x=10,y=105)
pgtm_label3=ttk.Label(tab17,text="Temettü Verimi :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
pgtm_entry1=tk.Entry(tab17,width=15,background=background102)
pgtm_entry2=tk.Entry(tab17,width=15,background=background102)
#input box'ları yerleştiriyoruz
pgtm_entry1.place(x=285,y=70)
pgtm_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
pgtm_label_sonuc=ttk.Label(tab17,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
pgtm_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(10) LİKİDİTE ORANI CARİ ORAN İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab18)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def loco_1():
    ap=tk.Tk()
    ap.geometry("380x120")
    ap.title("Cari Oran")
    label1=tk.Label(ap,text="""
        Cari Oran = Dönen Varlıklar / Kısa Vadeli Yabancı Kaynaklar
                            """).place(x=0,y=15)
#Açıklama
def loco_2():
    ap=tk.Tk()
    ap.geometry("900x225")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Kısa vadeli borçların ödeyebilme gücünü gösterir. Oranın 2.00'ın üzerinde olması arzu edilir. İşletmeye kredi vermek isteyen banka gibi kuruluşların
    ilk bakacağı oran, cari oran olacaktır. Eğer oran, arzu edilen düzeyin altında ise işletmeye kredi verilmeyebilir.

    Cari oran, likidite oranları içerisinde en yaygın olarak kullanılan orandır. Şirketin 1 yıl içerisinde ödemesi gereken borç tutarının, bir yıl içerisinde nakde
    dönüştürülebilecek olan varlıklardan az mı çok mu olduğunu gösterir. Bu problemin çözümü için yeni borçlanma ihtiyacı doğar. Yeni borç alınca hem
    yükümlülükler hem de şirketin finansman gideri artmakta, bunun sonucunda da net kâr azalmaktadır. Genelde bu oranın 2 olması şirket için güvenlik sınırı olarak
    kabul edilir. Oranın 1'den aşağıda olmaması ise kesin tercih olmalıdır. Cari oranı hesaplarken kullandığımız dönen varlıklara şirketin stokları da dahildir.
    Eğer şirketin stok devir hızı yüksekse yani stoklarını kısa sürede elden çıkarabiliyorsa o zaman cari oranımızın 2 olmasına gerek yok ama 1'in altında olması
    iyiye işaret değildir, bu yüzden minimum değer olarak genellikle 1 kabul edilir.""").place(x=0,y=15)
def loco_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
loco1=tk.Button(tab18,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=loco_1).place(x=10,y=25)
loco2=tk.Button(tab18,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=loco_2).place(x=285,y=25)
loco3=tk.Button(tab18,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=loco_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
loco_label1=ttk.Label(tab18,text="Dönen Varlıklar :",style="BW.TLabel").place(x=10,y=70)
loco_label2=ttk.Label(tab18,text="Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=105)
loco_label3=ttk.Label(tab18,text="Cari Oran :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
loco_entry1=tk.Entry(tab18,width=15,background=background102)
loco_entry2=tk.Entry(tab18,width=15,background=background102)
#input box'ları yerleştiriyoruz
loco_entry1.place(x=285,y=70)
loco_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
loco_label_sonuc=ttk.Label(tab18,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
loco_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(11) LİKİDİTE ORANI ASİT-TEST ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab19)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def loato_1():
    ap=tk.Tk()
    ap.geometry("440x90")
    ap.title("Asit-test Oranı")
    label1=tk.Label(ap,text="""
        Asit - Test Oranı = (Dönen Varlıklar - Stoklar) / Kısa Vadeli Yabancı Kaynaklar
                            """).place(x=0,y=15)
#Açıklama
def loato_2():
    ap=tk.Tk()
    ap.geometry("900x180")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Asit-test Oranı, Cari orana benzerdir; fakat cari orandan daha anlamlı sonuçlar verir. Stokların dönen varlıklardan çıkarılmasındaki amaç, bu hesap grubundaki
    varlıkların paraya çevrilmesinin uzun zaman almasından kaynaklanmaktadır. Bu şekilde kısa vadeli borçların tamamının likit dönen varlıklar
    ile süratle ödenip ödenemeyeceği anlaşılabilir.

    Oranın 1.00'ın üzerinde olması arzu edilir. Eğer bu oran 1'in üzerindeyse şirket kısa vadeli yükümlülüklerini karşılamakta problem yaşamayacaktır.
    1’in altındaysa eğer pazarda büyük bir talep düşüklüğü yoksa, ciddi bir ekonomik kriz söz konusu değilse şirketler stoklarını satarak nakit yaratabilir. """).place(x=0,y=15)
def loato_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
loato1=tk.Button(tab19,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=loato_1).place(x=10,y=25)
loato2=tk.Button(tab19,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=loato_2).place(x=285,y=25)
loato3=tk.Button(tab19,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=loato_3).place(x=285,y=210)
#kullanıcıdan input için label ekleniyor
loato_label1=ttk.Label(tab19,text="Dönen Varlıklar :",style="BW.TLabel").place(x=10,y=70)
loato_label2=ttk.Label(tab19,text="Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=105)
loato_label3=ttk.Label(tab19,text="Stoklar :",style="BW.TLabel").place(x=10,y=140)
loato_label4=ttk.Label(tab19,text="Asit-test Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
loato_entry1=tk.Entry(tab19,width=15,background=background102)
loato_entry2=tk.Entry(tab19,width=15,background=background102)
loato_entry3=tk.Entry(tab19,width=15,background=background102)
#input box'ları yerleştiriyoruz
loato_entry1.place(x=285,y=70)
loato_entry2.place(x=285,y=105)
loato_entry3.place(x=285,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
loato_label_sonuc=ttk.Label(tab19,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
loato_label_sonuc.place(x=285,y=175)

######################################################################################################################################################
"""(12) LİKİDİTE ORANI NAKİT ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab20)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def lono_1():
    ap=tk.Tk()
    ap.geometry("500x100")
    ap.title("Asit-test Oranı")
    label1=tk.Label(ap,text="""
        Nakit Oranı = (Hazır Değerler + Menkul Kıymetler) / Kısa Vadeli Borçlar
                            """).place(x=0,y=15)
#Açıklama
def lono_2():
    ap=tk.Tk()
    ap.geometry("880x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    İşletmeye hiçbir nakit girişi olmaması durumunda elde bulunan nakitler ve menkul kıymetlerle kısa vadeli borçların ne kadarının ödenebileceğini gösterir.
    Oranın 1.00'ın üzerinde olması arzu edilir.
    Şirketin stoklarını azaltabilmesi veya alacaklarını tahsil edip edememesi gibi belirsizlikleri analiz etmek için kullanılan bir orandır.
    Kriz zamanları dışında çok kullanılmamaktadır. Eğer oran 1'in üzerindeyse şirket ekonomik bir krize karşı dahi çok dayanıklıdır denilebilir. """).place(x=0,y=15)
def lono_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
lono1=tk.Button(tab20,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=lono_1).place(x=10,y=25)
lono2=tk.Button(tab20,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=lono_2).place(x=285,y=25)
lono3=tk.Button(tab20,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=lono_3).place(x=285,y=210)
#kullanıcıdan input için label ekleniyor
lono_label1=ttk.Label(tab20,text="Hazır Değerler :",style="BW.TLabel").place(x=10,y=70)
lono_label2=ttk.Label(tab20,text="Menkul Kıymetler :",style="BW.TLabel").place(x=10,y=105)
lono_label3=ttk.Label(tab20,text="Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=140)
lono_label4=ttk.Label(tab20,text="Nakit Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
lono_entry1=tk.Entry(tab20,width=15,background=background102)
lono_entry2=tk.Entry(tab20,width=15,background=background102)
lono_entry3=tk.Entry(tab20,width=15,background=background102)
#input box'ları yerleştiriyoruz
lono_entry1.place(x=285,y=70)
lono_entry2.place(x=285,y=105)
lono_entry3.place(x=285,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
lono_label_sonuc=ttk.Label(tab20,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
lono_label_sonuc.place(x=285,y=175)

######################################################################################################################################################
"""(13) LİKİDİTE ORANI STOK BAĞIMLILIK ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab21)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def losbo_1():
    ap=tk.Tk()
    ap.geometry("550x100")
    ap.title("Stok Bağımlılık Oranı")
    label1=tk.Label(ap,text="""
        Stok Bağımlılık Oranı = [Kıs. Vad. Yab. Kaynaklar - (Hazır Değerler + Menkul Kıymetler)] / Stoklar
                            """).place(x=0,y=15)
#Açıklama
def losbo_2():
    ap=tk.Tk()
    ap.geometry("880x200")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Asit - test oranının 1'den küçük çıkması durumunda kısa vadeli borçların ödenebilmesi için stokların yüzde kaçının satılması gerektiğini belirtir. 

    Stok Bağımlılık Oranı ≈ 0.33 varsayalım.
    Yorumu şu şekildedir:
    Stokların en az %33'ü satılmalı ki asit - test oranı 1'in üzerine çıkabilsin.

    Stok bağımlılık oranı asit test oranının 1 ‘den küçük olması durumunda borçların geri ödenmesinde işletmenin stoklara bağımlılığını ölçen oran olarak
    da tanımlanmaktadır. Asit test oranının 1’den büyük olması durumunda stoklar dışındaki dönen varlıklar, kısa vadeli yabancı kaynakları ödemeye yetecektir.
    Bu durumunda stok bağımlılık oranını hesaplamaya gerek yoktur. """).place(x=0,y=15)
def losbo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
losbo1=tk.Button(tab21,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=losbo_1).place(x=10,y=25)
losbo2=tk.Button(tab21,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=losbo_2).place(x=285,y=25)
losbo3=tk.Button(tab21,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=losbo_3).place(x=285,y=245)
#kullanıcıdan input için label ekleniyor
losbo_label1=ttk.Label(tab21,text="Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=70)
losbo_label2=ttk.Label(tab21,text="Hazır Değerler :",style="BW.TLabel").place(x=10,y=105)
losbo_label3=ttk.Label(tab21,text="Menkul Kıymetler :",style="BW.TLabel").place(x=10,y=140)
losbo_label4=ttk.Label(tab21,text="Stoklar :",style="BW.TLabel").place(x=10,y=175)
losbo_label5=ttk.Label(tab21,text="Stok Bağımlılık Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=210)
#input alanı oluşturuyoruz
losbo_entry1=tk.Entry(tab21,width=15,background=background102)
losbo_entry2=tk.Entry(tab21,width=15,background=background102)
losbo_entry3=tk.Entry(tab21,width=15,background=background102)
losbo_entry4=tk.Entry(tab21,width=15,background=background102)
#input box'ları yerleştiriyoruz
losbo_entry1.place(x=285,y=70)
losbo_entry2.place(x=285,y=105)
losbo_entry3.place(x=285,y=140)
losbo_entry4.place(x=285,y=175)
#Sonucu yazdıracağımız label'i oluşturuyoruz
losbo_label_sonuc=ttk.Label(tab21,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
losbo_label_sonuc.place(x=285,y=210)

######################################################################################################################################################
"""(14) LİKİDİTE ORANI NET İŞLETME SERMAYESİ / TOPLAM AKTİFLER İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab22)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def lonista_1():
    ap=tk.Tk()
    ap.geometry("550x100")
    ap.title("Net İşletme Sermayesi/Toplam Aktifler Oranı")
    label1=tk.Label(ap,text="""
        Net işletme sermayesi/Aktifler Oranı=(Dönen Varlıklar-Kısa Vadeli Borçlar)/Toplam Aktifler
                            """).place(x=0,y=15)
#Açıklama
def lonista_2():
    ap=tk.Tk()
    ap.geometry("800x160")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Bu oran bize şirketlerin faaliyetlerine devam etmek için gereksinim duydukları net işletme sermaye tutarının aktiflerin içindeki yüzdesel dilimini verir.
    Bu oranla yapılan analizlerde aktiflerin toplam büyüklüğündeki değişiklikler de gözönüne alınmalıdır.

    Net işletme sermayesinin aktifler içindeki oranının şirket ihtiyaçları için optimal düzeyde olup olmadığını ölçmek için, sektör içerisindeki diğer
    şirketlerin oranları ile karşılaştırılabilir veya orandaki değişim miktarı şirketin diğer verilerindeki değişimler (karlılık, net satışlar, likidite
    oranlarındaki değişim miktarları..) ile karşılaştırılabilir.""").place(x=0,y=15)
def lonista_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
lonista1=tk.Button(tab22,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=lonista_1).place(x=10,y=25)
lonista2=tk.Button(tab22,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=lonista_2).place(x=285,y=25)
lonista3=tk.Button(tab22,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=lonista_3).place(x=285,y=210)
#kullanıcıdan input için label ekleniyor
lonista_label1=ttk.Label(tab22,text="Dönen Varlıklar :",style="BW.TLabel").place(x=10,y=70)
lonista_label2=ttk.Label(tab22,text="Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=105)
lonista_label3=ttk.Label(tab22,text="Toplam Aktifler :",style="BW.TLabel").place(x=10,y=140)
lonista_label4=ttk.Label(tab22,text="Net İşletme Sermayesi/Aktifler Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
lonista_entry1=tk.Entry(tab22,width=15,background=background102)
lonista_entry2=tk.Entry(tab22,width=15,background=background102)
lonista_entry3=tk.Entry(tab22,width=15,background=background102)
#input box'ları yerleştiriyoruz
lonista_entry1.place(x=285,y=70)
lonista_entry2.place(x=285,y=105)
lonista_entry3.place(x=285,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
lonista_label_sonuc=ttk.Label(tab22,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
lonista_label_sonuc.place(x=285,y=175)

######################################################################################################################################################
"""(15) LİKİDİTE ORANI LİKİT AKTİFLER ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab23)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def lolao_1():
    ap=tk.Tk()
    ap.geometry("350x100")
    ap.title("Likit Aktifler Oranı")
    label1=tk.Label(ap,text="""
        Likit Aktifler/Aktifler Oranı=Likit Aktifler/Toplam Aktifler
                            """).place(x=0,y=15)
#Açıklama
def lolao_2():
    ap=tk.Tk()
    ap.geometry("840x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Şirketlerin, likit aktiflerinin toplam aktifler içerisindeki payını gösteren bu oran ile şirketin aktiflerinin ne derece likit olduğu anlaşılabilir.
    Bu oran alternatif maliyetler ve işletmenin bulunduğu sektörün nakit üretme kapasitesi göz önüne alınarak değerlendirilmelidir. Bu oranın yüksek oluşu,
    şirketin beklenmedik durumlardaki manevra yeteneğini arttırır. """).place(x=0,y=15)
def lolao_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
lolao1=tk.Button(tab23,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=lolao_1).place(x=10,y=25)
lolao2=tk.Button(tab23,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=lolao_2).place(x=285,y=25)
lolao3=tk.Button(tab23,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=lolao_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
lolao_label1=ttk.Label(tab23,text="Likit Aktifler :",style="BW.TLabel").place(x=10,y=70)
lolao_label2=ttk.Label(tab23,text="Toplam Aktifler :",style="BW.TLabel").place(x=10,y=105)
lolao_label3=ttk.Label(tab23,text="Likit Aktifler Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
lolao_entry1=tk.Entry(tab23,width=15,background=background102)
lolao_entry2=tk.Entry(tab23,width=15,background=background102)
#input box'ları yerleştiriyoruz
lolao_entry1.place(x=285,y=70)
lolao_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
lolao_label_sonuc=ttk.Label(tab23,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
lolao_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(16) BORÇLANMA ORANLARI KALDIRAÇ ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab24)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def boko_1():
    ap=tk.Tk()
    ap.geometry("500x80")
    ap.title("Kaldıraç Oranı")
    label1=tk.Label(ap,text="""
    Kaldıraç Oranı = Kısa ve Uzun Vadeli Borçlar(Toplam Borçlar) / Aktif Toplamı
                            """).place(x=0,y=15)
#Açıklama
def boko_2():
    ap=tk.Tk()
    ap.geometry("800x135")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Toplam Borçların, toplam varlıklara bölünmesiyle birlikte bir şirketteki varlıkların ne kadarının borçlar ile finanse edildiği saptanmış olunur. %50'den
    aşağı olması arzu edilir. %50'den yüksek olması işletmenin riskli finanse edildiğinin işaretidir.
    Yüksek borç işletmenin ödeme  riskini arttıracağı için  kreditörler bu oranın  düşük olmasını tercih ederler fakat belirli bir seviyede yabancı kaynak
    kullanımı öz sermaye kârlılığını arttırıyorsa  olumlu karşılanabilir.  Bu durum kaldıraç etkisi olarak adlandırılır. Gelişmekte olan ülkelerde, şirketler
    sermaye kıtlığı sebebiyle daha fazla dış kaynaklı borç almaktadır.""").place(x=0,y=15)
def boko_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
boko1=tk.Button(tab24,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=boko_1).place(x=10,y=25)
boko2=tk.Button(tab24,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=boko_2).place(x=285,y=25)
boko3=tk.Button(tab24,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=boko_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
boko_label1=ttk.Label(tab24,text="Toplam Borçlar :",style="BW.TLabel").place(x=10,y=70)
boko_label2=ttk.Label(tab24,text="Toplam Aktifler :",style="BW.TLabel").place(x=10,y=105)
boko_label3=ttk.Label(tab24,text="Kaldıraç Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
boko_entry1=tk.Entry(tab24,width=15,background=background102)
boko_entry2=tk.Entry(tab24,width=15,background=background102)
#input box'ları yerleştiriyoruz
boko_entry1.place(x=285,y=70)
boko_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
boko_label_sonuc=ttk.Label(tab24,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
boko_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(17) BORÇLANMA ORANLARI FİNANSMAN ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab25)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def bofo_1():
    ap=tk.Tk()
    ap.geometry("550x80")
    ap.title("Finansman Oranı")
    label1=tk.Label(ap,text="""
    Finansman Oranı = Özkaynaklar(Özsermaye) / Kısa ve Uzun Vadeli Borçlar(Toplam Borçlar)
                            """).place(x=0,y=15)
#Açıklama
def bofo_2():
    ap=tk.Tk()
    ap.geometry("900x250")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Finansal bağımsızlığı gösteren en önemli orandır. Oranın 1.00'dan büyük olması arzu edilir.Öz kaynakların,kısa vadeli yabancı kaynaklar ile uzun vadeli
    yabancı kaynaklar toplamına bölünmesiyle bulunan orandır.Bu oran işletmenin mali bağımsızlık derecesini gösterir. Oranın arzu edilen seviyenin altında
    olunması durumunda işletmenin sahiplerinden daha çok üçüncü kişilerce finanse edildiğini gösterir. Bu da işletme için bir risk unsurudur.

    Bu oran 1 ve 1’e yakın değerler almalıdır. 1 olması özkaynaklar ile yabancı kaynakların aynı oranda kullanıldığı anlamına gelmektedir. 1’den küçük değerler
    alması şirket için risk durumu taşımaktadır. Şirkete yabancı kaynaktan dolayı olağandan fazla faiz yükü getirir.  Yani, şirket borçlarını ödeyememe durumuyla
    karşılaşabilir.

    Oranın 1’den küçük olması durumunda nakit dönüş hızı da önem taşımaktadır. Nitekim, 2009 krizinde ABD’li şirketlerin finansman oranları kabul edilebilir seviyede
    olmasına rağmen nakit dönüş süresi uzadığı için bir çok firma iflas etmiştir.

    Finansman oranının 1’den büyük olması durumunda ise şirketin borçlarını ödeyebileceği ancak, düşük maliyetli uzun dönemli kredilerden yararlanmadığını
    göstermektedir.""").place(x=0,y=15)
def bofo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
bofo1=tk.Button(tab25,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bofo_1).place(x=10,y=25)
bofo2=tk.Button(tab25,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bofo_2).place(x=285,y=25)
bofo3=tk.Button(tab25,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bofo_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
bofo_label1=ttk.Label(tab25,text="Toplam Borçlar :",style="BW.TLabel").place(x=10,y=70)
bofo_label2=ttk.Label(tab25,text="Toplam Aktifler :",style="BW.TLabel").place(x=10,y=105)
bofo_label3=ttk.Label(tab25,text="Kaldıraç Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
bofo_entry1=tk.Entry(tab25,width=15,background=background102)
bofo_entry2=tk.Entry(tab25,width=15,background=background102)
#input box'ları yerleştiriyoruz
bofo_entry1.place(x=285,y=70)
bofo_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
bofo_label_sonuc=ttk.Label(tab25,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
bofo_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(18) BORÇLANMA ORANLARI TOPLAM BORÇLAR/ÖZSERMAYE ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab26)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def botboo_1():
    ap=tk.Tk()
    ap.geometry("500x80")
    ap.title("Toplam Borçlar/Özsermaye Oranı")
    label1=tk.Label(ap,text="""
    Toplam Borçlar/Özsermaye Oranı = Kısa ve Uzun Vadeli Borçlar / Öz Kaynaklar
                            """).place(x=0,y=15)
#Açıklama
def botboo_2():
    ap=tk.Tk()
    ap.geometry("900x310")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Finansman oranının tersidir. Borçlarının yüzde kaçının öz kaynaklar ile karşılandığını gösterir. Oranın 1.00'dan küçük olması arzu edilir.
    borçlanma katsayısı olarak da bilinen bu oran, şirketin, işletme sermayesi ve yatırımlarının finansman ihtiyacını dış kaynaklardan mı (borç) yoksa
    iç kaynaklardan mı (özsermaye) karşıladığını gösteren orandır. Oranın düşük olması işletmenin borçlanarak değil daha çok kendi kaynaklarından finansman
    sağladığını  büyük olması ise işletmenin finansman için agresif borçlanma yolunu tercih ettiğini gösterir. 

    Genel olarak analizlerde bir işletmenin borcunun düşük olması tercih edilir. Borç/Özsermaye oranı yorumlanırken kullanılan borç ve özsermaye arasında denge
    olması tercih edilir.  Örneğin bir işletme  daha fazla borçlanarak  faiz giderlerine karşılık  yaptığı yatırımlar ile  daha fazla gelir elde ediyor  ve borç
    ödemelerinde sorun yaşamıyorsa  bu işletmenin borç özsermaye  oranının yüksek olması  tercih edilebilir.  Farklı bir işletme ise yüksek faiz yükü nedeniyle
    ödeme sıkıntıları çekiyor ve borçlanma karşılığında yeterli geliri elde edemiyor  olabilir.  Bu durumda  işletmenin özvarlıklarıyla  finansman sağlaması
    ya da borçlarını  azaltması daha doğru görülebilir.  Aksi takdirde  şirket iflas  riski ile karşılaşabilir. 

    Borç özsermaye oranı  ilgili işletmenin bulunduğu sektöre göre ve rakiplerine göre  değerlendirilmelidir. bu oranın  genel olarak 1’i aşmaması  istenirken
    sermaye yoğun sektörde  2 ve üzeri,  emek yoğun sektörde 0.5 olması normal karşılanabilir. Çok yüksek bir borç/özsermaye oranı şirketin aşırı borçlu olduğu
    anlamına gelebilir. Bu da onu faiz artışı, eğer döviz borcu varsa kur artışına karşı daha hassas yapabilir. Sonuçta faize ne kadar çok para giderse, hissedarlara
    o kadar az kâr payı kalır. 

    Çok düşük bir borç/sermaye oranı ise şirketin ucuz kaynağı kullanmadığı anlamına gelebilir. Bu da verimsizliğe sebep olabilir.""").place(x=0,y=15)
def botboo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
botboo1=tk.Button(tab26,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=botboo_1).place(x=10,y=25)
botboo2=tk.Button(tab26,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=botboo_2).place(x=285,y=25)
botboo3=tk.Button(tab26,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=botboo_3).place(x=285,y=175)
#kullanıcıdan input için label ekleniyor
botboo_label1=ttk.Label(tab26,text="Toplam Borçlar :",style="BW.TLabel").place(x=10,y=70)
botboo_label2=ttk.Label(tab26,text="Özsermaye :",style="BW.TLabel").place(x=10,y=105)
botboo_label3=ttk.Label(tab26,text="Toplam Borçlar/Özsermaye Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
botboo_entry1=tk.Entry(tab26,width=15,background=background102)
botboo_entry2=tk.Entry(tab26,width=15,background=background102)
#input box'ları yerleştiriyoruz
botboo_entry1.place(x=285,y=70)
botboo_entry2.place(x=285,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
botboo_label_sonuc=ttk.Label(tab26,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
botboo_label_sonuc.place(x=285,y=140)

######################################################################################################################################################
"""(19) BORÇLANMA ORANLARI OTOFİNANSMAN ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab27)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def booo_1():
    ap=tk.Tk()
    ap.geometry("500x80")
    ap.title("Otofinansman Oranı")
    label1=tk.Label(ap,text="""
    Otofinansman Oranı = (Kâr Yedekleri - Geçmiş Yıllar Zararları) / Ödenmiş Sermaye
                            """).place(x=0,y=15)
#Açıklama
def booo_2():
    ap=tk.Tk()
    ap.geometry("880x170")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Otofinansman, işletmenin elde ettiği kârın bir kısmının dağıtılmayıp işletmede bırakılmasıdır. Bu şekilde işletme kendine öz kaynak yaratmış olur.
    Bir şirketin, yatırımlarını kendi iç kaynaklarından finanse etmesidir. Otofinansmanın kaynağını şirketin dağıtılmayan kârları ile ayırdığı akçeler oluşturur.
    Şirketler, finansman ihtiyaçlarını ya dış, ya da iç kaynaklardan karşılayabilirler.

    Otofinansman oranı ise, işletmenin otofinansman yoluyla sağlamış olduğu kaynakların oransal gösterimidir.Bu oranın büyük olması, işletmenin faaliyet
    sonucuna göre iç kaynak yaratabildiği anlamına gelir. Oranın sonucu ne kadar büyük çıkarsa işletme için o kadar iyidir.""").place(x=0,y=15)
def booo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
booo1=tk.Button(tab27,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=booo_1).place(x=10,y=25)
booo2=tk.Button(tab27,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=booo_2).place(x=285,y=25)
booo3=tk.Button(tab27,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=booo_3).place(x=285,y=210)
#kullanıcıdan input için label ekleniyor
booo_label1=ttk.Label(tab27,text="Kâr Yedekleri :",style="BW.TLabel").place(x=10,y=70)
booo_label2=ttk.Label(tab27,text="Geçmiş Yıllar Zararları :",style="BW.TLabel").place(x=10,y=105)
booo_label3=ttk.Label(tab27,text="Ödenmiş Sermaye :",style="BW.TLabel").place(x=10,y=140)
booo_label4=ttk.Label(tab27,text="Otofinansman Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
booo_entry1=tk.Entry(tab27,width=15,background=background102)
booo_entry2=tk.Entry(tab27,width=15,background=background102)
booo_entry3=tk.Entry(tab27,width=15,background=background102)
#input box'ları yerleştiriyoruz
booo_entry1.place(x=285,y=70)
booo_entry2.place(x=285,y=105)
booo_entry3.place(x=285,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
booo_label_sonuc=ttk.Label(tab27,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
booo_label_sonuc.place(x=285,y=175)

######################################################################################################################################################
"""(20) BORÇLANMA ORANLARI MADDİ DURAN VARLIKLAR/ÖZSERMAYE İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab28)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def bomdvo_1():
    ap=tk.Tk()
    ap.geometry("500x80")
    ap.title("Maddi Duran Varlıklar/Özsermaye Oranı")
    label1=tk.Label(ap,text="""
    Oran = Maddî Duran Varlıklar / Özsermaye
                            """).place(x=0,y=15)
#Açıklama
def bomdvo_2():
    ap=tk.Tk()
    ap.geometry("880x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Maddî duran varlıkların ne kadarını öz kaynaklar ile karşılandığını gösterir. Oranın 0.70'den yukarı olması arzu edilir.
    Bu oran şirketin maddi varlıklarının ne kadarının özvarlıklarla finanse edildiğini göstermektedir. Maddi duran varlıklar, fiziki varlıkların şirket
    faaliyetleri için satın alınması  ömrü 1 yıldan fazla olan, hasar görebilir, yıpranabilir ve eskiyebilmeye tabi tutulabilen bilanço kalemleridir.""").place(x=0,y=15)
def bomdvo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
bomdvo1=tk.Button(tab28,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bomdvo_1).place(x=10,y=25)
bomdvo2=tk.Button(tab28,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bomdvo_2).place(x=250,y=25)
bomdvo3=tk.Button(tab28,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bomdvo_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
bomdvo_label1=ttk.Label(tab28,text="Maddi Duran Varlıklar :",style="BW.TLabel").place(x=10,y=70)
bomdvo_label2=ttk.Label(tab28,text="Özsermaye :",style="BW.TLabel").place(x=10,y=105)
bomdvo_label3=ttk.Label(tab28,text="Oran :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
bomdvo_entry1=tk.Entry(tab28,width=15,background=background102)
bomdvo_entry2=tk.Entry(tab28,width=15,background=background102)
#input box'ları yerleştiriyoruz
bomdvo_entry1.place(x=250,y=70)
bomdvo_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
bomdvo_label_sonuc=ttk.Label(tab28,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
bomdvo_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(21) BORÇLANMA ORANLARI DURAN VARLIKLAR/DEVAMLI SERMAYE ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab29)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def bodvdso_1():
    ap=tk.Tk()
    ap.geometry("400x80")
    ap.title("Duran Varlıklar/Devamlı Sermaye Oranı")
    label1=tk.Label(ap,text="""
    Oran = Duran Varlıklar / (Uzun Vadeli Borçlar + Özsermaye)
                            """).place(x=0,y=15)
#Açıklama
def bodvdso_2():
    ap=tk.Tk()
    ap.geometry("650x85")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
     Duran varlıklarının ne kadarının devamlı sermaye ile finanse edildiğini gösterir. Oranın 1.00'dan büyük olması arzu edilir.
     Hatırlanacağı üzere devamlı sermaye, uzun vadeli yabancı kaynaklar ile öz kaynakların toplamını ifade etmektedir.""").place(x=0,y=15)
def bodvdso_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
bodvdso1=tk.Button(tab29,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bodvdso_1).place(x=10,y=25)
bodvdso2=tk.Button(tab29,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bodvdso_2).place(x=250,y=25)
bodvdso3=tk.Button(tab29,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bodvdso_3).place(x=250,y=210)
#kullanıcıdan input için label ekleniyor
bodvdso_label1=ttk.Label(tab29,text="Duran Varlıklar :",style="BW.TLabel").place(x=10,y=70)
bodvdso_label2=ttk.Label(tab29,text="Uzun Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=105)
bodvdso_label3=ttk.Label(tab29,text="Özsermaye :",style="BW.TLabel").place(x=10,y=140)
bodvdso_label4=ttk.Label(tab29,text="Oran :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)

#input alanı oluşturuyoruz
bodvdso_entry1=tk.Entry(tab29,width=15,background=background102)
bodvdso_entry2=tk.Entry(tab29,width=15,background=background102)
bodvdso_entry3=tk.Entry(tab29,width=15,background=background102)

#input box'ları yerleştiriyoruz
bodvdso_entry1.place(x=250,y=70)
bodvdso_entry2.place(x=250,y=105)
bodvdso_entry3.place(x=250,y=140)

#Sonucu yazdıracağımız label'i oluşturuyoruz
bodvdso_label_sonuc=ttk.Label(tab29,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
bodvdso_label_sonuc.place(x=250,y=175)

######################################################################################################################################################
"""(22) FAALİYET ORANLARI ALACAK DEVİR HIZI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab30)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def foadh_1():
    ap=tk.Tk()
    ap.geometry("350x80")
    ap.title("Alacak Devir Hızı")
    label1=tk.Label(ap,text="""
    Alacak Devir Hızı = Kredili Net Satışlar / Ticarî Alacaklar
                            """).place(x=0,y=15)
#Açıklama
def foadh_2():
    ap=tk.Tk()
    ap.geometry("750x190")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    İşletmenin ticarî alacaklarını, gerçekleştirdiği satışlarla yılda kaç kez tahsil ettiğini gösterir. Yüksek olması olumlu yorumlanır.
    Bu oran alacakların tahsil becerisini gösteren bir ölçüdür. Bu orana alacakların paraya dönüşme çabukluğu da denmektedir.
    Bu oranın artması alacakların likidite değerinin de arttığı anlamına gelir. Oranın küçülmesi ise alacakların vadesinin uzadığı anlamına gelir.
    Ortalama ticari alacaklar dönem başı ticari alacaklar ve dönem sonu ticari alacakların toplamının ikiye bölünmesiyle elde edilir.
    Dönem başı alacak tutarı verilmediği takdirde sadece dönem sonu ticari alacak tutarı hesaplamaya katılır.
    Kredili satışların verilmediği durumlarda kredili satışlar yerine “net satışlar” da kullanılmaktadır.
    Ticari alacaklarda net toplam yerine brüt toplamın alınması daha doğru sonucu verecektir.
    Bunun yanı sıra “Verilen depozito ve teminatlar hesabı ticari alacaklara dahil edilmemesi gerekir.""").place(x=0,y=15)
def foadh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
foadh1=tk.Button(tab30,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=foadh_1).place(x=10,y=25)
foadh2=tk.Button(tab30,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=foadh_2).place(x=250,y=25)
foadh3=tk.Button(tab30,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=foadh_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
foadh_label1=ttk.Label(tab30,text="Kredili Net Satışlar :",style="BW.TLabel").place(x=10,y=70)
foadh_label2=ttk.Label(tab30,text="Ticari Alacaklar :",style="BW.TLabel").place(x=10,y=105)
foadh_label3=ttk.Label(tab30,text="Alacak Devir Hızı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
foadh_entry1=tk.Entry(tab30,width=15,background=background102)
foadh_entry2=tk.Entry(tab30,width=15,background=background102)
#input box'ları yerleştiriyoruz
foadh_entry1.place(x=250,y=70)
foadh_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
foadh_label_sonuc=ttk.Label(tab30,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
foadh_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(23) FAALİYET ORANLARI ORTALAMA TAHSİLAT SÜRESİ İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab31)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def foots_1():
    ap=tk.Tk()
    ap.geometry("300x80")
    ap.title("Ortalama Tahsilat Süresi")
    label1=tk.Label(ap,text="""
    Ortalama Tahsil Süresi = 360 / Alacak Devir Hızı
                            """).place(x=0,y=15)
#Açıklama
def foots_2():
    ap=tk.Tk()
    ap.geometry("830x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    1 yıl içinde alacakların kaç günde bir tahsil edildiğini gösteren orandır. Örneğin, 4 olarak hesaplanan devir hızı, alacakların yılda 4 kez devrettiğini
    ve 360/4= 90 gün tahsilat süresinin olduğunu gösterir. 
    Alacakların ortalama kaç günde tahsil edildiğini gösterir. Düşük olması olumlu yorumlanır.
    Alacak devir hızının düşük olması alacakların daha uzun sürede tahsil edildiğini göstermektedir. Alacak devir hızının yüksek olması işletme için pozitif
    bir durumdur. Alacakların kolaylıkla tahsil edildiğini göstermektedir. Yüksek devir hızında daha düşük cari oran ve likidite oranı ile çalışılabilir.""").place(x=0,y=15)
def foots_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
foots1=tk.Button(tab31,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=foots_1).place(x=10,y=25)
foots2=tk.Button(tab31,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=foots_2).place(x=250,y=25)
foots3=tk.Button(tab31,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=foots_3).place(x=250,y=140)
#kullanıcıdan input için label ekleniyor
foots_label1=ttk.Label(tab31,text="Alacak Devir Hızı :",style="BW.TLabel").place(x=10,y=70)
foots_label2=ttk.Label(tab31,text="Ortalama Tahsilat Süresi :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=105)
#input alanı oluşturuyoruz
foots_entry1=tk.Entry(tab31,width=15,background=background102)
#input box'ları yerleştiriyoruz
foots_entry1.place(x=250,y=70)
#Sonucu yazdıracağımız label'i oluşturuyoruz
foots_label_sonuc=ttk.Label(tab31,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
foots_label_sonuc.place(x=250,y=105)

######################################################################################################################################################
"""(24) FAALİYET ORANLARI MADDİ DURAN VARLIKLAR DEVİR HIZI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab32)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def fomdvh_1():
    ap=tk.Tk()
    ap.geometry("440x80")
    ap.title("Maddi Duran Varlıklar Devir Hızı")
    label1=tk.Label(ap,text="""
    Maddî Duran Varlıklar Devir Hızı = Net Satışlar / Net Maddî Duran Varlıklar
    Net Maddî Duran Varlıklar = Maddî Duran Varlıklar - Birikmiş Amortismanlar
                            """).place(x=0,y=15)
#Açıklama
def fomdvh_2():
    ap=tk.Tk()
    ap.geometry("830x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    İşletmenin maddî duran varlıklara aşırı yatırım yapıp yapmadığını gösterir. Oranın düşük olması işletmede atıl kapasitenin olduğunu gösterir.
    Duran varlık devir hızı duran varlıklara yapılan yatırımın seviyesini belirlemeye yardımcı olur. Oranın düşme eğilimi göstermesi kapasite kullanım oranının
    düştüğünü, duran varlıkların verimli kullanılamadığını gösterirken, oranın artış eğilimine girmesi kapasite kullanım oranının arttığını ve işletmenin duran
    varlıklarını verimli kullandığını gösterir. Genel olarak sanayi işletmelerinde bu oranın 2 olması yeterli görülmektedir.""").place(x=0,y=15)
def fomdvh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
fomdvh1=tk.Button(tab32,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=fomdvh_1).place(x=10,y=25)
fomdvh2=tk.Button(tab32,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=fomdvh_2).place(x=250,y=25)
fomdvh3=tk.Button(tab32,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=fomdvh_3).place(x=250,y=210)
#kullanıcıdan input için label ekleniyor
fomdvh_label1=ttk.Label(tab32,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=70)
fomdvh_label2=ttk.Label(tab32,text="Maddî Duran Varlıklar :",style="BW.TLabel").place(x=10,y=105)
fomdvh_label3=ttk.Label(tab32,text="Birikmiş Amortismanlar :",style="BW.TLabel").place(x=10,y=140)
fomdvh_label4=ttk.Label(tab32,text="Maddî Duran Varlıklar Devir Hızı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
fomdvh_entry1=tk.Entry(tab32,width=15,background=background102)
fomdvh_entry2=tk.Entry(tab32,width=15,background=background102)
fomdvh_entry3=tk.Entry(tab32,width=15,background=background102)
#input box'ları yerleştiriyoruz
fomdvh_entry1.place(x=250,y=70)
fomdvh_entry2.place(x=250,y=105)
fomdvh_entry3.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
fomdvh_label_sonuc=ttk.Label(tab32,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
fomdvh_label_sonuc.place(x=250,y=175)

######################################################################################################################################################
"""(25) FAALİYET ORANLARI STOK DEVİR HIZI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab33)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def fosdh_1():
    ap=tk.Tk()
    ap.geometry("400x80")
    ap.title("Stok Devir Hızı")
    label1=tk.Label(ap,text="""
    Stok Devir Hızı = Satışların Maliyeti / Ortalama Stok
    Ortalama Stok = (Dönem Başı Stok + Dönem Sonu Stok) / 2
                            """).place(x=0,y=15)
#Açıklama
def fosdh_2():
    ap=tk.Tk()
    ap.geometry("920x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Stokların yılda kaç kez yenilendiğini gösterir. Yüksek olması işletmenin sürekli satış yapıp, stoklarını yenilediğini gösterir. Bu yüzden olumlu yorumlanır.
    Stok devir hızı, bir firmanın stoklarında yer alan ürünlerin yıl içerisindeki devir sayısını gösteren bir hesaplama yöntemidir. Başka bir deyişle, firmanın bir
    yıl içerisinde stoklarını kaç kez yenilediğini göstermektedir.Örneğin hızlı tüketim gerektiren gıda ya da çabuk bozulan ürünlerde, stok hızının yüksek olması
    gerekir. Aksi takdirde stoklardaki ürünler bozulabilir ve firma zarara uğrayabilir. Bunun aksine daha uzun süre dayanan ürünlerde (örneğin: elektronik eşyalar)
    stok devir hızı daha düşük olabilir. Bu oran firmanın sattığı ürünlerle göre değişiklik gösterebilir.""").place(x=0,y=15)
def fosdh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
fosdh1=tk.Button(tab33,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=fosdh_1).place(x=10,y=25)
fosdh2=tk.Button(tab33,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=fosdh_2).place(x=250,y=25)
fosdh3=tk.Button(tab33,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=fosdh_3).place(x=250,y=210)
#kullanıcıdan input için label ekleniyor
fosdh_label1=ttk.Label(tab33,text="Satışların Maliyeti :",style="BW.TLabel").place(x=10,y=70)
fosdh_label2=ttk.Label(tab33,text="Dönem Başı Stok :",style="BW.TLabel").place(x=10,y=105)
fosdh_label3=ttk.Label(tab33,text="Dönem Sonu Stok :",style="BW.TLabel").place(x=10,y=140)
fosdh_label4=ttk.Label(tab33,text="Stok Devir Hızı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
fosdh_entry1=tk.Entry(tab33,width=15,background=background102)
fosdh_entry2=tk.Entry(tab33,width=15,background=background102)
fosdh_entry3=tk.Entry(tab33,width=15,background=background102)
#input box'ları yerleştiriyoruz
fosdh_entry1.place(x=250,y=70)
fosdh_entry2.place(x=250,y=105)
fosdh_entry3.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
fosdh_label_sonuc=ttk.Label(tab33,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
fosdh_label_sonuc.place(x=250,y=175)

######################################################################################################################################################
"""(26) FAALİYET ORANLARI STOK DEĞİŞİM SÜRESİ-HIZI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab34)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def fosdeh_1():
    ap=tk.Tk()
    ap.geometry("300x80")
    ap.title("Stok Değişim Hızı")
    label1=tk.Label(ap,text="""
    Stok Değişim Süresi = 360 / Stok Devir Hızı
                            """).place(x=0,y=15)
#Açıklama
def fosdeh_2():
    ap=tk.Tk()
    ap.geometry("520x90")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Stokların ortalama kaç günde bir yenilendiğini gösterir. Düşük olması olumlu yorumlanır.""").place(x=0,y=15)
def fosdeh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
fosdeh1=tk.Button(tab34,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=fosdeh_1).place(x=10,y=25)
fosdeh2=tk.Button(tab34,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=fosdeh_2).place(x=250,y=25)
fosdeh3=tk.Button(tab34,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=fosdeh_3).place(x=250,y=140)
#kullanıcıdan input için label ekleniyor
fosdeh_label1=ttk.Label(tab34,text="Stok Devir Hızı :",style="BW.TLabel").place(x=10,y=70)
fosdeh_label2=ttk.Label(tab34,text="Stok Değişim Hızı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=105)
#input alanı oluşturuyoruz
fosdeh_entry1=tk.Entry(tab34,width=15,background=background102)
#input box'ları yerleştiriyoruz
fosdeh_entry1.place(x=250,y=70)
#Sonucu yazdıracağımız label'i oluşturuyoruz
fosdeh_label_sonuc=ttk.Label(tab34,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
fosdeh_label_sonuc.place(x=250,y=105)


######################################################################################################################################################
"""(27) FAALİYET ORANLARI AKTİF DEVİR HIZI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab35)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def foaktifdh_1():
    ap=tk.Tk()
    ap.geometry("300x80")
    ap.title("Aktif Devir Hızı")
    label1=tk.Label(ap,text="""
    Aktif Devir Hızı = Net Satışlar / Aktif Toplamı
                            """).place(x=0,y=15)
#Açıklama
def foaktifdh_2():
    ap=tk.Tk()
    ap.geometry("860x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    İşletmenin sermaye ağırlıklı çalışıp çalışmadığını gösterir. Yüksek olması olumlu yorumlanır.

    Bu oran sektörden sektöre değişse de, Aktif Devir Hızı 1,5 olan bir şirket makul miktarda iş yapıyor demektir. 2 ve üzerindeki değerlerin oldukça iyi olduğu
    söylenebilir. Aktif Devir Hızı yüksek şirketler genellikle komisyoncu diye tabir edebileceğimiz, sürümden kazanan, üretim yapmayan, sattığı ürüne pek katma
    değer katmayan, düşük kar marjıyla çalışan sektörlerden çıkmaktadır. Hem Aktif Devir Hızı yüksek, hem de yüksek kar marjıyla çalışan şirketler uzun vadeli
    yatırımcı için çok kıymetlidir.Aktif devir hızı düşük şirketin varlıkları büyük ihtimalle atıl duruyordur, etkin şekilde değerlendirilmiyordur.""").place(x=0,y=15)
def foaktifdh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
foaktifdh1=tk.Button(tab35,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=foaktifdh_1).place(x=10,y=25)
foaktifdh2=tk.Button(tab35,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=foaktifdh_2).place(x=250,y=25)
foaktifdh3=tk.Button(tab35,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=foaktifdh_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
foaktifdh_label1=ttk.Label(tab35,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=70)
foaktifdh_label2=ttk.Label(tab35,text="Aktif Toplamı :",style="BW.TLabel").place(x=10,y=105)
foaktifdh_label3=ttk.Label(tab35,text="Aktif Devir Hızı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
foaktifdh_entry1=tk.Entry(tab35,width=15,background=background102)
foaktifdh_entry2=tk.Entry(tab35,width=15,background=background102)
#input box'ları yerleştiriyoruz
foaktifdh_entry1.place(x=250,y=70)
foaktifdh_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
foaktifdh_label_sonuc=ttk.Label(tab35,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
foaktifdh_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(28) FAALİYET ORANLARI TİCARİ BORÇ DEVİR HIZI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab36)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def fotbdh_1():
    ap=tk.Tk()
    ap.geometry("450x80")
    ap.title("Aktif Devir Hızı")
    label1=tk.Label(ap,text="""
    Ticarî Borç Devir Hızı = Satışların Maliyeti / Ortalama Ticarî Borçlar
    Ortalama Ticarî Borçlar = (Dönem Başı Ticarî Borç + Dönem Sonu Ticarî Borç)
                            """).place(x=0,y=15)
#Açıklama
def fotbdh_2():
    ap=tk.Tk()
    ap.geometry("860x100")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Ticarî borçların ne hızda ödendiğini gösterir. Oranın düşük olması şirketin ticari borçlarını geri ödemede rahat olduğunu ortaya koyar ve bu durumda şirketin
    cari ve likidite oranları düşük olsa bile, ticari borçlarını geri ödemede rahat olduğunu gösterir. Oranın zamanla yükselme eğiliminde olması ise, şirketin
    faaliyetlerini (aynı hacimde olmak koşuluyla) yürütürken gitgide daha fazla işletme sermayesine gereksinim duyacağını gösterir.""").place(x=0,y=15)
def fotbdh_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
fotbdh1=tk.Button(tab36,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=fotbdh_1).place(x=10,y=25)
fotbdh2=tk.Button(tab36,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=fotbdh_2).place(x=250,y=25)
fotbdh3=tk.Button(tab36,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=fotbdh_3).place(x=250,y=210)
#kullanıcıdan input için label ekleniyor
fotbdh_label1=ttk.Label(tab36,text="Satışların Maliyeti :",style="BW.TLabel").place(x=10,y=70)
fotbdh_label2=ttk.Label(tab36,text="Dönem Başı Ticari Borç :",style="BW.TLabel").place(x=10,y=105)
fotbdh_label3=ttk.Label(tab36,text="Dönem Sonu Ticari Borç :",style="BW.TLabel").place(x=10,y=140)
fotbdh_label4=ttk.Label(tab36,text="Ticari Borç Devir Hızı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
fotbdh_entry1=tk.Entry(tab36,width=15,background=background102)
fotbdh_entry2=tk.Entry(tab36,width=15,background=background102)
fotbdh_entry3=tk.Entry(tab36,width=15,background=background102)
#input box'ları yerleştiriyoruz
fotbdh_entry1.place(x=250,y=70)
fotbdh_entry2.place(x=250,y=105)
fotbdh_entry3.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
fotbdh_label_sonuc=ttk.Label(tab36,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
fotbdh_label_sonuc.place(x=250,y=175)

######################################################################################################################################################
"""(29) KÂRLILIK ORANLARI ÖZSERMAYE KÂRLILIĞI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab37)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def kook_1():
    ap=tk.Tk()
    ap.geometry("450x80")
    ap.title("Özsermaye Kârlılığı")
    label1=tk.Label(ap,text="""
    Malî Rantabilite = Net Kâr / Ortalama Öz Sermaye
    Ortalama Öz Sermaye = (Dönem Başı Öz Sermaye + Dönem Sonu Öz Sermaye) / 2
                            """).place(x=0,y=15)
#Açıklama
def kook_2():
    ap=tk.Tk()
    ap.geometry("900x225")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    İşletmenin öz sermayesi ile net kârı arasındaki ilişkiyi ortaya koyar. Yüksek olması işletme rantabilitesinin tatmin edici düzeyde olduğunu gösterir.
    Not: Net kârdan kasıt dönem net kârıdır.Özsermaye, şirketlerin başlıca kaynaklarından biri olup, şirketlerin ortaklarının şirketlerden hak ettikleri kısmı
    oluşturmaktadır. Öz sermayeyi oluşturan kaynak kalemleri, ortakların koymuş oldukları sermaye ile hak ettikleri fakat şirkette bırakmış oldukları cari ve geçmiş
    dönemden dağıtılmamış karlardan oluşmaktadır.

    Öz Sermaye karlılığı ise, ortakların şirkete kaynak olarak bırakmış oldukları fonların bir birimine düşen karlılığı
    ölçen orandır. İşletmenin yönetimindeki başarı derecesi karlılık durumunun analizinde önemli bir göstergedir. Şirketlerin kullanımına bırakılmış olan bu fonları
    getirisinin ölçülmesi bakımından önem arzetmektedir.

    Ödenmiş sermayenin dikkate alındığı hisse başına kar rakamından önemli farkı ise ortakların şirkete
    sağladıkları tüm fonların (öz sermaye) dikkate almasıdır. Yönetimin başarısını ölçmek için kullanılan bu oranı şirkete ortak olan yatırımcılar, katılımlarının
    getirisini görmek için de kullanırlar.""").place(x=0,y=15)
def kook_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
kook1=tk.Button(tab37,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=kook_1).place(x=10,y=25)
kook2=tk.Button(tab37,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=kook_2).place(x=250,y=25)
kook3=tk.Button(tab37,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=kook_3).place(x=250,y=210)
#kullanıcıdan input için label ekleniyor
kook_label1=ttk.Label(tab37,text="Net Kâr :",style="BW.TLabel").place(x=10,y=70)
kook_label2=ttk.Label(tab37,text="Dönem Başı Öz Sermaye :",style="BW.TLabel").place(x=10,y=105)
kook_label3=ttk.Label(tab37,text="Dönem Sonu Öz Sermaye :",style="BW.TLabel").place(x=10,y=140)
kook_label4=ttk.Label(tab37,text="Özsermaye Kârlılığı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
kook_entry1=tk.Entry(tab37,width=15,background=background102)
kook_entry2=tk.Entry(tab37,width=15,background=background102)
kook_entry3=tk.Entry(tab37,width=15,background=background102)
#input box'ları yerleştiriyoruz
kook_entry1.place(x=250,y=70)
kook_entry2.place(x=250,y=105)
kook_entry3.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
kook_label_sonuc=ttk.Label(tab37,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
kook_label_sonuc.place(x=250,y=175)


######################################################################################################################################################
"""(30) KÂRLILIK ORANLARI EKONOMİK KÂRLILIK İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab38)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def koek_1():
    ap=tk.Tk()
    ap.geometry("375x80")
    ap.title("Ekonomik Kârlılık")
    label1=tk.Label(ap,text="""
    Ekonomik Kârlılık = Vergi ve Faiz Öncesi Kâr / Pasif Toplamı
                            """).place(x=0,y=15)
#Açıklama
def koek_2():
    ap=tk.Tk()
    ap.geometry("500x90")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Kaynakların verimli kullanılıp kullanılmadığını gösterir. Yüksek olması olumlu yorumlanır.""").place(x=0,y=15)
def koek_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
koek1=tk.Button(tab38,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=koek_1).place(x=10,y=25)
koek2=tk.Button(tab38,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=koek_2).place(x=250,y=25)
koek3=tk.Button(tab38,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=koek_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
koek_label1=ttk.Label(tab38,text="Vergi ve Faiz Öncesi Kâr :",style="BW.TLabel").place(x=10,y=70)
koek_label2=ttk.Label(tab38,text="Pasif Toplamı :",style="BW.TLabel").place(x=10,y=105)
koek_label3=ttk.Label(tab38,text="Ekonomik Kârlılık :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
koek_entry1=tk.Entry(tab38,width=15,background=background102)
koek_entry2=tk.Entry(tab38,width=15,background=background102)
#input box'ları yerleştiriyoruz
koek_entry1.place(x=250,y=70)
koek_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
koek_label_sonuc=ttk.Label(tab38,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
koek_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(31) KÂRLILIK ORANLARI BRÜT KÂRLILIK İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab39)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def kobk_1():
    ap=tk.Tk()
    ap.geometry("250x80")
    ap.title("Brüt Kârlılık")
    label1=tk.Label(ap,text="""
    Brüt Kârlılık=Brüt Satış Karı/Net Satışlar
                            """).place(x=0,y=15)
#Açıklama
def kobk_2():
    ap=tk.Tk()
    ap.geometry("750x100")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Brüt kar marjını satılan ürünün fiyatı ve maliyeti belirlediğinden, bu etmenlerdeki değişikliklerin iyi bir şekilde takip edilmesi gerekir.
    Brüt kar marjı adet bazındaki satış miktarından bağımsız bir oran olduğundan, şirketlerin karları hakkında bir bilgi vermekten çok rekabet
    gücünün seyri ve diğer firmalarla kıyas yapabilme imkanı tanımaktadır.""").place(x=0,y=15)
def kobk_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
kobk1=tk.Button(tab39,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=kobk_1).place(x=10,y=25)
kobk2=tk.Button(tab39,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=kobk_2).place(x=250,y=25)
kobk3=tk.Button(tab39,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=kobk_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
kobk_label1=ttk.Label(tab39,text="Brüt Satış Kârı :",style="BW.TLabel").place(x=10,y=70)
kobk_label2=ttk.Label(tab39,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=105)
kobk_label3=ttk.Label(tab39,text="Brüt Kârlılık :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
kobk_entry1=tk.Entry(tab39,width=15,background=background102)
kobk_entry2=tk.Entry(tab39,width=15,background=background102)
#input box'ları yerleştiriyoruz
kobk_entry1.place(x=250,y=70)
kobk_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
kobk_label_sonuc=ttk.Label(tab39,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
kobk_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(32) KÂRLILIK ORANLARI NET KÂRLILIK İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab40)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def konk_1():
    ap=tk.Tk()
    ap.geometry("300x80")
    ap.title("Net Kârlılık")
    label1=tk.Label(ap,text="""
    Net Kârlılık=Net Dönem Kârı/Net Satışlar
                            """).place(x=0,y=15)
#Açıklama
def konk_2():
    ap=tk.Tk()
    ap.geometry("800x110")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Net dönem karı, şirketlerin tüm faaliyetlerinin neticelerini yansıtan bir değerdir. Net dönem karını satışlara oranladığımızda net kar
    marjını (oranını) buluruz. Net kar marjı, hesaplamada şirketlerin diğer gelir ve giderleri dikkate alındığından, şirketlerin tüm faaliyet,
    yatırım ve finansman politikaları hakkında yargıya varmamızı sağlayan bir orandır. Ödenecek temettü tutarları net dönem karı üzerinden
    hesaplandığı ve dağıtıldığı için, yatırımcılar açısından net kar marjındaki gelişmelerin ayrı bir önemi vardır. """).place(x=0,y=15)
def konk_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
konk1=tk.Button(tab40,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=konk_1).place(x=10,y=25)
konk2=tk.Button(tab40,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=konk_2).place(x=250,y=25)
konk3=tk.Button(tab40,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=konk_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
konk_label1=ttk.Label(tab40,text="Net Dönem Kârı :",style="BW.TLabel").place(x=10,y=70)
konk_label2=ttk.Label(tab40,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=105)
konk_label3=ttk.Label(tab40,text="Net Kârlılık :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
konk_entry1=tk.Entry(tab40,width=15,background=background102)
konk_entry2=tk.Entry(tab40,width=15,background=background102)
#input box'ları yerleştiriyoruz
konk_entry1.place(x=250,y=70)
konk_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
konk_label_sonuc=ttk.Label(tab40,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
konk_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(33) KÂRLILIK ORANLARI ESAS FAALİYET KÂRLILIĞI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab41)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def koefk_1():
    ap=tk.Tk()
    ap.geometry("250x80")
    ap.title("Esas Faaliyet Kârlılığı")
    label1=tk.Label(ap,text="""
    Esas Faaliyet Kârlılığı=Esas Faaliyet Kârı/Net Satışlar
                            """).place(x=0,y=15)
#Açıklama
def koefk_2():
    ap=tk.Tk()
    ap.geometry("750x110")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Esas faaliyet karlılığı, esas faaliyet kârının satışlara oranı şeklinde hesaplanmaktadır. Bu sebeple brüt kar marjından farklı olarak
    şirketlerin satış faaliyetleri ile ilgili giderleri de dikkate almaktadır. Bu şekilde satışlarını ne kadarlık bir kâr marjı ile
    gerçekleştirdiğini, yani rekabet gücünü ve rekabet gücünün dönemler itibariyle gelişimini gözlemleyebiliriz. Bu kârlılığın büyük
    sermayeye sahip sanayi şirketlerinde yüksek olması istenir. Küçük sermayelerle çalışan işletmelerde ise düşük bir faaliyet karlılığı bile
    tatmin edici olabilir.  """).place(x=0,y=15)
def koefk_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
koefk1=tk.Button(tab41,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=koefk_1).place(x=10,y=25)
koefk2=tk.Button(tab41,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=koefk_2).place(x=250,y=25)
koefk3=tk.Button(tab41,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=koefk_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
koefk_label1=ttk.Label(tab41,text="Esas Faaliyet Kârı :",style="BW.TLabel").place(x=10,y=70)
koefk_label2=ttk.Label(tab41,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=105)
koefk_label3=ttk.Label(tab41,text="Esas Faaliyet Kârlılığı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
koefk_entry1=tk.Entry(tab41,width=15,background=background102)
koefk_entry2=tk.Entry(tab41,width=15,background=background102)
#input box'ları yerleştiriyoruz
koefk_entry1.place(x=250,y=70)
koefk_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
koefk_label_sonuc=ttk.Label(tab41,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
koefk_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(34) KÂRLILIK ORANLARI FAALİYET KÂRLILIĞI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab42)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def kofa_1():
    ap=tk.Tk()
    ap.geometry("250x110")
    ap.title("Faaliyet Kârlılığı")
    label1=tk.Label(ap,text="""
    Faaliyet Kârlılığı=Faaliyet Kârı/Net Satışlar
                            """).place(x=0,y=15)
#Açıklama
def kofa_2():
    ap=tk.Tk()
    ap.geometry("750x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Faaliyet karlılığı=Faaliyet karı/Net satışlar

    Faaliyet karlılığı şirketlerin hem satış, hem de yatırım ve finansman politikaları hakkında bilgi verdiğinden ayrı bir önemi bulunmaktadır.
    Şirketlerin dönemler itibariyle veya aynı dönemlerde benzer şirketler karşısında faaliyetlerini ne kadarlık bir kar marjı ile gerçekleştirdiği,
    yani rekabet gücü ve rekabet gücünün dönemler itibariyle gelişimi ve bunun yanında yöneticilerin başarısı hakkında da bilgi edinebiliriz.
    Faaliyet karlılığını şirketlerin satış, yatırım ve finansman politikaları gibi etmenler belirlediğinden, bu etmenlerdeki değişikliklerin iyi
    bir şekilde takip edilmesi gerekir. Ayrıca bu karlılığın büyük sermayeye sahip sanayi şirketlerinde yüksek olması istenir.
    Küçük sermayelerle çalışan işletmelerde ise düşük bir faaliyet karlılığı bile tatmin edici olabilir. 
    """).place(x=0,y=15)
def kofa_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
kofa1=tk.Button(tab42,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=kofa_1).place(x=10,y=25)
kofa2=tk.Button(tab42,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=kofa_2).place(x=250,y=25)
kofa3=tk.Button(tab42,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=kofa_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
kofa_label1=ttk.Label(tab42,text="Faaliyet Kârı :",style="BW.TLabel").place(x=10,y=70)
kofa_label2=ttk.Label(tab42,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=105)
kofa_label3=ttk.Label(tab42,text="Faaliyet Kârlılığı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
kofa_entry1=tk.Entry(tab42,width=15,background=background102)
kofa_entry2=tk.Entry(tab42,width=15,background=background102)
#input box'ları yerleştiriyoruz
kofa_entry1.place(x=250,y=70)
kofa_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
kofa_label_sonuc=ttk.Label(tab42,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
kofa_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(35) KÂRLILIK ORANLARI FVOK MARJI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab43)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def kofm_1():
    ap=tk.Tk()
    ap.geometry("325x110")
    ap.title("Faiz ve Vergi Öncesi Kârlılık")
    label1=tk.Label(ap,text="""
    Faiz ve Vergi Öncesi Kârlılık=Faiz ve Vergi Öncesi Kâr/Net Satışlar.
    Faiz ve Vergi Öncesi Kâr=(Dönem karı+Finansman giderleri)/Net Satışlar
    """).place(x=0,y=15)
#Açıklama
def kofm_2():
    ap=tk.Tk()
    ap.geometry("760x140")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    FVÖK Marjı ,FVÖK’nın şirketlerin satış tutarına oranlanması sonucu hesaplanmaktadır. FVÖK Marjı ile şirketlerin satış ve atıl fonlarından elde
    ettikleri gelirlerini satış hasılatı rakamlarına oranlayarak, şirketlerin ana faaliyetleri ile yatırım politikalarını ölçmekte olan önemli bir
    göstergeyi hesaplamış oluruz. Vergi ve piyasa faiz oranlarındaki değişimlerden etkilenmeyen bu kar marjı, ţirketlerin geçmiş dönemleriyle en
    rasyonel şekilde karşılaştırma yapma olanağını sağlamaktadır. 
    Faaliyet karı normal hallerde vergi ve faizler ödendikten sonra firma ortaklarına yeterli bir kar sağlayacak düzeyde bulunmalıdır. Eğer bir
    işletmede sermaye satış hacmine oranla oldukça az ise; düşük bir Faaliyet Karı Net Satışlar oranı bile tatmin edici olabilir.  
    """).place(x=0,y=15)
def kofm_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
kofm1=tk.Button(tab43,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=kofm_1).place(x=10,y=25)
kofm2=tk.Button(tab43,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=kofm_2).place(x=250,y=25)
kofm3=tk.Button(tab43,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=kofm_3).place(x=250,y=210)
#kullanıcıdan input için label ekleniyor
kofm_label1=ttk.Label(tab43,text="Dönem Kârı :",style="BW.TLabel").place(x=10,y=70)
kofm_label2=ttk.Label(tab43,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=105)
kofm_label3=ttk.Label(tab43,text="Finansman Giderleri :",style="BW.TLabel").place(x=10,y=140)
kofm_label4=ttk.Label(tab43,text="FVÖK Marjı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
kofm_entry1=tk.Entry(tab43,width=15,background=background102)
kofm_entry2=tk.Entry(tab43,width=15,background=background102)
kofm_entry3=tk.Entry(tab43,width=15,background=background102)
#input box'ları yerleştiriyoruz
kofm_entry1.place(x=250,y=70)
kofm_entry2.place(x=250,y=105)
kofm_entry3.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
kofm_label_sonuc=ttk.Label(tab43,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
kofm_label_sonuc.place(x=250,y=175)


######################################################################################################################################################
"""(36) KÂRLILIK ORANLARI VERGİ/NET SATIŞLAR İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab44)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def kovnso_1():
    ap=tk.Tk()
    ap.geometry("325x80")
    ap.title("Ödenecek Vergi ve Yasal Yükümlülükler/Net Satışlar")
    label1=tk.Label(ap,text="""
    Oran=Ödenecek vergi ve yasal yükümlülükler/Net satışlar
    """).place(x=0,y=15)
#Açıklama
def kovnso_2():
    ap=tk.Tk()
    ap.geometry("830x160")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Bu oran şirketlerin dönem sonlarında elde ettikleri dönem karlarından Maliye Bakanlığının kabul etmiş olduğu gelir ve gider tanımlamasına göre
    bulunan mali kar rakamı üzerinden hesaplanmakta olan Ödenecek Vergi tutarının, şirketlerin gerçekleştirmiş oldukları satış miktarına bölünerek bulunur.
    Şirketlerin faaliyetlerine göre farklılık gösterebilmektedir. 

    Bu oran ile şirketlerin yapmış oldukları 100 birimlik satış karşılığında ödemekle yükümlü oldukları vergi tutarı, özellikle sektörler arası
    kıyaslamada kullanılabilmektedir. Dikkat edilmesi gereken bir diğer husus ise, şirketlerin 100 birimlik satış için ödeyecekleri vergi tutarlarının düşük
    olmasının bir nedeninin de elde edilen düşük net dönem karı olabileceğidir.   
    """).place(x=0,y=15)
def kovnso_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
kovnso1=tk.Button(tab44,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=kovnso_1).place(x=10,y=25)
kovnso2=tk.Button(tab44,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=kovnso_2).place(x=250,y=25)
kovnso3=tk.Button(tab44,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=kovnso_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
kovnso_label1=ttk.Label(tab44,text="Ödenecek Vergi ve Yasal Yükümlülükler :",style="BW.TLabel").place(x=10,y=70)
kovnso_label2=ttk.Label(tab44,text="Net Satışlar :",style="BW.TLabel").place(x=10,y=105)
kovnso_label3=ttk.Label(tab44,text="Oran :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
kovnso_entry1=tk.Entry(tab44,width=15,background=background102)
kovnso_entry2=tk.Entry(tab44,width=15,background=background102)
#input box'ları yerleştiriyoruz
kovnso_entry1.place(x=250,y=70)
kovnso_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
kovnso_label_sonuc=ttk.Label(tab44,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
kovnso_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(37) KÂRLILIK ORANLARI DEVAMLI SERMAYE ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab45)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def kodsk_1():
    ap=tk.Tk()
    ap.geometry("350x80")
    ap.title("Devamlı Sermaye Kârlılığı")
    label1=tk.Label(ap,text="""
    Devamlı Sermaye Kârlılığı=Net Kâr/Ortalama Devamlı Sermaye
    """).place(x=0,y=15)
#Açıklama
def kodsk_2():
    ap=tk.Tk()
    ap.geometry("830x150")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Devamlı sermaye kârlılığı, şirketlerin uzun vadeli kaynakları ile hangi oranda karlı çalıştıklarını ölçmede kullanılan bir orandır.
    Bu kârlılık rakamı ile şirketlerin edinmiş oldukları uzun vadeli kaynaklarını ne kadar optimal kullandıklarını geçmiş dönemlerle ve benzer şirketler
    ile karşılaştırarak ölçebiliriz. 

    Devamlı sermaye karlılığının öz sermaye karlılığından başlıca farkı, gerek ortaklardan gerekse uzun vadeli fon sağlayan kreditörlerden tedarik edinilecek
    fonları karşılamadaki yükümlülüklerini yerine getirip getiremeyeceğini ölçmede kullanılabiliyor olmasıdır.   
    """).place(x=0,y=15)
def kodsk_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
kodsk1=tk.Button(tab45,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=kodsk_1).place(x=10,y=25)
kodsk2=tk.Button(tab45,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=kodsk_2).place(x=250,y=25)
kodsk3=tk.Button(tab45,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=kodsk_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
kodsk_label1=ttk.Label(tab45,text="Net Kâr :",style="BW.TLabel").place(x=10,y=70)
kodsk_label2=ttk.Label(tab45,text="Ortalama Devamlı Sermaye :",style="BW.TLabel").place(x=10,y=105)
kodsk_label3=ttk.Label(tab45,text="Devamlı Sermaye Kârlılığı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
kodsk_entry1=tk.Entry(tab45,width=15,background=background102)
kodsk_entry2=tk.Entry(tab45,width=15,background=background102)
#input box'ları yerleştiriyoruz
kodsk_entry1.place(x=250,y=70)
kodsk_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
kodsk_label_sonuc=ttk.Label(tab45,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
kodsk_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(38) KÂRLILIK ORANLARI AKTİF KÂRLILIĞI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab46)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def koak_1():
    ap=tk.Tk()
    ap.geometry("300x80")
    ap.title("Aktif Kârlılığı")
    label1=tk.Label(ap,text="""
    Aktif Kârlılığı=Net Kâr/Ortalama Toplam Aktifler
    """).place(x=0,y=15)
#Açıklama
def koak_2():
    ap=tk.Tk()
    ap.geometry("830x170")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Aktif kârlılığı, şirketlerin ulaşmış oldukları büyüklük ile sağladıkları verimin ölçülmesinde kullanılır. Aktif kârlılık şirketlerin edinmiş
    oldukları tüm varlıkların (yapılan maddi ve finansal yatırımlar dahil olmak üzere) hangi oranda etkin kullanıldığını göstermektedir. 
    Net kâr, faizler indirildikten sonra kalan tutarı ifade ettiği için bir firmanın finansman şekline göre bu oran önemli değişiklikler göstermektedir.
    Fazla yabancı kaynak kullandığı için ağır faiz yükü altında olan bir firmanın, ağırlıklı olarak kendini özkaynakları ile finanse eden bir firmaya
    kıyasla NetKâr-Aktif Toplamı oranının daha düşük olması olağandır. Firmanın finansman şekline göre farklı sonuçlar veren, pay ve paydası arasında
    tutarlılık bulunmayan bu oranın karlılık analizinde kullanılması fazla anlamlı değildir. Finansman yapıları farklı firmalar arasında karşılaştırma,
    hatta zaman içerisinde ilgili firmanın finansman yapısı değişmiş olabileceğinden geçmiş yıllarla karşılaştırma yapılırken, FVÖK-Aktif toplamı
    oranının kullanılması daha anlamlı olacaktır. 
    """).place(x=0,y=15)
def koak_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
koak1=tk.Button(tab46,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=koak_1).place(x=10,y=25)
koak2=tk.Button(tab46,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=koak_2).place(x=250,y=25)
koak3=tk.Button(tab46,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=koak_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
koak_label1=ttk.Label(tab46,text="Net Kâr :",style="BW.TLabel").place(x=10,y=70)
koak_label2=ttk.Label(tab46,text="Ortalama Toplam Aktifler :",style="BW.TLabel").place(x=10,y=105)
koak_label3=ttk.Label(tab46,text="Aktif Kârlılığı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
koak_entry1=tk.Entry(tab46,width=15,background=background102)
koak_entry2=tk.Entry(tab46,width=15,background=background102)
#input box'ları yerleştiriyoruz
koak_entry1.place(x=250,y=70)
koak_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
koak_label_sonuc=ttk.Label(tab46,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
koak_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(39) KÂRLILIK ORANLARI FİNANSAL GİDERLER/STOKLAR ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab47)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def kofgs_1():
    ap=tk.Tk()
    ap.geometry("360x80")
    ap.title("Finansal Giderler/Stoklar")
    label1=tk.Label(ap,text="""
    Finansal Giderler/Stoklar=Finansman Giderleri/Ortalama Stoklar
    Ortalama Stoklar=(Dönem Başı Stok+Dönem Sonu Stok)/2
    """).place(x=0,y=15)
#Açıklama
def kofgs_2():
    ap=tk.Tk()
    ap.geometry("780x100")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Şirketlerin stok tutarları ile finansal giderler arasındaki ilişkiyi gösteren bu oran, atıl olarak duran stokların fonlama maliyetinin ölçülmesinde
    kullanılmaktadır. Finansal giderler-stoklar oranının dönemler itibariyle yapılacak olan karşılaştırmasında, stokların dönemler itibariyle
    gelişiminin de göz önünde bulundurulması önemli saptamalar yapılmasını sağlayabilir. 
    """).place(x=0,y=15)
def kofgs_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
kofgs1=tk.Button(tab47,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=kofgs_1).place(x=10,y=25)
kofgs2=tk.Button(tab47,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=kofgs_2).place(x=250,y=25)
kofgs3=tk.Button(tab47,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=kofgs_3).place(x=250,y=210)
#kullanıcıdan input için label ekleniyor
kofgs_label1=ttk.Label(tab47,text="Finansman Giderleri :",style="BW.TLabel").place(x=10,y=70)
kofgs_label2=ttk.Label(tab47,text="Dönem Başı Stok :",style="BW.TLabel").place(x=10,y=105)
kofgs_label3=ttk.Label(tab47,text="Dönem Sonu Stok :",style="BW.TLabel").place(x=10,y=140)
kofgs_label4=ttk.Label(tab47,text="Oran :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)
#input alanı oluşturuyoruz
kofgs_entry1=tk.Entry(tab47,width=15,background=background102)
kofgs_entry2=tk.Entry(tab47,width=15,background=background102)
kofgs_entry3=tk.Entry(tab47,width=15,background=background102)
#input box'ları yerleştiriyoruz
kofgs_entry1.place(x=250,y=70)
kofgs_entry2.place(x=250,y=105)
kofgs_entry3.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
kofgs_label_sonuc=ttk.Label(tab47,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
kofgs_label_sonuc.place(x=250,y=175)


######################################################################################################################################################
"""(40) BÜYÜME ORANLARI DEVAMLI SERMAYE BÜYÜME ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab48)"""
######################################################################################################################################################
#Paned window oluşturuluyor

bodsbo_pw1=ttk.Panedwindow(tab48,orient=tk.HORIZONTAL)
bodsbo_pw1.pack(fill=tk.BOTH,expand=True)
bodsbo_pw2=ttk.Panedwindow(tab48,orient=tk.HORIZONTAL)
#Paned window için frame oluşturuluyor
bodsbo_frame1=ttk.Frame(bodsbo_pw1,width=400,height=300,relief=tk.RIDGE)
bodsbo_frame2=ttk.Frame(bodsbo_pw2,width=400,height=300,relief=tk.RAISED)
bodsbo_pw2.add(bodsbo_frame2)
bodsbo_pw1.add(bodsbo_frame1)

bodsbo_pw1.add(bodsbo_pw2)
#KANVASLAR
tema_kanvas48_1=tk.Canvas(bodsbo_frame1,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas48_2=tk.Canvas(bodsbo_frame2,width=1000,height=550,background=backround100).place(x=0,y=0)
#Formülü görmek için tıklayınız
def bodsbo_1():
    ap=tk.Tk()
    ap.geometry("600x80")
    ap.title("Devamlı Sermaye Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Devamlı Sermaye Büyüme Oranı=[(Devamlı Sermaye(güncel)/Devamlı Sermaye(bir önceki dönem))-1]
                            """).place(x=0,y=30)
def bodsbo_11():
    ap=tk.Tk()
    ap.geometry("720x80")
    ap.title("Devamlı Sermaye Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Devamlı Sermaye Büyüme Oranı=([(Uzun Vadeli Borçlar+Özsermaye(güncel))/(Uzun vadeli borçlar+özsermaye(bir önceki dönem))]-1)
                            """).place(x=0,y=30)
#Açıklama
def bodsbo_2():
    ap=tk.Tk()
    ap.geometry("850x240")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Dönemler itibariyle uzun vadeli kaynaklardaki (devamlı sermayedeki) değişiklikleri ölçmede kullanılan devamlı sermaye büyüme oranı, bize
    şirketlerin uzun
    vadeli kaynaklardaki artış hızının diğer şirketlerle kıyas yapılmasına olanak verdiği gibi, toplam aktifler büyüme hızı ile birlikte
    değerlendirme yapıldığında şirketlerin finansman politikaları bakımından uzun vadeli kaynaklara ne kadar yöneldiklerini göstermektedir. 
    Toplam aktifler büyüme oranındaki gelişmenin devamlı sermayenin büyüme oranından küçük olması durumunda, şirketlerin uzun vadeli borç yoluyla
    finansmana daha fazla ağırlık vermeye başladığı şeklinde bir tespitte bulunabiliriz. 

    Dikkat edilmesi gereken nokta ise uzun vadeli kaynak kullanımında bir öz sermaye-uzun vadeli borç dengesinin gözetilip gözetilmediğidir.
    ÖzSermaye büyüme oranının devamlı sermaye büyüme oranından yüksek olması durumunda, şirketlerin daha çok oto-finansmana veya ortaklardan
    bedelli sermaye artırımı yoluyla fon teminine başvurdukları çıkarımı yapılabilir. Dönemler itibarıyla bulunacak artış (büyüme) hızları yardımıyla,
    gelecekte devamlı sermayenin ulaşabileceği büyüklük istatistiksel yöntemlerle tahmin edilebilir. Böylece, şirketlerin devamlı sermaye karlılıkları
    hakkında da öngörüde bulunulursa, gelecek dönemlerde şirketlerin elde edebileceği net dönem karları tahmin edilebilir.""").place(x=0,y=30)
def bodsbo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=8,y=15)
#Pencere açma butonları ekleniyor    
bodsbo1=tk.Button(bodsbo_frame1,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bodsbo_1).place(x=10,y=25)
bodsbo2=tk.Button(bodsbo_frame1,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bodsbo_2).place(x=250,y=25)
bodsbo3=tk.Button(bodsbo_frame1,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bodsbo_3).place(x=250,y=175)

bodsbo4=tk.Button(bodsbo_frame2,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bodsbo_11).place(x=10,y=25)
bodsbo5=tk.Button(bodsbo_frame2,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bodsbo_2).place(x=250,y=25)
bodsbo6=tk.Button(bodsbo_frame2,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bodsbo_3).place(x=250,y=210)

#kullanıcıdan input için label ekleniyor
bodsbo_label1=ttk.Label(bodsbo_frame1,text="Şu anki Devamlı Sermaye :",style="BW.TLabel").place(x=10,y=70)
bodsbo_label2=ttk.Label(bodsbo_frame1,text="Bir Dönem Önceki Devamlı Sermaye :",style="BW.TLabel").place(x=10,y=105)
bodsbo_label3=ttk.Label(bodsbo_frame1,text="Devamlı Sermaye Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)

bodsbo_label4=ttk.Label(bodsbo_frame2,text="Uzun Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=70)
bodsbo_label5=ttk.Label(bodsbo_frame2,text="Şu anki Özsermaye :",style="BW.TLabel").place(x=10,y=105)
bodsbo_label6=ttk.Label(bodsbo_frame2,text="Bir Dönem Önceki Özsermaye :",style="BW.TLabel").place(x=10,y=140)
bodsbo_label7=ttk.Label(bodsbo_frame2,text="Devamlı Sermaye Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)

#input alanı oluşturuyoruz
bodsbo_entry1=tk.Entry(bodsbo_frame1,width=15,background=background102)
bodsbo_entry2=tk.Entry(bodsbo_frame1,width=15,background=background102)

bodsbo_entry3=tk.Entry(bodsbo_frame2,width=15,background=background102)
bodsbo_entry4=tk.Entry(bodsbo_frame2,width=15,background=background102)
bodsbo_entry5=tk.Entry(bodsbo_frame2,width=15,background=background102)

#input box'ları yerleştiriyoruz
bodsbo_entry1.place(x=250,y=70)
bodsbo_entry2.place(x=250,y=105)

bodsbo_entry3.place(x=250,y=70)
bodsbo_entry4.place(x=250,y=105)
bodsbo_entry5.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
bodsbo_label_sonuc=ttk.Label(bodsbo_frame1,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bodsbo_label_sonuc2=ttk.Label(bodsbo_frame2,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))

#Sonucu yazdıracağımız label'i ekliyoruz
bodsbo_label_sonuc.place(x=250,y=140)
bodsbo_label_sonuc2.place(x=250,y=175)
# Label
bodsbo_label_7=tk.Label(bodsbo_frame1,text="Yöntem 1",background=backround100,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",15,"bold"),width=30,height=2)
bodsbo_label_7.place(x=3,y=245)
# Label
bodsbo_label_8=tk.Label(bodsbo_frame2,text="Yöntem 2",background=backround100,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",15,"bold"),width=30,height=2)
bodsbo_label_8.place(x=3,y=280)

######################################################################################################################################################
"""(41) KÂRLILIK ORANLARI NET KÂR BÜYÜME ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab49)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def bonkbo_1():
    ap=tk.Tk()
    ap.geometry("400x100")
    ap.title("Net Kâr Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Net Kâr Büyüme Oranı=[(Net Dönem Kârı(t)/Net Dönem Kârı(t-1)]-1)
    t:dönem
    t-1: önceki dönem
    """).place(x=0,y=15)
#Açıklama
def bonkbo_2():
    ap=tk.Tk()
    ap.geometry("780x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Dönemler itibariyle Net dönem karındaki değişiklikleri ölçmede kullanılan net kar büyüme oranı, şirketlerin karlılığındaki artış hızının diğer
    şirketlerle kıyas yapılmasına olanak verdiği gibi, şirketlerin geçmiş dönemlerde gerçekleşen artış hızları ile de kıyas yapabilmemize imkan tanır.
    Dönemler itibarıyla bulunacak artış (büyüme) hızları yardımıyla, gelecekte şirketlerin elde edebileceği net karlar istatistiksel yöntemlerle
    tahmin edilebilir. Böylece, şirketlerin kar dağıtım oranları da tahmin edilebilirse, dağıtılabilecek kar da (temettü) belirlenebilir. Diğer
    şirketlere kıyasla daha düşük büyüme oranına sahip bir şirketin yeterince iyi yönetilemediği yorumu yapılabilir. 
    """).place(x=0,y=15)
def bonkbo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
bonkbo1=tk.Button(tab49,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bonkbo_1).place(x=10,y=25)
bonkbo2=tk.Button(tab49,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bonkbo_2).place(x=250,y=25)
bonkbo3=tk.Button(tab49,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bonkbo_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
bonkbo_label1=ttk.Label(tab49,text="Şu anki Net Dönem Kârı :",style="BW.TLabel").place(x=10,y=70)
bonkbo_label2=ttk.Label(tab49,text="Bir Dönem Önceki Net Dönem Kârı :",style="BW.TLabel").place(x=10,y=105)
bonkbo_label3=ttk.Label(tab49,text="Net Kâr Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
bonkbo_entry1=tk.Entry(tab49,width=15,background=background102)
bonkbo_entry2=tk.Entry(tab49,width=15,background=background102)
#input box'ları yerleştiriyoruz
bonkbo_entry1.place(x=250,y=70)
bonkbo_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
bonkbo_label_sonuc=ttk.Label(tab49,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
bonkbo_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(42) KÂRLILIK ORANLARI NET SATIŞLAR BÜYÜME ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab50)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def bonsbo_1():
    ap=tk.Tk()
    ap.geometry("490x90")
    ap.title("Net Satışlar Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Net Satışlar Büyüme Oranı=(Net Satışlar(güncel)/Net satışlar(bir önceki dönem))-1

    """).place(x=0,y=15)
#Açıklama
def bonsbo_2():
    ap=tk.Tk()
    ap.geometry("780x160")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Dönemler itibarıyla net satış tutarlarındaki değişiklikleri ölçmede kullanılan net satışlar büyüme oranı, bize şirketlerin satışlarındaki
    artış hızının diğer şirketlerle kıyas yapılmasına olanak verdiği gibi, şirketlerin gelecekteki pazar payı dağılımı hakkında tahmini
    öngörüler yapabilmemize olanak tanır. Dönemler itibariyle bulunacak artış (büyüme) hızları yardımıyla, gelecekte şirketlerin elde edebileceği
    net satışlar istatistiksel yöntemlerle tahmin edilebilir. Böylece, şirketlerin net kar marjları da tahmin edilebilirse, gelecek dönemlerde
    şirketlerin elde edebileceği net dönem karları tahmin edilebilir. Diğer şirketlere kıyasla daha düşük büyüme oranına sahip bir şirketin
    yeterince iyi yönetilemediği yorumu yapılabilir. Ancak unutulmaması gereken önemli nokta satışlardaki büyümenin şirket performansı hakkında,
    tek başına belirleyici olamayacağıdır. Maliyetlerdeki artış oranının da incelenmesi gerekir. 
    """).place(x=0,y=15)
def bonsbo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
bonsbo1=tk.Button(tab50,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bonsbo_1).place(x=10,y=25)
bonsbo2=tk.Button(tab50,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bonsbo_2).place(x=250,y=25)
bonsbo3=tk.Button(tab50,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bonsbo_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
bonsbo_label1=ttk.Label(tab50,text="Şu anki Net Satışlar :",style="BW.TLabel").place(x=10,y=70)
bonsbo_label2=ttk.Label(tab50,text="Bir Dönem Önceki Net Satışlar :",style="BW.TLabel").place(x=10,y=105)
bonsbo_label3=ttk.Label(tab50,text="Net Satışlar Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
bonsbo_entry1=tk.Entry(tab50,width=15,background=background102)
bonsbo_entry2=tk.Entry(tab50,width=15,background=background102)
#input box'ları yerleştiriyoruz
bonsbo_entry1.place(x=250,y=70)
bonsbo_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
bonsbo_label_sonuc=ttk.Label(tab50,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
bonsbo_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(43) BÜYÜME ORANLARI NET İŞLETME SERMAYESİ BÜYÜME ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab51)"""
######################################################################################################################################################
#Paned window oluşturuluyor

bonisbo_pw1=ttk.Panedwindow(tab51,orient=tk.HORIZONTAL)
bonisbo_pw1.pack(fill=tk.BOTH,expand=True)
bonisbo_pw2=ttk.Panedwindow(tab51,orient=tk.HORIZONTAL)
#Paned window için frame oluşturuluyor
bonisbo_frame1=ttk.Frame(bonisbo_pw1,width=400,height=300,relief=tk.RIDGE)
bonisbo_frame2=ttk.Frame(bonisbo_pw2,width=400,height=300,relief=tk.RAISED)
bonisbo_pw2.add(bonisbo_frame2)
bonisbo_pw1.add(bonisbo_frame1)

bonisbo_pw1.add(bonisbo_pw2)
#KANVASLAR
tema_kanvas43_1=tk.Canvas(bonisbo_frame1,width=1000,height=550,background=backround100).place(x=0,y=0)
tema_kanvas43_2=tk.Canvas(bonisbo_frame2,width=1000,height=550,background=backround100).place(x=0,y=0)
#Formülü görmek için tıklayınız
def bonisbo_1():
    ap=tk.Tk()
    ap.geometry("680x90")
    ap.title("Net İşletme Sermayesi Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Net İşletme Sermayesi Büyüme Oranı=((Net İşletme Sermayesi(güncel)/Net İşletme Sermayesi(bir önceki dönem))-1)
     Not:Bilanço ve/veya gelir tablosunda (-) olarak görülen gider ve borç kalemleri
     formüllerde mutlak değerleri alınarak kullanılmalıdır.
                            """).place(x=0,y=15)
def bonisbo_11():
    ap=tk.Tk()
    ap.geometry("720x100")
    ap.title("Net İşletme Sermayesi Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Net İşletme Sermayesi Büyüme Oranı=((Dönen Varlıklar-Kısa Vadeli Borçlar(güncel))/(Dönen Varlıklar-Kısa Vadeli Borçlar(bir önceki dönem))-1)
     Not:Bilanço ve/veya gelir tablosunda (-) olarak görülen gider ve borç kalemleri
     formüllerde mutlak değerleri alınarak kullanılmalıdır.
                            """).place(x=0,y=15)
#Açıklama
def bonisbo_2():
    ap=tk.Tk()
    ap.geometry("800x150")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Dönemler itibarıyla Net işletme sermayesindeki değişiklikleri ölçmede kullanılan Net işletme sermaye büyüme oranı, bize şirketlerin
    Net işletme sermayesindeki artış hızının diğer şirketlerle kıyas yapılmasına olanak verdiği gibi, şirketlerin faaliyetleri sonucu
    nakit yaratma güçleri hakkında da bilgi vermektedir. Aktiflerdeki büyüme oranı ve satışlardaki büyüme oranı ile beraber
    değerlendirildiğinde Net İşletme Sermaye büyüme oranının yeterli olup olmadığı hakkında daha doğru saptamalarda bulunulabilir.
    Böylece şirketlerin nakit ihtiyacı içerisinde bulunup bulunmadığı veya atıl olarak nakit tutup tutmadığı daha iyi tespit edilir.""").place(x=0,y=30)
def bonisbo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)
#Pencere açma butonları ekleniyor    
bonisbo1=tk.Button(bonisbo_frame1,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bonisbo_1).place(x=10,y=25)
bonisbo2=tk.Button(bonisbo_frame1,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bonisbo_2).place(x=250,y=25)
bonisbo3=tk.Button(bonisbo_frame1,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bonisbo_3).place(x=250,y=175)

bonisbo4=tk.Button(bonisbo_frame2,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=bonisbo_11).place(x=10,y=25)
bonisbo5=tk.Button(bonisbo_frame2,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=bonisbo_2).place(x=250,y=25)
bonisbo6=tk.Button(bonisbo_frame2,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=bonisbo_3).place(x=250,y=210)

#kullanıcıdan input için label ekleniyor
bonisbo_label1=ttk.Label(bonisbo_frame1,text="Şu anki Net İşletme Sermayesi :",style="BW.TLabel").place(x=10,y=70)
bonisbo_label2=ttk.Label(bonisbo_frame1,text="Bir Dönem Önceki Net İşletme Sermayesi :",style="BW.TLabel").place(x=10,y=105)
bonisbo_label3=ttk.Label(bonisbo_frame1,text="Net İşletme Sermayesi Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)

bonisbo_label4=ttk.Label(bonisbo_frame2,text="Dönen Varlıklar :",style="BW.TLabel").place(x=10,y=70)
bonisbo_label5=ttk.Label(bonisbo_frame2,text="Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=105)
bonisbo_label6=ttk.Label(bonisbo_frame2,text="Bir Dönem Önceki Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=140)
bonisbo_label7=ttk.Label(bonisbo_frame2,text="Net İşletme Sermayesi Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=175)

#input alanı oluşturuyoruz
bonisbo_entry1=tk.Entry(bonisbo_frame1,width=15,background=background102)
bonisbo_entry2=tk.Entry(bonisbo_frame1,width=15,background=background102)

bonisbo_entry3=tk.Entry(bonisbo_frame2,width=15,background=background102)
bonisbo_entry4=tk.Entry(bonisbo_frame2,width=15,background=background102)
bonisbo_entry5=tk.Entry(bonisbo_frame2,width=15,background=background102)

#input box'ları yerleştiriyoruz
bonisbo_entry1.place(x=250,y=70)
bonisbo_entry2.place(x=250,y=105)

bonisbo_entry3.place(x=250,y=70)
bonisbo_entry4.place(x=250,y=105)
bonisbo_entry5.place(x=250,y=140)
#Sonucu yazdıracağımız label'i oluşturuyoruz
bonisbo_label_sonuc=ttk.Label(bonisbo_frame1,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
bonisbo_label_sonuc2=ttk.Label(bonisbo_frame2,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))

#Sonucu yazdıracağımız label'i ekliyoruz
bonisbo_label_sonuc.place(x=250,y=140)
bonisbo_label_sonuc2.place(x=250,y=175)
# Label
bonisbo_label_7=tk.Label(bonisbo_frame1,text="Yöntem 1",background=backround100,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",15,"bold"),width=30,height=2)
bonisbo_label_7.place(x=3,y=245)
# Label
bonisbo_label_8=tk.Label(bonisbo_frame2,text="Yöntem 2",background=backround100,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",15,"bold"),width=30,height=2)
bonisbo_label_8.place(x=3,y=280)


######################################################################################################################################################
"""(44) BÜYÜME ORANLARI AKTİFLER BÜYÜME ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab52)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def boabo_1():
    ap=tk.Tk()
    ap.geometry("750x80")
    ap.title("Toplam Aktifler Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Toplam Aktifler Büyüme Oranı=((Aktif Toplamı(güncel)/Aktif Toplamı(önceki dönem))-1)
    Not:Bilanço ve/veya gelir tablosunda (-) olarak görülen gider ve borç kalemleri formüllerde mutlak değerleri alınarak kullanılmalıdır.
    """).place(x=0,y=15)
#Açıklama
def boabo_2():
    ap=tk.Tk()
    ap.geometry("800x180")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Dönemler itibarıyla toplam aktiflerdeki değişiklikleri ölçmede kullanılan toplam aktifler büyüme oranı, bize şirketlerin toplam aktiflerindeki
    artış hızının diğer şirketlerle kıyas yapılmasına olanak verdiği gibi, şirketlerin gelecekteki varlıklarındaki büyüklükleri hakkında tahmin
    yapılabilmesine olanak sağlar. Dönemler itibariyle bulunacak artış (büyüme) hızları yardımıyla, gelecekte şirketlerin ulaşabileceği varlık
    (aktif) büyüklükleri istatistiksel yöntemlerle tahmin edilebilir. Böylece, şirketlerin aktif karlılıkları hakkında da öngörülerde bulunulursa,
    gelecek dönemlerde şirketlerin elde edebileceği net dönem karları tahmin edilebilir. Diğer şirketlere kıyasla düşük bir aktif büyüme oranına
    sahip bir şirket, satışlardaki büyüme oranı ile birlikte değerlendirilerek yeterince verimli bir şekilde yönetilemiyor ve gerekli büyümeyi
    gerçekleştiremiyor yorumu yapılabilir. Fakat şirketlerin diğer verilerinde olumsuz gelişmelerin görülmemesi durumunda, bu durum şirketlerin daha
    optimal yönetilmeye başlandığının bir göstergesi de olabilir.
    """).place(x=0,y=15)
def boabo_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
boabo1=tk.Button(tab52,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=boabo_1).place(x=10,y=25)
boabo2=tk.Button(tab52,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=boabo_2).place(x=250,y=25)
boabo3=tk.Button(tab52,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=boabo_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
boabo_label1=ttk.Label(tab52,text="Şu anki Toplam Aktifler :",style="BW.TLabel").place(x=10,y=70)
boabo_label2=ttk.Label(tab52,text="Bir Önceki Dönem Toplam Aktifler :",style="BW.TLabel").place(x=10,y=105)
boabo_label3=ttk.Label(tab52,text="Toplam Aktifler Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
boabo_entry1=tk.Entry(tab52,width=15,background=background102)
boabo_entry2=tk.Entry(tab52,width=15,background=background102)
#input box'ları yerleştiriyoruz
boabo_entry1.place(x=250,y=70)
boabo_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
boabo_label_sonuc=ttk.Label(tab52,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
boabo_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(45) BÜYÜME ORANLARI ÖZSERMAYE BÜYÜME ORANI İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab53)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def booboz_1():
    ap=tk.Tk()
    ap.geometry("500x80")
    ap.title("Özsermaye Büyüme Oranı")
    label1=tk.Label(ap,text="""
    Özsermaye Büyüme Oranı=((Özsermaye(güncel)/Özsermaye(bir önceki dönem))-1)
    """).place(x=0,y=15)
#Açıklama
def booboz_2():
    ap=tk.Tk()
    ap.geometry("830x210")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Dönemler itibarıyla Özsermayedeki değişiklikleri ölçmede kullanılan özsermaye büyüme oranı, bize şirketlerin Öz Sermayedeki artış hızının diğer
    şirketlerle kıyas yapılmasına olanak verdiği gibi, ortakların şirketlerdeki paylarının gelecekteki gelişimi hakkında tahmin yapabilmemize olanak
    tanır. Toplam aktifler büyüme oranındaki gelişmenin Öz Sermayenin büyüme oranından daha küçük olması durumunda şirketlerin Öz Sermaye yoluyla
    finansmanına (oto-finansmana) daha fazla ağırlık vermeye başladıkları şeklinde bir tespit yapılabilir. Dikkat edilmesi gereken bir nokta da
    oto-finansmanın, karın dağıtılmayıp yedek akçe olarak ayrılması ve sonra sermayeye eklenmesi ile de yapılabileceğidir. Bunun için bu oranın net
    kâr büyüme hızı ve temettü verimi oranı ile birlikte değerlendirilmesi uygun olacaktır. Dönemler itibariyle bulunacak artış (büyüme) hızları
    yardımıyla, gelecekte Öz Sermayenin ulaşabileceği büyüklük tahmin edilebilir. Böylece, şirketlerin Özsermaye karlılıkları ve net dönem karları
    tahmin edilebilir. Diğer şirketlere kıyasla düşük bir büyüme oranına sahip şirketlerin Özsermaye büyüme oranındaki artış hızının toplam aktifler
    büyüme hızının altında kalması durumunda, şirketlerin daha çok yabancı kaynaklara yöneldikleri şeklinde yorum yapılabilir. Fakat şirketlerin
    finansman politikalarında bu şekilde bir eğilim yetersiz olan net dönem karı ile sonuçlanıyorsa, bu durumdaki şirketlerin daha ayrıntılı bir
    şekilde incelenmesi uygun olacaktır.
    """).place(x=0,y=15)
def booboz_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
booboz1=tk.Button(tab53,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=booboz_1).place(x=10,y=25)
booboz2=tk.Button(tab53,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=booboz_2).place(x=250,y=25)
booboz3=tk.Button(tab53,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=booboz_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
booboz_label1=ttk.Label(tab53,text="Şu anki Özsermaye :",style="BW.TLabel").place(x=10,y=70)
booboz_label2=ttk.Label(tab53,text="Bir Önceki Dönem Özsermaye :",style="BW.TLabel").place(x=10,y=105)
booboz_label3=ttk.Label(tab53,text="Özsermaye Büyüme Oranı :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
booboz_entry1=tk.Entry(tab53,width=15,background=background102)
booboz_entry2=tk.Entry(tab53,width=15,background=background102)
#input box'ları yerleştiriyoruz
booboz_entry1.place(x=250,y=70)
booboz_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
booboz_label_sonuc=ttk.Label(tab53,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
booboz_label_sonuc.place(x=250,y=140)


######################################################################################################################################################
"""(46) YARDIMCI DEĞERLER NET İŞLETME SERMAYESİ İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab54)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def yanis_1():
    ap=tk.Tk()
    ap.geometry("400x80")
    ap.title("Net İşletme Sermayesi")
    label1=tk.Label(ap,text="""
    Net İşletme Sermayesi = Dönen Varlıklar - Kısa Vadeli Borçlar
    """).place(x=0,y=15)
#Açıklama
def yanis_2():
    ap=tk.Tk()
    ap.geometry("810x100")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Değer Şirketlerin faaliyetlerini devam ettirebilmeleri için gerekli olan brüt işletme sermayesinin (dönen varlıklar ve kısa süreli
    yükümlülüklerini karşılamakta kullanabilecek iktisadi değerler) kısa vadeli borçlarını aşan kısmına net işletme sermayesi denir.
    Net işletme sermayesi tutarının büyüklüğü, şirketlerin faaliyetleri süresince tam kapasitede karlı ve verimli şekilde çalışabilmesi,
    üretimini devam ettirebilmesi, iş hacmini arttırabilmesi, yükümlülüklerini karşılayamama riskinin azalması açısından önem taşır.
    Dönemler itibarıyla net işletme sermayesindeki değişimler, şirketlerin faaliyetleri sonucu nakit yaratma potansiyelini gözlemleme olanağı sağlar. 
    """).place(x=0,y=15)
def yanis_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
yanis1=tk.Button(tab54,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=yanis_1).place(x=10,y=25)
yanis2=tk.Button(tab54,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=yanis_2).place(x=250,y=25)
yanis3=tk.Button(tab54,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=yanis_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
yanis_label1=ttk.Label(tab54,text="Dönen Varlıklar :",style="BW.TLabel").place(x=10,y=70)
yanis_label2=ttk.Label(tab54,text="Kısa Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=105)
yanis_label3=ttk.Label(tab54,text="Net İşletme Sermayesi :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
yanis_entry1=tk.Entry(tab54,width=15,background=background102)
yanis_entry2=tk.Entry(tab54,width=15,background=background102)
#input box'ları yerleştiriyoruz
yanis_entry1.place(x=250,y=70)
yanis_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
yanis_label_sonuc=ttk.Label(tab54,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
yanis_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(47) YARDIMCI DEĞERLER LİKİT AKTİFLER İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab55)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def yala_1():
    ap=tk.Tk()
    ap.geometry("600x80")
    ap.title("Likit Aktifler")
    label1=tk.Label(ap,text="""
    Likit Aktifler = Hazır Değerler + Menkul Değerler + Kısa Vadeli Ticari Alacaklar + Diğer Kısa Vadeli Alacaklar
    """).place(x=0,y=15)
#Açıklama
def yala_2():
    ap=tk.Tk()
    ap.geometry("780x110")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Değer Şirketlerin ihtiyaç anında en hızlı ve kolay yoldan, ederinden fazla değer kaybına uğramadan nakite dönüştürebilecekleri aktiflerine
    likit (hızlı) aktifler denir. Likit aktifler tutarının büyüklüğü, faaliyetlerini icra ettikleri sürede şirketlerin borçlarını ve ihtiyaçlarını
    kolay karşılayabilmesi açısından önem taşır. Şirketlerin olağandışı durumlarla karşılaştığında, gösterecekleri tepkinin derecesini gösterir.
    Dönemler itibariyle likit aktiflerdeki değişimler, şirketlerin faaliyetleri sonucu nakit yaratma potansiyelini gözlemleme olanağı sağlar. 
    """).place(x=0,y=15)
def yala_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
yala1=tk.Button(tab55,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=yala_1).place(x=10,y=25)
yala2=tk.Button(tab55,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=yala_2).place(x=250,y=25)
yala3=tk.Button(tab55,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=yala_3).place(x=250,y=245)
#kullanıcıdan input için label ekleniyor
yala_label1=ttk.Label(tab55,text="Hazır Değerler :",style="BW.TLabel").place(x=10,y=70)
yala_label2=ttk.Label(tab55,text="Menkul Kıymetler :",style="BW.TLabel").place(x=10,y=105)
yala_label3=ttk.Label(tab55,text="Kısa Vadeli Ticari Alacaklar :",style="BW.TLabel").place(x=10,y=140)
yala_label4=ttk.Label(tab55,text="Diğer Kısa Vadeli Alacaklar :",style="BW.TLabel").place(x=10,y=175)
yala_label5=ttk.Label(tab55,text="Likit Aktifler :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=210)
#input alanı oluşturuyoruz
yala_entry1=tk.Entry(tab55,width=15,background=background102)
yala_entry2=tk.Entry(tab55,width=15,background=background102)
yala_entry3=tk.Entry(tab55,width=15,background=background102)
yala_entry4=tk.Entry(tab55,width=15,background=background102)
#input box'ları yerleştiriyoruz
yala_entry1.place(x=250,y=70)
yala_entry2.place(x=250,y=105)
yala_entry3.place(x=250,y=140)
yala_entry4.place(x=250,y=175)
#Sonucu yazdıracağımız label'i oluşturuyoruz
yala_label_sonuc=ttk.Label(tab55,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
yala_label_sonuc.place(x=250,y=210)


######################################################################################################################################################
"""(48) YARDIMCI DEĞERLER DEVAMLI SERMAYE İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab56)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def yads_1():
    ap=tk.Tk()
    ap.geometry("460x90")
    ap.title("Deevamlı Sermaye")
    label1=tk.Label(ap,text="""
    Devamlı Sermaye = Uzun Vadeli Borçlar + Özsermaye
    Not : Bilanço ve/veya gelir tablosunda (-) olarak görülen gider ve borç kalemleri
    formüllerde mutlak değerleri alınarak kullanılmalıdır. 
    """).place(x=0,y=15)
#Açıklama
def yads_2():
    ap=tk.Tk()
    ap.geometry("770x110")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Değer Şirketlerin uzun vadeli kaynaklarının toplamını göstermekte olan devamlı sermaye, şirketlerin varlıklarını fonlamada kullandığı
    kaynakların niteliklerini ve bu varlıkları fonlama gücünü (riskini) göstermektedir. Devamlı sermayenin yüksek oluşu ve zamanla artması
    şirketlerin kısa vadede bir kaynak bulma zorluğu içerisine girmeyeceğini düşündürmekle birlikte ülkemizdeki uzun süreli fon teminindeki
    zorluklar, devamlı sermayenin şirketlerin pasiflerinde yeterince yer tutmamasına neden olmaktadır.
    """).place(x=0,y=15)
def yads_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
yads1=tk.Button(tab56,text="Formülü görmek için tıklayınız",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=yads_1).place(x=10,y=25)
yads2=tk.Button(tab56,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=5,command=yads_2).place(x=250,y=25)
yads3=tk.Button(tab56,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=2,width=5,command=yads_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
yads_label1=ttk.Label(tab56,text="Uzun Vadeli Borçlar :",style="BW.TLabel").place(x=10,y=70)
yads_label2=ttk.Label(tab56,text="Özsermaye :",style="BW.TLabel").place(x=10,y=105)
yads_label3=ttk.Label(tab56,text="Devamlı Sermaye :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
yads_entry1=tk.Entry(tab56,width=15,background=background102)
yads_entry2=tk.Entry(tab56,width=15,background=background102)
#input box'ları yerleştiriyoruz
yads_entry1.place(x=250,y=70)
yads_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
yads_label_sonuc=ttk.Label(tab56,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
yads_label_sonuc.place(x=250,y=140)

######################################################################################################################################################
"""(49) YARDIMCI DEĞERLER FAİZ VE VERGİ ÖNCESİ KÂR İÇİNDEKİ OBJELER OLUŞTURULUYOR(tab57)"""
######################################################################################################################################################
#Formülü görmek için tıklayınız
def yafvok_1():
    ap=tk.Tk()
    ap.geometry("460x90")
    ap.title("Deevamlı Sermaye")
    label1=tk.Label(ap,text="""
     Faiz ve Vergi Öncesi Kar = Dönem Kârı + Finansman Giderleri 
     Not : Bilanço ve/veya gelir tablosunda (-) olarak görülen gider ve borç kalemleri
     formüllerde mutlak değerleri alınarak kullanılmalıdır.
    """).place(x=0,y=15)
#Açıklama
def yafvok_2():
    ap=tk.Tk()
    ap.geometry("770x110")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
    Değer Şirketlerin karlarından finansman giderleri ve vergiler indirilmeden bulunan tutar; "Faiz ve Vergi Öncesi Kar" olarak adlandırılmaktadır.
     Şirketlerin faiz ve vergi yükümlülükleri öncesi kar tutarları, şirketlerin toplam faaliyetlerinden ne kadar kar ettiğini görmemizi sağlar. 
    """).place(x=0,y=15)
def yafvok_3():
    ap=tk.Tk()
    ap.geometry("520x120")
    ap.title("Açıklama")
    label1=tk.Label(ap,text="""
                    Program dili gereği türkçe karakter değil ingilizce karakter kullanıldığından
                    türkçede ondalıklı sayılar 'virgül' ile ifade edilirken, ingilizce karakterde 'nokta'
                    olarak ifade edilir. Yani program çıktısında görebileceğiniz 13.3464 gibi bir sayı
                    aslında ondalıklı sayıdır.
                                            """).place(x=0,y=15)

#Pencere açma butonları ekleniyor    
yafvok1=tk.Button(tab57,text="Formülü görmek için tıklayınız",bg="aquamarine4",fg="white",height=1,width=30,command=yafvok_1).place(x=10,y=25)
yafvok2=tk.Button(tab57,text="?",bg="MediumPurple1",fg="white",height=1,width=5,command=yafvok_2).place(x=250,y=25)
yafvok3=tk.Button(tab57,text="?",bg="SkyBlue2",fg="white",height=2,width=5,command=yafvok_3).place(x=250,y=175)
#kullanıcıdan input için label ekleniyor
yafvok_label1=ttk.Label(tab57,text="Dönem Kârı :",style="BW.TLabel").place(x=10,y=70)
yafvok_label2=ttk.Label(tab57,text="Finansman Giderleri :",style="BW.TLabel").place(x=10,y=105)
yafvok_label3=ttk.Label(tab57,text="Faiz ve Vergi Öncesi Kâr :",foreground=foreground101,background=backround100,font=("Arial",12,"bold")).place(x=10,y=140)
#input alanı oluşturuyoruz
yafvok_entry1=tk.Entry(tab57,width=15,background=background102)
yafvok_entry2=tk.Entry(tab57,width=15,background=background102)
#input box'ları yerleştiriyoruz
yafvok_entry1.place(x=250,y=70)
yafvok_entry2.place(x=250,y=105)
#Sonucu yazdıracağımız label'i oluşturuyoruz
yafvok_label_sonuc=ttk.Label(tab57,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
yafvok_label_sonuc.place(x=250,y=140)




######################################################################################################################################################
"""FONKSİYONLAR OLUŞTURULUYOR""" #fonksiyonların sayı numarası proje.py 'de ki fonksiyonların işlem numarası
######################################################################################################################################################

def hesapla3():
    #Değerler çekiliyor
    nominal_faiz=bbf_entry1.get()
    enflasyon_orani=bbf_entry2.get()
    anapara=bbf_entry3.get()
    sure=bbf_entry4.get()
    stopaj_orani=bbf_entry5.get()
    #Sayıya dönüştürülüyor
    nf=float(nominal_faiz)
    eo=float(enflasyon_orani)
    ap=float(anapara)
    s=int(sure)
    so=float(stopaj_orani)
    #Hesaplanıyor...
    reel_faiz=(nf-eo)/1200
    basit_faiz_getirisi=ap*reel_faiz*s
    stopaj_kesintisi=basit_faiz_getirisi*(so/100) #sk
    yeni_anapara=ap+(basit_faiz_getirisi-stopaj_kesintisi) ##yap
    gercek_getiri=basit_faiz_getirisi-stopaj_kesintisi ##gg
    #Sayılar düzenleniyor...
    sk=round(stopaj_kesintisi,2)
    yap=round(yeni_anapara,2)
    gg=round(gercek_getiri,2) 
    #Yazdırılıyor...
    bbf_label_sure.configure(text=s)
    bbf_label_getiri.configure(text=gg)
    bbf_label_stopaj.configure(text=sk)
    bbf_label_yenianapara.configure(text=yap)
def hesapla4():
    #Değerler çekiliyor
    nominal_faiz=bif_entry1.get()
    enflasyon_orani=bif_entry2.get()
    anapara=bif_entry3.get()
    sure=bif_entry4.get()
    stopaj_orani=bif_entry5.get()
    #Sayıya dönüştürülüyor
    nf=float(nominal_faiz)
    eo=float(enflasyon_orani)
    ap=float(anapara)
    s=int(sure)
    so=float(stopaj_orani)
    #Hesaplanıyor...
    reel_faiz=(nf-eo)/1200 ##rf
    bilesik_faiz_getirisi=(ap)*((1+reel_faiz)**s) ##bfg
    stopaj_kesintisi=bilesik_faiz_getirisi*(so/100) ##sk
    yeni_anapara=ap+(bilesik_faiz_getirisi-stopaj_kesintisi) ##yap
    gercek_getiri=bilesik_faiz_getirisi-stopaj_kesintisi ##gg
    #Sayılar düzenleniyor...
    rf=round(reel_faiz,2)
    bfg=round(bilesik_faiz_getirisi,2)
    sk=round(stopaj_kesintisi,2)
    yap=round(yeni_anapara,2)
    gg=round(gercek_getiri,2)
    #Yazdırılıyor...
    bif_label_sure.configure(text=s)
    bif_label_getiri.configure(text=gg)
    bif_label_stopaj.configure(text=sk)
    bif_label_yenianapara.configure(text=yap)
def hesapla2_1():
    #Değerler çekiliyor
    nominal_faiz=fdrfh_entry1.get()
    beklenen_enflasyon_orani=fdrfh_entry2.get()
    #Sayıya dönüştürülüyor
    nf=float(nominal_faiz)
    beo=float(beklenen_enflasyon_orani)
    #Hesaplanıyor...
    reel_faiz=nf-beo
    #Sayılar düzenleniyor...
    rf=round(reel_faiz,2)
    #Yazdırılıyor...
    fdrfh_label_sonuc.configure(text=rf)
def hesapla2_2():
    #Değerler çekiliyor
    nominal_faiz=fdrfh_entry3.get()
    beklenen_enflasyon_orani=fdrfh_entry4.get()
    #Sayıya dönüştürülüyor
    nf=float(nominal_faiz)
    beo=float(beklenen_enflasyon_orani)
    #Hesaplanıyor...
    reel_faiz=((1+nf)/(1+beo))-1 
    #Sayılar düzenleniyor...
    rf=round(reel_faiz,2)
    #Yazdırılıyor...
    fdrfh_label_sonuc2.configure(text=rf)
def hesapla1():
    #Değerler çekiliyor
    dbhsf=hsgh_entry1.get()
    dshsf=hsgh_entry2.get()
    t=hsgh_entry3.get()
    #Sayıya dönüştürülüyor
    float_dbhsf=float(dbhsf)
    float_dshsf=float(dshsf)
    float_t=float(t)
    #Hata mesajı
    if (float_dbhsf==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    r=((float_dshsf-float_dbhsf)+float_t)/float_dbhsf
    #Sayılar düzenleniyor...
    r_round=round(r,2)
    #Yazdırılıyor...
    hsgh_label_sonuc.configure(text=r_round)
        
def hesapla5():
    #Değerler çekiliyor
    bugun_fiyat=hsdm_entry1.get()
    temettu=hsdm_entry2.get()
    getiri_oran=hsdm_entry3.get()
    son_fiyat=hsdm_entry4.get()
    #Sayıya dönüştürülüyor
    float_bugun_fiyat=float(bugun_fiyat)
    float_temettu=float(temettu)
    float_getiri_oran=float(getiri_oran)
    float_son_fiyat=float(son_fiyat)
     #Hata mesajı
    if (1+float_getiri_oran==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    p=(float_temettu+float_son_fiyat)/(1+float_getiri_oran)
    #Sayılar düzenleniyor...
    p_round=round(p,2)
    #Yazdırılıyor...
    hsdm_label_sonuc.configure(text=p_round)
def hesapla6():
    #Değerler çekiliyor
    ozsermaye=pgdd_entry1.get()
    odenmis_sermaye=pgdd_entry2.get()
    #Sayıya dönüştürülüyor
    float_ozsermaye=float(ozsermaye)
    float_odenmis_sermaye=float(odenmis_sermaye)
    #Hata mesajı
    if (float_odenmis_sermaye==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    dd=float_ozsermaye/float_odenmis_sermaye
    #Sayılar düzenleniyor...
    dd_round=round(dd,2)
    #Yazdırılıyor...
    pgdd_label_sonuc.configure(text=dd_round)
def hesapla7():
    #Değerler çekiliyor
    bf=pgfko_entry1.get()
    hbk=pgfko_entry2.get()
    #Sayıya dönüştürülüyor
    float_bf=float(bf)
    float_hbk=float(hbk)
    #Hata mesajı
    if (float_hbk==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    fko=float_bf/float_hbk
    #Sayılar düzenleniyor...
    fko_round=round(fko,2)
    #Yazdırılıyor...
    pgfko_label_sonuc.configure(text=fko_round)
def hesapla8():
    #Değerler çekiliyor
    bf=pgpddd_entry1.get()
    odenmis=pgpddd_entry2.get()
    ozsermaye=pgpddd_entry3.get()
    #Sayıya dönüştürülüyor
    float_bf=float(bf)
    float_odenmis=float(odenmis)
    float_ozsermaye=float(ozsermaye)
    #Hata mesajı
    if (float_odenmis==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    pddd=(float_bf)/(float_ozsermaye/float_odenmis)
    #Sayılar düzenleniyor...
    pddd_round=round(pddd,2)
    #Yazdırılıyor...
    pgpddd_label_sonuc.configure(text=pddd_round)

def hesapla9():
    #Değerler çekiliyor
    tot=pgtm_entry1.get()
    pd=pgtm_entry2.get()
    #Sayıya dönüştürülüyor
    float_tot=float(tot)
    float_pd=float(pd)
    #Hata mesajı
    if (float_pd==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    tv=float_tot/float_pd
    #Sayılar düzenleniyor...
    tv_round=round(tv,2)
    #Yazdırılıyor...
    pgtm_label_sonuc.configure(text=tv_round)

def hesapla10():
    #Değerler çekiliyor
    dv=loco_entry1.get()
    kvb=loco_entry2.get()
    #Sayıya dönüştürülüyor
    float_dv=float(dv)
    float_kvb=float(kvb)
    #Hata mesajı
    if (float_kvb==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    co=float_dv/float_kvb
    #Sayılar düzenleniyor...
    co_round=round(co,2)
    #Yazdırılıyor...
    loco_label_sonuc.configure(text=co_round)

def hesapla11():
    #Değerler çekiliyor
    dv=loato_entry1.get()
    kvb=loato_entry2.get()
    s=loato_entry3.get()
    #Sayıya dönüştürülüyor
    float_dv=float(dv)
    float_kvb=float(kvb)
    float_s=float(s)
    #Hata mesajı
    if (float_kvb==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    ato=(float_dv-float_s)/float_kvb
    #Sayılar düzenleniyor...
    ato_round=round(ato,2)
    #Yazdırılıyor...
    loato_label_sonuc.configure(text=ato_round)
def hesapla12():
    #Değerler çekiliyor
    hd=lono_entry1.get()
    mk=lono_entry2.get()
    kvb=lono_entry3.get()
    #Sayıya dönüştürülüyor
    float_hd=float(hd)
    float_mk=float(mk)
    float_kvb=float(kvb)
    #Hata mesajı
    if (float_kvb==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    no=(float_hd+float_mk)/float_kvb
    #Sayılar düzenleniyor...
    no_round=round(no,2)
    #Yazdırılıyor...
    lono_label_sonuc.configure(text=no_round)

def hesapla13():
    #Değerler çekiliyor
    kvb=losbo_entry1.get()
    hd=losbo_entry2.get()
    mk=losbo_entry3.get()
    s=losbo_entry4.get()
    #Sayıya dönüştürülüyor
    float_kvb=float(kvb)
    float_hd=float(hd)
    float_mk=float(mk)
    float_s=float(s)
    #Hata mesajı
    if (float_s==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    sbo=(float_kvb-(float_hd+float_mk))/float_s
    #Sayılar düzenleniyor...
    sbo_round=round(sbo,2)
    #Yazdırılıyor...
    losbo_label_sonuc.configure(text=sbo_round)

def hesapla14():
    #Değerler çekiliyor
    dv=lonista_entry1.get()
    kvb=lonista_entry2.get()
    ta=lonista_entry3.get()
    #Sayıya dönüştürülüyor
    float_dv=float(dv)
    float_kvb=float(kvb)
    float_ta=float(ta)
    #Hata mesajı
    if (float_ta==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    nista=(float_dv-float_kvb)/float_ta
    #Sayılar düzenleniyor...
    nista_round=round(nista,2)
    #Yazdırılıyor...
    lonista_label_sonuc.configure(text=nista_round)

def hesapla15():
    #Değerler çekiliyor
    la=lolao_entry1.get()
    ta=lolao_entry2.get()
    #Sayıya dönüştürülüyor
    float_la=float(la)
    float_ta=float(ta)
    #Hata mesajı
    if (float_ta==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    lao=float_la/float_ta
    #Sayılar düzenleniyor...
    lao_round=round(lao,2)
    #Yazdırılıyor...
    lolao_label_sonuc.configure(text=lao_round)

def hesapla16():
    #Değerler çekiliyor
    tb=boko_entry1.get()
    ta=boko_entry2.get()
    #Sayıya dönüştürülüyor
    float_tb=float(tb)
    float_ta=float(ta)
    #Hata mesajı
    if (float_ta==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    ko=float_tb/float_ta
    #Sayılar düzenleniyor...
    ko_round=round(ko,2)
    #Yazdırılıyor...
    boko_label_sonuc.configure(text=ko_round)

def hesapla17():
    #Değerler çekiliyor
    os=bofo_entry1.get()
    tb=bofo_entry2.get()
    #Sayıya dönüştürülüyor
    float_os=float(os)
    float_tb=float(tb)
    #Hata mesajı
    if (float_tb==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    fo=float_os/float_tb
    #Sayılar düzenleniyor...
    fo_round=round(fo,2)
    #Yazdırılıyor...
    bofo_label_sonuc.configure(text=fo_round)

def hesapla18():
    #Değerler çekiliyor
    tb=botboo_entry1.get()
    o=botboo_entry2.get()
    #Sayıya dönüştürülüyor
    float_tb=float(tb)
    float_o=float(o)
    #Hata mesajı
    if (float_o==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    tbo=float_tb/float_o
    #Sayılar düzenleniyor...
    tbo_round=round(tbo,2)
    #Yazdırılıyor...
    botboo_label_sonuc.configure(text=tbo_round)

def hesapla19():
    #Değerler çekiliyor
    ky=booo_entry1.get()
    gyz=booo_entry2.get()
    o=booo_entry3.get()
    #Sayıya dönüştürülüyor
    float_ky=float(ky)
    float_gyz=float(gyz)
    float_o=float(o)
    #Hata mesajı
    if (float_o==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oo=(float_ky-float_gyz)/float_o
    #Sayılar düzenleniyor...
    oo_round=round(oo,2)
    #Yazdırılıyor...
    booo_label_sonuc.configure(text=oo_round)

def hesapla20():
    #Değerler çekiliyor
    mdv=bomdvo_entry1.get()
    o=bomdvo_entry2.get()
    #Sayıya dönüştürülüyor
    float_mdv=float(mdv)
    float_o=float(o)
    #Hata mesajı
    if (float_o==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=float_mdv/float_o
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    bomdvo_label_sonuc.configure(text=oran_round)

def hesapla21():
    #Değerler çekiliyor
    dv=bodvdso_entry1.get()
    uvb=bodvdso_entry2.get()
    o=bodvdso_entry2.get()
    #Sayıya dönüştürülüyor
    float_dv=float(dv)
    float_uvb=float(uvb)
    float_o=float(o)
    #Hata mesajı
    if (float_uvb+float_o==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=float_dv/(float_uvb+float_o)
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    bodvdso_label_sonuc.configure(text=oran_round)

def hesapla22():
    #Değerler çekiliyor
    kns=foadh_entry1.get()
    ta=foadh_entry2.get()
    #Sayıya dönüştürülüyor
    float_kns=float(kns)
    float_ta=float(ta)
    #Hata mesajı
    if (float_ta==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    adh=float_kns/float_ta
    #Sayılar düzenleniyor...
    adh_round=round(adh,2)
    #Yazdırılıyor...
    foadh_label_sonuc.configure(text=adh_round)

def hesapla23():
    #Değerler çekiliyor
    adh=foots_entry1.get()
    #Sayıya dönüştürülüyor
    float_adh=float(adh)
    #Hata mesajı
    if (float_adh==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    ots=float_adh/360
    #Sayılar düzenleniyor...
    ots_round=round(ots,2)
    #Yazdırılıyor...
    foots_label_sonuc.configure(text=ots_round)

def hesapla24():
    #Değerler çekiliyor
    ns=fomdvh_entry1.get()
    mdv=fomdvh_entry2.get()
    ba=fomdvh_entry3.get()
    #Sayıya dönüştürülüyor
    float_ns=float(ns)
    float_mdv=float(mdv)
    float_ba=float(ba)
    
    #Hesaplanıyor...
    nmdv=float_mdv-float_ba
    float_nmdv=float(nmdv)
    #Hata mesajı
    if (float_nmdv==0):
        hata()
    else:
        pass
    mdvdh=float_ns/float_nmdv
    #Sayılar düzenleniyor...
    mdvdh_round=round(mdvdh,2)
    #Yazdırılıyor...
    fomdvh_label_sonuc.configure(text=mdvdh_round)

def hesapla25():
    #Değerler çekiliyor
    sm=fosdh_entry1.get()
    dbs=fosdh_entry2.get()
    dss=fosdh_entry3.get()
    #Sayıya dönüştürülüyor
    float_sm=float(sm)
    float_dbs=float(dbs)
    float_dss=float(dss)
    #Hata mesajı
    if (float_dbs+float_dss==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    os=(float_dbs+float_dss)/2
    sdh=float_sm/os
    #Sayılar düzenleniyor...
    sdh_round=round(sdh,2)
    #Yazdırılıyor...
    fosdh_label_sonuc.configure(text=sdh_round)

def hesapla26():
    #Değerler çekiliyor
    sdh=fosdeh_entry1.get()
    #Sayıya dönüştürülüyor
    float_sdh=float(sdh)
    #Hata mesajı
    if (float_sdh==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    sds=360/float_sdh
    #Sayılar düzenleniyor...
    sds_round=round(sds,2)
    #Yazdırılıyor...
    fosdeh_label_sonuc.configure(text=sds_round)

def hesapla27():
    #Değerler çekiliyor
    ns=foaktifdh_entry1.get()
    at=foaktifdh_entry2.get()
    #Sayıya dönüştürülüyor
    float_ns=float(ns)
    float_at=float(at)
    #Hata mesajı
    if (float_at==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    adh=float_ns/float_at
    #Sayılar düzenleniyor...
    adh_round=round(adh,2)
    #Yazdırılıyor...
    foaktifdh_label_sonuc.configure(text=adh_round)

def hesapla28():
    #Değerler çekiliyor
    sm=fotbdh_entry1.get()
    dbtb=fotbdh_entry2.get()
    dstb=fotbdh_entry3.get()
    #Sayıya dönüştürülüyor
    float_sm=float(sm)
    float_dbtb=float(dbtb)
    float_dstb=float(dstb)
    if (float_dbtb+float_dstb==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    otb=(float_dbtb+float_dstb)/2
    tbdh=float_sm/otb
    #Sayılar düzenleniyor...
    tbdh_round=round(tbdh,2)
    #Yazdırılıyor...
    fotbdh_label_sonuc.configure(text=tbdh_round)

def hesapla29():
    #Değerler çekiliyor
    nk=kook_entry1.get()
    dbos=kook_entry2.get()
    dsos=kook_entry3.get()
    #Sayıya dönüştürülüyor
    float_nk=float(nk)
    float_dbos=float(dbos)
    float_dsos=float(dsos)
    #Hata mesajı
    if (float_dbos+float_dsos==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    os=(float_dbos+float_dsos)/2
    k=float_nk/os
    #Sayılar düzenleniyor...
    k_round=round(k,2)
    #Yazdırılıyor...
    kook_label_sonuc.configure(text=k_round)

def hesapla30():
    #Değerler çekiliyor
    fvok=koek_entry1.get()
    pt=koek_entry2.get()
    #Sayıya dönüştürülüyor
    float_fvok=float(fvok)
    float_pt=float(pt)
    #Hata mesajı
    if (float_pt==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    ek=float_fvok/float_pt
    #Sayılar düzenleniyor...
    ek_round=round(ek,2)
    #Yazdırılıyor...
    koek_label_sonuc.configure(text=ek_round)

def hesapla31():
    #Değerler çekiliyor
    bsk=kobk_entry1.get()
    ns=kobk_entry2.get()
    #Sayıya dönüştürülüyor
    float_bsk=float(bsk)
    float_ns=float(ns)
    #Hata mesajı
    if (float_ns==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    bk=float_bsk/float_ns
    #Sayılar düzenleniyor...
    bk_round=round(bk,2)
    #Yazdırılıyor...
    kobk_label_sonuc.configure(text=bk_round)

def hesapla32():
    #Değerler çekiliyor
    ndk=konk_entry1.get()
    ns=konk_entry2.get()
    #Sayıya dönüştürülüyor
    float_ndk=float(ndk)
    float_ns=float(ns)
    #Hata mesajı
    if (float_ns==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    nk=float_ndk/float_ns
    #Sayılar düzenleniyor...
    nk_round=round(nk,2)
    #Yazdırılıyor...
    konk_label_sonuc.configure(text=nk_round)

def hesapla33():
    #Değerler çekiliyor
    efk=koefk_entry1.get()
    ns=koefk_entry2.get()
    #Sayıya dönüştürülüyor
    float_efk=float(efk)
    float_ns=float(ns)
    #Hata mesajı
    if (float_ns==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    o=float_efk/float_ns
    #Sayılar düzenleniyor...
    o_round=round(o,2)
    #Yazdırılıyor...
    koefk_label_sonuc.configure(text=o_round)

def hesapla34():
    #Değerler çekiliyor
    fk=kofa_entry1.get()
    ns=kofa_entry2.get()
    #Sayıya dönüştürülüyor
    float_fk=float(fk)
    float_ns=float(ns)
    #Hata mesajı
    if (float_ns==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    o=float_fk/float_ns
    #Sayılar düzenleniyor...
    o_round=round(o,2)
    #Yazdırılıyor...
    kofa_label_sonuc.configure(text=o_round)

def hesapla35():
    #Değerler çekiliyor
    dk=kofm_entry1.get()
    ns=kofm_entry2.get()
    fg=kofm_entry3.get()
    #Sayıya dönüştürülüyor
    float_dk=float(dk)
    float_ns=float(ns)
    float_fg=float(fg)
    #Hata mesajı
    if (float_ns==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    fvok=(float_dk+float_fg)/float_ns
    o=fvok/float_ns
    #Sayılar düzenleniyor...
    o_round=round(o,2)
    #Yazdırılıyor...
    kofm_label_sonuc.configure(text=o_round)

def hesapla36():
    #Değerler çekiliyor
    v=kovnso_entry1.get()
    ns=kovnso_entry2.get()
    #Sayıya dönüştürülüyor
    float_v=float(v)
    float_ns=float(ns)
    #Hata mesajı
    if (float_ns==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    o=float_v/float_ns
    #Sayılar düzenleniyor...
    o_round=round(o,2)
    #Yazdırılıyor...
    kovnso_label_sonuc.configure(text=o_round)

def hesapla37():
    #Değerler çekiliyor
    n=kodsk_entry1.get()
    o=kodsk_entry2.get()
    #Sayıya dönüştürülüyor
    float_n=float(n)
    float_o=float(o)
    #Hata mesajı
    if (float_o==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    dsk=float_n/float_o
    #Sayılar düzenleniyor...
    dsk_round=round(dsk,2)
    #Yazdırılıyor...
    kodsk_label_sonuc.configure(text=dsk_round)

def hesapla38():
    #Değerler çekiliyor
    n=koak_entry1.get()
    o=koak_entry2.get()
    #Sayıya dönüştürülüyor
    float_n=float(n)
    float_o=float(o)
    #Hata mesajı
    if (float_o==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    ak=float_n/float_o
    #Sayılar düzenleniyor...
    ak_round=round(ak,2)
    #Yazdırılıyor...
    koak_label_sonuc.configure(text=ak_round)

def hesapla39():
    #Değerler çekiliyor
    f=kofgs_entry1.get()
    dbs=kofgs_entry2.get()
    dss=kofgs_entry3.get()
    #Sayıya dönüştürülüyor
    float_f=float(f)
    float_dbs=float(dbs)
    float_dss=float(dss)
    #Hata mesajı
    if (float_dbs+float_dss==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    os=(float_dbs+float_dss)/2
    oran=float_f/os
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    kofgs_label_sonuc.configure(text=oran_round)

def hesapla40_1():
    #Değerler çekiliyor
    ds=bodsbo_entry1.get()
    eds=bodsbo_entry2.get()
    #Sayıya dönüştürülüyor
    float_ds=float(ds)
    float_eds=float(eds)
    #Hata mesajı
    if (float_eds==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    hesap=(float_ds/float_eds)-1
    #Sayılar düzenleniyor...
    hesap_round=round(hesap,2)
    #Yazdırılıyor...
    bodsbo_label_sonuc.configure(text=hesap_round)

def hesapla40_2():
    #Değerler çekiliyor
    uvb=bodsbo_entry3.get()
    o=bodsbo_entry4.get()
    eo=bodsbo_entry5.get()
    #Sayıya dönüştürülüyor
    float_uvb=float(uvb)
    float_o=float(o)
    float_eo=float(eo)
    if (float_uvb+float_eo==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    hesap=((float_uvb+float_o)/(float_uvb+float_eo))-1
    #Sayılar düzenleniyor...
    hesap_round=round(hesap,2)
    #Yazdırılıyor...
    bodsbo_label_sonuc2.configure(text=hesap_round)

def hesapla41():
    #Değerler çekiliyor
    n=bonkbo_entry1.get()
    en=bonkbo_entry2.get()
    #Sayıya dönüştürülüyor
    float_n=float(n)
    float_en=float(en)
    #Hata mesajı
    if (float_en==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=float_n/float_en
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    bonkbo_label_sonuc.configure(text=oran_round)

def hesapla42():
    #Değerler çekiliyor
    ns=bonsbo_entry1.get()
    ens=bonsbo_entry2.get()
    #Sayıya dönüştürülüyor
    float_ns=float(ns)
    float_ens=float(ens)
    #Hata mesajı
    if (float_ens==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=(float_ns/float_ens)-1
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    bonsbo_label_sonuc.configure(text=oran_round)

def hesapla43_1():
    #Değerler çekiliyor
    nis=bonisbo_entry1.get()
    enis=bonisbo_entry2.get()
    #Sayıya dönüştürülüyor
    float_nis=float(nis)
    float_enis=float(enis)
    #Hata mesajı
    if (float_enis==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=(float_nis/float_enis)-1
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    bonisbo_label_sonuc.configure(text=oran_round)

def hesapla43_2():
    #Değerler çekiliyor
    dv=bonisbo_entry3.get()
    kvb=bonisbo_entry4.get()
    ekvb=bonisbo_entry5.get()
    #Sayıya dönüştürülüyor
    float_dv=float(dv)
    float_kvb=float(kvb)
    float_ekvb=float(ekvb)
    #Hata mesajı
    if (float_dv+float_ekvb==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=((float_dv-float_kvb)/(float_dv-float_ekvb))-1
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    bonisbo_label_sonuc2.configure(text=oran_round)

def hesapla44():
    #Değerler çekiliyor
    ta=boabo_entry1.get()
    eta=boabo_entry2.get()
    #Sayıya dönüştürülüyor
    float_ta=float(ta)
    float_eta=float(eta)
    #Hata mesajı
    if (float_eta==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=(float_ta/float_eta)-1
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    boabo_label_sonuc.configure(text=oran_round)

def hesapla45(): #Büyüme Oranları Özsermaye Büyüme Oranı
    #Değerler çekiliyor
    o=booboz_entry1.get()
    eo=booboz_entry2.get()
    #Sayıya dönüştürülüyor
    float_o=float(o)
    float_eo=float(eo)
    if (float_eo==0):
        hata()
    else:
        pass
    #Hesaplanıyor...
    oran=(float_o/float_eo)-1
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    booboz_label_sonuc.configure(text=oran_round)
    

def hesapla46(): #Yardımcı Değerler Net İşletme Sermayesi 
    #Değerler çekiliyor
    dv=yanis_entry1.get()
    kvb=yanis_entry2.get()
    #Sayıya dönüştürülüyor
    float_dv=float(dv)
    float_kvb=float(kvb)
    #Hesaplanıyor...
    oran=float_dv-float_kvb
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    yanis_label_sonuc.configure(text=oran_round)
    

def hesapla47():
    #Değerler çekiliyor
    h=yala_entry1.get()
    m=yala_entry2.get()
    k=yala_entry3.get()
    d=yala_entry4.get()
    #Sayıya dönüştürülüyor
    float_h=float(h)
    float_m=float(m)
    float_k=float(k)
    float_d=float(d)
    #Hesaplanıyor...
    oran=float_h+float_m+float_k+float_d
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    yala_label_sonuc.configure(text=oran_round)

def hesapla48():
    #Değerler çekiliyor
    u=yads_entry1.get()
    o=yads_entry2.get()
    #Sayıya dönüştürülüyor
    float_u=float(u)
    float_o=float(o)
    #Hesaplanıyor...
    oran=float_u+float_o
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    yads_label_sonuc.configure(text=oran_round)


def hesapla49():
    #Değerler çekiliyor
    d=yafvok_entry1.get()
    f=yafvok_entry2.get()
    #Hata mesajı
    #Sayıya dönüştürülüyor
    float_d=float(d)
    float_f=float(f)
    #Hesaplanıyor...
    oran=float_d+float_f
    #Sayılar düzenleniyor...
    oran_round=round(oran,2)
    #Yazdırılıyor...
    yafvok_label_sonuc.configure(text=oran_round)
    
    
def hata():
    errormessage=messagebox.showerror(title="Hata",message="Bir sayı 0'a bölünemez")



######################################################################################################################################################
"""FONKSİYONLAR OLUŞTURULDU"""
######################################################################################################################################################

######################################################################################################################################################
"""HESAPLAYICI BUTONLAR OLUŞTURULUYOR"""
######################################################################################################################################################

#buton(3)
bbf_hesapla=tk.Button(tab58,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla3).place(x=10,y=400)
#buton(4)
bif_hesapla=tk.Button(tab59,text="Hesapla",width=40,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla4).place(x=10,y=400)
#buton(2_1)
fdrfh_hesapla=tk.Button(fdrfh_frame1,text="Hesapla",width=40,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla2_1).place(x=10,y=175)
#buton(2_2)
fdrfh_hesapla2=tk.Button(fdrfh_frame2,text="Hesapla",width=40,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla2_2).place(x=10,y=175)
#buton(1)
hsgh_hesapla=tk.Button(tab61,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla1).place(x=10,y=225)
#buton(5)
hsdm_hesapla=tk.Button(tab62,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla5).place(x=10,y=245)
#buton(6)
pgdd_hesapla=tk.Button(tab14,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla6).place(x=10,y=175)
#buton(7)
pgfko_hesapla=tk.Button(tab15,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla7).place(x=10,y=175)
#buton(8)
pgpddd_hesapla=tk.Button(tab16,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla8).place(x=10,y=210)
#buton(9)
pgtm_hesapla=tk.Button(tab17,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla9).place(x=10,y=175)
#buton(10)
loco_hesapla=tk.Button(tab18,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla10).place(x=10,y=175)
#buton(11)
loato_hesapla=tk.Button(tab19,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla11).place(x=10,y=210)
#buton(12)
lono_hesapla=tk.Button(tab20,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla12).place(x=10,y=210)
#buton(13)
losbo_hesapla=tk.Button(tab21,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla13).place(x=10,y=245)
#buton(14)
lonista_hesapla=tk.Button(tab22,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla14).place(x=10,y=210)
#buton(15)
lolao_hesapla=tk.Button(tab23,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla15).place(x=10,y=175)
#buton(16)
boko_hesapla=tk.Button(tab24,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla16).place(x=10,y=175)
#buton(17)
bofo_hesapla=tk.Button(tab25,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla17).place(x=10,y=175)
#buton(18)
botboo_hesapla=tk.Button(tab26,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla18).place(x=10,y=175)
#buton(19)
booo_hesapla=tk.Button(tab27,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla19).place(x=10,y=210)
#buton(20)
bomdvo_hesapla=tk.Button(tab28,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla20).place(x=10,y=175)
#buton(21)
bodvdso_hesapla=tk.Button(tab29,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla21).place(x=10,y=210)
#buton(22)
foadh_hesapla=tk.Button(tab30,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla22).place(x=10,y=175)
#buton(23)
foots_hesapla=tk.Button(tab31,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla23).place(x=10,y=140)
#buton(24)
fomdvh_hesapla=tk.Button(tab32,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla24).place(x=10,y=210)
#buton(25)
fosdh_hesapla=tk.Button(tab33,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla25).place(x=10,y=210)
#buton(26)
fosdeh_hesapla=tk.Button(tab34,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla26).place(x=10,y=140)
#buton(27)
foaktifdh_hesapla=tk.Button(tab35,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla27).place(x=10,y=175)
#buton(28)
fotbdh_hesapla=tk.Button(tab36,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla28).place(x=10,y=210)
#buton(29)
kook_hesapla=tk.Button(tab37,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla29).place(x=10,y=210)
#buton(30)
koek_hesapla=tk.Button(tab38,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla30).place(x=10,y=175)
#buton(31)
kobk_hesapla=tk.Button(tab39,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla31).place(x=10,y=175)
#buton(32)
konk_hesapla=tk.Button(tab40,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla32).place(x=10,y=175)
#buton(33)
koefk_hesapla=tk.Button(tab41,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla33).place(x=10,y=175)
#buton(34)
kofa_hesapla=tk.Button(tab42,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla34).place(x=10,y=175)
#buton(35)
kofm_hesapla=tk.Button(tab43,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla35).place(x=10,y=210)
#buton(36)
kovnso_hesapla=tk.Button(tab44,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla36).place(x=10,y=175)
#buton(37)
kodsk_hesapla=tk.Button(tab45,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla37).place(x=10,y=175)
#buton(38)
koak_hesapla=tk.Button(tab46,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla38).place(x=10,y=175)
#buton(39)
kofgs_hesapla=tk.Button(tab47,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla39).place(x=10,y=210)
#buton(40_1)
bodsbo_hesapla=tk.Button(bodsbo_frame1,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla40_1).place(x=10,y=175)
#buton(40_2)
bodsbo_hesapla2=tk.Button(bodsbo_frame2,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla40_2).place(x=10,y=210)
#buton(41)
bonkbo_hesapla=tk.Button(tab49,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla41).place(x=10,y=175)
#buton(42)
bonsbo_hesapla=tk.Button(tab50,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla42).place(x=10,y=175)
#buton(43_1)
bonisbo_hesapla=tk.Button(bonisbo_frame1,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla43_1).place(x=10,y=175)
#buton(43_2)
bonisbo_hesapla=tk.Button(bonisbo_frame2,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla43_2).place(x=10,y=210)
#buton(44)
boabo_hesapla=tk.Button(tab52,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla44).place(x=10,y=175)
#buton(45)
booboz_hesapla=tk.Button(tab53,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla45).place(x=10,y=175)
#buton(46)
yanis_hesapla=tk.Button(tab54,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla46).place(x=10,y=175)
#buton(47)
yala_hesapla=tk.Button(tab55,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla47).place(x=10,y=245)
#buton(48)
yads_hesapla=tk.Button(tab56,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla48).place(x=10,y=175)
#buton(49)
yafvok_hesapla=tk.Button(tab57,text="Hesapla",width=30,height=2,background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),command=hesapla49).place(x=10,y=175)


######################################################################################################################################################
"""LABEL OLUŞTURULUYOR..."""
######################################################################################################################################################

#Developer
label1=tk.Label(anapencere,text="Developer:Burak Türker Tügen",font="Times 12",fg="black")
label1.pack(side=tk.TOP,pady=5)

#Giriş
label4=tk.Label(tab1,text="""
Temel Analiz Programı Nedir?
Bu program, şirketlerin mali durumunu,kârlılıklarını, faaliyetlerini ve şirket hakkında birçok veriyi analiz edebilmek için gerekli fonksiyonlara
sahiptir. Her fonksiyona ait özel bir açıklama ve formül butonu bulunur. Programın işlevleri kısaca şöyle sıralanabilir:
-Halka arz edilmiş bir şirketin hisse senetlerine yatırım yapmadan önce şirketi nasıl analiz edeceğiniz konusunda size gerekli analiz araçlarını sunar.
-Kamu Aydınlatma Platformunda yayınlanan şirket bilançolarını okuyabilmenize yardımcı olur.
-Hisse senedi analizi yapabilmeniz için gerekli olan araçların tümünü size ücretsiz sunar.
-Hisse senedi analizi yapabilmeniz için farklı kaynakların internet adreslerini sizlerle paylaşır.
Program Beta aşamasındadır.
""",font="Times 10",fg="black")
label4.place(x=10,y=10)

#Mail
label2=tk.Label(tab3,text="burakturkertugenn@gmail.com",font="Times 10",fg="black")
label2.place(x=10,y=10)

#Versiyon
label3=tk.Label(tab3,text="""
Temel Analiz Programı
Çıkış: 20.02.2020
Versiyon: 1.0
""",font="Times 10",fg="black")
label3.place(x=10,y=30)




anapencere.mainloop()
