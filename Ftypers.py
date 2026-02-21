import os
import random
import time
import tkinter
from datetime import date

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ftypers")
root.geometry("500x500")
root.resizable(False,False)

#metinler
try:
    os.mkdir("metinler")
except FileExistsError:
    None
try:
    os.mkdir("sonuclar")
except FileExistsError:
    None
try:
    os.mkdir("images")
except FileExistsError:
    None
try:
    with open("metinler/metin1.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin2.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin3.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin4.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin5.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin6.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin7.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin8.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin9.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None
try:
    with open("metinler/metin10.txt" ,"x", encoding="utf-8") as file:
        file.write("")
except FileExistsError:
    None

with open("metinler/metin1.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text1 = read
with open("metinler/metin2.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text2 = read
with open("metinler/metin3.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text3 = read
with open("metinler/metin4.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text4 = read
with open("metinler/metin5.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text5 = read
with open("metinler/metin6.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text6 = read
with open("metinler/metin7.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text7 = read
with open("metinler/metin8.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text8 = read
with open("metinler/metin9.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text9 = read
with open("metinler/metin10.txt" ,"r", encoding="utf-8") as file:
    read = file.read()
    text10 = read
#

bg = PhotoImage(file="images/sample.png")
bgg = tkinter.Label(root, image=bg)
bgg.place(relheight=1, relwidth=1)
logo = PhotoImage(file="images/logo.png")
root.iconphoto(False,logo)
lbl = Label(root,text = "Metni Seçin",font="Times 20 bold",fg="white",bg="black")
lbl.pack(anchor="center")
lbl2 = Label(root,text = "1 - 1 Sınav\n2 - 2 Sınav\n3 - 3 Sınav\n4 - 4 Sınav\n5 - 5 Sınav\n6 - 6 Sınav\n7 -7 Sınav\n8 - 8 Sınav\n9 - 9 Sınav\n10 - 10 Sınav",font="Times 15",justify="left",bg="black",fg="white")
lbl2.pack(anchor="w")

txt = Entry(root,width=25)
txt.focus_force()
txt.pack(ipadx=5,ipady=5)

txt2 = Entry(root,width=20)
txt2.place(x=365, y = 50)

txt3 = Entry(root,width=20)
txt3.place(x=365, y = 80)

txt4 = Entry(root,width=20)
txt4.place(x=365, y = 110)

inf = Label(root,text="İsim Soyisim:",font="Times 10 bold", bg="black",fg="white")
inf.place(x=277,y=50)

inf = Label(root,text="Sınıf ve Sınıf Numarası:",font="Times 10 bold", bg="black",fg="white")
inf.place(x=220,y=80)

inf = Label(root,text="Süre:",font="Times 10 bold", bg="black",fg="white")
inf.place(x=307,y=110)

inf = Label(root,text="github.com/CommandBreaker",font="Times 10 bold", bg="black",fg="white")
inf.place(x=5,y=475)

countt = 0


def toggler():
    if swvalue.get():
        swvalue.set(False)
        swvalue3.set(True)

def toggler2():
    if swvalue3.get():
        swvalue3.set(False)
        swvalue.set(True)

#ayar 1
inf = Label(root,text="Metin Renklendirilmesi (1) :",font="Times 10 bold", bg="black",fg="white")
inf.place(x=300,y=450)

swvalue = BooleanVar(root)
swvalue.set(False)

switchhighlight = Checkbutton(root,name="metin takibi",background="black" ,foreground="black",variable=swvalue, command=toggler2)
switchhighlight.place(x=461,y=450)

#ayar1
inf = Label(root,text="Metin Silme :",font="Times 10 bold", bg="black",fg="white")
inf.place(x=300,y=410)

swvalue22 = BooleanVar(root)
swvalue22.set(False)

switchhighlight22 = Checkbutton(root,name="metin silme",background="black" ,foreground="black",variable=swvalue22)
switchhighlight22.place(x=461,y=410)
#

#ayar2
inf = Label(root,text="Tam Ekran Sınav :",font="Times 10 bold", bg="black",fg="white")
inf.place(x=300,y=430)

swvalue2 = BooleanVar(root)
swvalue2.set(False)

switchhighlight2 = Checkbutton(root,name="tame ekran sınav",background="black" ,foreground="black",variable=swvalue2)
switchhighlight2.place(x=461,y=430)
#

#ayar3
inf = Label(root,text="Metin Renklendirilmesi (2) :",font="Times 10 bold", bg="black",fg="white")
inf.place(x=300,y=470)

swvalue3 = BooleanVar(root)
swvalue3.set(True)

switchhighlight2 = Checkbutton(root,name="metin takibi arka plan",background="black" ,foreground="black",variable=swvalue3,command=toggler)
switchhighlight2.place(x=461,y=470)
#


def clicked():
    if txt.get() == "" or txt2.get() == "" or txt3.get() == "" or txt4.get() == "" or txt4.get() == "":
        messagebox.showerror("HATA 456🦑", "Bazı Bilgiler Girilmemiş!")
        return
    try:
        if int(txt4.get()) <= 0 or int(txt4.get()) > 999999 :
            messagebox.showerror("HATA!", "Geçerli bir süre giriniz!")
            return
    except Exception as e:
        messagebox.showerror("ROMEWASNTBUILDINADAY", "Geçerli bir süre giriniz!")
        return
    try:
        if int(txt.get()) <= 0 or int(txt.get()) > 10:
            return
    except ValueError:
        return



    selection = str(txt.get())
    global filename
    global sinif
    global isim
    global totaltime
    totaltime = txt4.get()  # dakika
    isim = txt2.get()
    sinif = txt3.get()
    filename = txt2.get() + ".txt"
    root.destroy()
    examgui(selection)

btn = Button(root,text="Giriş",font="Times 20 bold", command=clicked,bg="black",fg="white")
btn.pack(ipady=10,ipadx=25,pady=10)

def blocker(event):
    return 'break'

highlight = 1
megacount = 0
selectedword = 0
UltraCounter = 0


def highlightplus(event):
    global highlight
    global megacount
    global xdtag
    global xdtag2
    global selectedword
    global UltraCounter

    wordlenght = len(selectedtext.split()[selectedword]) + 1 + UltraCounter
    if highlight == wordlenght:
        if str(event.keysym) == "space":
            highlight += 1
            UltraCounter += len(selectedtext.split()[selectedword]) + 1
            selectedword += 1
        return

    if str(event.keysym) == "BackSpace":
        try:
            test.tag_delete(xdtag2)
        except Exception as e:
            None
        xdtag2 = "highlight2_" + str(random.randint(0,999))
        test.tag_add(xdtag2, highlightedited2, tkinter.END)
        if swvalue.get():
            test.tag_configure(xdtag2, foreground="white")
        elif swvalue3.get():
            test.tag_configure(xdtag2, background="black")
        highlight -=1
        if highlight < 0 :
            highlight = 1
        return
    if (str(event.keysym) == "Tab") or (str(event.keysym) == "Escape") or (str(event.keysym) == "Control_R") or (str(event.keysym) == "Control_L") or (str(event.keysym) == "Shift_L") or (str(event.keysym) == "Shift_R") or (str(event.keysym) == "Caps_Lock") or (str(event.keysym) == "Win_L") or (str(event.keysym) == "App") or (str(event.keysym) == "Alt_L") or (str(event.keysym) == "Alt_R") or (str(event.keysym) == "F1") or (str(event.keysym) == "F2") or (str(event.keysym) == "F3") or (str(event.keysym) == "F4") or (str(event.keysym) == "F5") or (str(event.keysym) == "F6") or (str(event.keysym) == "F7") or (str(event.keysym) == "F8") or (str(event.keysym) == "F9") or (str(event.keysym) == "F10") or (str(event.keysym) == "F11") or (str(event.keysym) == "F12") or (str(event.keysym) == "Up") or (str(event.keysym) == "Down") or (str(event.keysym) == "Left") or (str(event.keysym) == "Right") or (str(event.keysym) == "space"):
        return
    highlight +=1
    if swvalue.get() or swvalue3.get():
        try:
            test.tag_delete(xdtag)
        except Exception as e:
            None
        xdtag = "highlight_" + str(random.randint(0,999))
        test.tag_add(xdtag, "1.0", highlightedited)
        if swvalue.get():
            test.tag_configure(xdtag, foreground="blue")
        elif swvalue3.get():
            test.tag_configure(xdtag, background="blue")

def examgui(number):
    global selectedtext
    exam = Tk()
    logo = PhotoImage(file="images/logo.png")
    exam.iconphoto(False, logo)
    exam.title(str(number) + " . Sınav")
    exam.focus_force()
    exam.geometry("800x800")
    if swvalue2.get():
        exam.attributes("-fullscreen", True)
    exam.resizable(False, False)

    if int(number) == 1:
        selectedtext = text1.replace("\n", "")
    elif int(number) == 2:
        selectedtext = text2.replace("\n", "")
    elif int(number) == 3:
        selectedtext = text3.replace("\n", "")
    elif int(number) == 4:
        selectedtext = text5.replace("\n", "")
    elif int(number) == 5:
        selectedtext = text5.replace("\n", "")
    elif int(number) == 6:
        selectedtext = text6.replace("\n", "")
    elif int(number) == 7:
        selectedtext = text7.replace("\n", "")
    elif int(number) == 8:
        selectedtext = text8.replace("\n", "")
    elif int(number) == 9:
        selectedtext = text9.replace("\n", "")
    elif int(number) == 10:
        selectedtext = text10.replace("\n", "")

    def donecheck():
        rawtext = str(examtxt.get("1.0", 'end-1c'))
        if int(len(rawtext.split()) < 10):
            messagebox.showerror("HATA 67 🤔","Çok az Kelime Yazdın Dostum (Klavyen Mi Bozuldu? 💔)")
            exam.destroy()
            return
        global examwords
        global resultwords
        examwords = selectedtext.split()
        resultwords = rawtext.split()
        global countt
        countt = 0
        toplamdogrukelime = 0
        for x in resultwords:
            if x == examwords[countt]:
                toplamdogrukelime += 1
            countt += 1

        yanliskelime = len(resultwords) - toplamdogrukelime
        toplamvurus = len(rawtext)
        vurushesaplama = (toplamvurus - yanliskelime * 20) / int(totaltime)

        messagebox.showinfo("Sonuç", "Toplam Vuruş Sayısı = " + str(toplamvurus) + "\nDoğru kelime sayısı = " + str(toplamdogrukelime) + "\nYanlış kelime sayısı = " + str(yanliskelime) + "\n\n\nHesaplanmış Not = " + str(vurushesaplama))
        filee2 = "sonuclar/" + str(filename)
        try:
            with open(filee2,"x", encoding="utf-8") as file:
                file.write("")
        except Exception as e:
            None
        try:
            with open(filee2,"w", encoding="utf-8") as file:
                today = date.today().strftime("%d.%m.%Y")
                file.write("Ftypers Sonuç |" + today + "| \n" + "----------------------------------------\n" + "Adı Soyadı : " + str(isim) + "\nTest Adı : " + str(number) + " Nolu Metin\n" + "Tarih : " + today + "\n----------------------------------------\n" + "TEST SONUÇLARI\n\n" + "Toplam Vuruş Sayısı = " + str(toplamvurus) + "\nDoğru kelime sayısı = " + str(toplamdogrukelime) + "\nYanlış kelime sayısı = " + str(yanliskelime)  + "\nSüre = " + str(totaltime) + " Dakika" + "\n\n#Hesaplama Formülü: Toplam Vuruş - Yanlış Kelime Sayısı * 20 / Dakika" + "\n\nHesaplanmış Not = " + str(vurushesaplama) + "\n----------------------------------------\n" + "Orjinal Metin\n\n" + selectedtext + "\n----------------------------------------\n" + "Öğrencinin Yazdığı Metin\n\n" + rawtext + "\n----------------------------------------\n" + str(isim) + "\n\n\n\n\n==========\nİmza")
        except Exception as e:
            None
        exam.destroy()

    bgg = PhotoImage(file="images/sample.png")
    bggg = tkinter.Label(exam, image=bgg)
    bggg.place(relheight=1, relwidth=1)
    timeleft = Label(exam, text="Sınav Süresi: 5 dakika",font="Times 15 bold",bg="black",fg="white")
    timeleft.pack(anchor="center")
    global test
    test = Text(exam, width=100, height=22,font="Times",bg="black",fg="white",wrap="word")
    test.insert(tkinter.END, selectedtext)
    test.pack(anchor="center", side="top")
    examtxt = Text(exam, width=100, height=25,font="Times",bg="black",fg="white",insertbackground="white",wrap="word")
    examtxt.focus_force()
    examtxt.pack(anchor="center", side="bottom")

    # 12 siniflara zorluk
    if not swvalue22.get():
        examtxt.bind("<BackSpace>", blocker)
        examtxt.bind("<Up>", blocker)
        examtxt.bind("<Down>", blocker)
        examtxt.bind("<Right>", blocker)
        examtxt.bind("<Left>", blocker)
    examtxt.bind("<Button>", blocker)
    examtxt.bind("<Control-c>", blocker)
    examtxt.bind("<Control-v>", blocker)
    examtxt.bind("<Control-a>", blocker)
    examtxt.bind("<Home>", blocker)
    examtxt.bind("<End>", blocker)
    examtxt.bind("<Delete>", blocker)
    test.bind("<Button>", blocker)
    examtxt.bind("<KeyRelease>", highlightplus)
    ttltime = int(totaltime)
    exam.after(ttltime * 60000, donecheck)
    starttime = time.time()
    try:
        while exam.winfo_exists():
            endtime = time.time()
            stime = endtime - starttime
            sstime = int(stime)
            mmtime = int(totaltime) * 60 - sstime
            mmmtime = mmtime // 60
            mmsstime = mmtime % 60
            global highlightedited
            global highlightedited2
            highlightedited = "1." + str(highlight)
            highlightedited2 = "1." + str(highlight - 2)
            if mmmtime > 0:
                timeleft.configure(text="Kalan Süre: " + str(mmmtime) + " Dakika " + str(mmsstime) + " Saniye")
            elif mmmtime <= 0:
                timeleft.configure(text="Kalan Süre: " + str(mmsstime) + " Saniye")

            root.update()
    except Exception as e:
        None

try:
    while root.winfo_exists():
        root.update()
except Exception as e:
    None
