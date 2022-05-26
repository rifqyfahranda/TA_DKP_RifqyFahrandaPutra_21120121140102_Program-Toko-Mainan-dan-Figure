from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.font import Font

root = Tk()
root.geometry("1200x700")
root.resizable(width=0,height=0)

#background dasar
class background:
    bg1 = ImageTk.PhotoImage(Image.open("C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/putih.jpg").resize((1200, 700)))
    labelbg = Label(root, image=bg1)
    labelbg.place(x=0, y=0)

#situs website, dipanggil berupa text
class website:
    mn1 = Label(root, text="www.wibuhobbystore.com", bg="white")
    mn1.place(x=480, y=43)
namatoko = Label(root, text=website.mn1)

#judul
class judul:
    judul = Label(root, text="Wibu Hobby Store", font=("Times New Roman", 20), bg="white")
    judul.place(x=450, y=10)

# label subjudul
class subjudul:
    nama = Label(root, text="Pilih Barang yang ingin dibeli", bg="white")
    nama2 = Label(root, text="Masukkan jumlah barang yang ingin dibeli", bg="white")
    nama3 = Label(root, text="Detail Pesanan: ", bg="white")
    nama.place(x=20, y=50)
    nama2.place(x=800, y=50)
    nama3.place(x=800, y=150)

# pemilihan barang
r = StringVar()
r.set("")
class barang:
    himiko = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/himikotoga.png')
    himiko_r = himiko.subsample(7)
    imagehimiko = Label(root, image=himiko_r)
    imagehimiko.place(x=50, y=90)
    e1 = Radiobutton(root, text="Pop Up Parade Himiko Toga (Boku no Hero Academia) : Rp 500.000", variable=r,
                     value='Pop Up Parade Himiko Toga (Boku no Hero Academia) : Rp 500.000', bg="white")
    e1.place(x=20, y=70)

    aqua = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/aquaa.png')
    aqua_r = aqua.subsample(5)
    imageaqua = Label(root, image=aqua_r)
    imageaqua.place(x=50, y=210)
    e2 = Radiobutton(root, text="Pop up Parade Aqua (Konosuba) : Rp 590.000", variable=r,
                     value='Pop up Parade Aqua (Konosuba) : Rp 590.000', bg="white")
    e2.place(x=20, y=190)

    venom = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/venom.png')
    venom_r = venom.subsample(6)
    imagevenom = Label(root, image=venom_r)
    imagevenom.place(x=50, y=360)
    e3 = Radiobutton(root, text="Nendoroid Venom (Marvel Comics) : Rp. 1.100.000", variable=r,
                     value='Nendoroid Venom (Marvel Comics) : Rp. 1.100.000', bg="white")
    e3.place(x=20, y=330)

    jack = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/jacksparrow.png')
    jack_r = jack.subsample(4)
    imagejack = Label(root, image=jack_r)
    imagejack.place(x=50, y=510)
    e4 = Radiobutton(root, text="Nendoroid Jack Sparrow (Pirataes of the Caribbean) Rp. 820.000", variable=r,
                     value='Nendoroid Jack Sparrow (Pirataes of the Caribbean) Rp. 820.000', bg="white")
    e4.place(x=20, y=480)

    ironman = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/ironman.png')
    ironman_r =ironman.subsample(6)
    imageironman = Label(root, image=ironman_r)
    imageironman.place(x=450, y=370)
    e5 = Radiobutton(root, text="Figma Iron Man Mark 7 (The Avengers) : Rp. 1.320.000", variable=r,
                      value='Figma Iron Man Mark 7 (The Avengers) : Rp. 1.320.000', bg="white")
    e5.place(x=420, y=340)

    kurapika = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/kurapika.jpg')
    kurapika_r =kurapika.subsample(7)
    imagekurapika = Label(root, image=kurapika_r)
    imagekurapika.place(x=450, y=90)
    e6 = Radiobutton(root, text="Figma Kurapika (Hunter x Hunter) : Rp. 1.450.000", variable=r,
                      value='Figma Kurapika (Hunter x Hunter) : Rp. 1.450.000', bg="white")
    e6.place(x=420, y=70)

    gojo = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/gojo.png')
    gojo_r =gojo.subsample(6)
    imagegojo = Label(root, image=gojo_r)
    imagegojo.place(x=450, y=210)
    e7 = Radiobutton(root, text="Figma Gojo Satoru (Jujutsu Kaisen) : Rp. 900.000", variable=r,
                      value='Figma Gojo Satoru (Jujutsu Kaisen) : Rp. 900.000', bg="white")
    e7.place(x=420, y=190)

    pubg = PhotoImage(file='C:/Users/rifqy/PycharmProjects/TugasAkhirPDKP/pubg.png')
    pubg_r =pubg.subsample(4)
    imagepubg = Label(root, image=pubg_r)
    imagepubg.place(x=450, y=510)
    e8 = Radiobutton(root, text="Figma The Lone Survivor (PUBG) : Rp. 1.200.000", variable=r,
                      value='Figma The Lone Survivor (PUBG) : Rp. 1.200.000', bg="white")
    e8.place(x=420, y=490)


# kolom jumlah pesanan
a = IntVar()
class pesanan:
    jumlahPesanan = Entry(root, width=10, bd=5)
    jumlahPesanan.place(x=800, y=70)


# tombol untuk menampilkan barang pesanan dan jumlahnya
class kelik:
    def clicked(value):
        toys = Label(root, text=pesanan.jumlahPesanan.get() + " pcs: " + value, bg="white")
        toys.place(x=800, y=170)

button = Button(root, text="Cek", command=lambda: kelik.clicked(r.get()))
button.place(x=800, y=100)


#tombol konfirmasi
def quit():
    opsi = messagebox.askyesno("yang benerrrr?", "yakinn mau udahan belanjanyaa?" )
    if opsi == 1:
        root.destroy()
    else:
        root.destroy()
        import main

tombolno = Button(root, text="Quit", command=quit)
tombolno.place(x=800, y=260)
konfirmasi = Label(root, text="Mau keluar dek? ", bg="white")
konfirmasi.place(x=800, y=240)

#setter getter
class wibu:
    def __init__(self,quote):
        self.quote = quote
    def setQuote(self, quote):
        self.quote = quote
        pass
    def getQuote(self):
        return self.quote

quotes = wibu("'Jauhi Kenakalan Remaja dengan menjadi Wibu'")
quotes = Label(root, text=quotes.getQuote(), font=("Segoe Print", 11), bg="white", )
quotes.place(x=820, y=670)


root.mainloop()