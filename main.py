import qrcode
from PIL import ImageTk, Image
from tkinter import filedialog, Label, Button, Entry, Tk
import pyperclip as pc
import emoji


image = None

root = Tk()
root.title('QR Code Creator App')
root.geometry("700x300")
root.resizable(width=0,height=0)
label = Label(root, text="Enter link to create QR Code:", font=('bold',20), fg="black")
label.pack()
label.place(x=10,y=30)
entry1 = Entry(root,fg="black", bg="deepskyblue", width=30,font=('Helvetica', 15, 'bold'))
entry1.pack()
entry1.place(x=10, y=70)


def SchowekKop():
    ClipText = pc.paste()
    entry1.insert(0,ClipText)


schowek = Button(root,text=f'{emoji.emojize(":clipboard:")}Paste from Clipboard',font=('Helvetica', 8, 'bold'),width=20,command=SchowekKop,bg="cyan")
schowek.pack()
schowek.place(x=10,y=100)



def stworz_kod(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color = "white")
    img.save("1.png")




def clear():
    entry1.delete(first=0,last=500)





def stworz_pkod():
    global image

    text1 = entry1.get()
    if text1 == "":
        print("error 404")
    else:
        stworz_kod(text1)
        #photo = PhotoImage(file='C:/Users/mikja/PycharmProjects/QrCreator/1.png')
        #photo = photo.subsample(2)
        photo = Image.open('./1.png')
        image = photo
        photo = photo.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(photo)
        varun_label = Label(root, image=photo, bg="red")
        varun_label.image=photo

        varun_label.pack()
        varun_label.place(x=480,y=20)




def pobierz():
    # print("pobierz")
    #
    # qr = qrcode.QRCode(
    #     version=1,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border=4
    # )
    # qr.add_data(entry1.get())
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".png")
    image.save(filename.name)

Create = Button(root,text=f'{emoji.emojize(":check_mark_button:")}Create QR Code',font=('Helvetica', 8, 'bold'),width=45,command=stworz_pkod,bg="lime")
Create.pack()
Create.place(x=10,y=130)

Clearr = Button(root,text=f'{emoji.emojize(":cross_mark:")} Clear',font=('Helvetica', 8, 'bold'),width=22,command=clear,bg="red")
Clearr.pack()
Clearr.place(x=170,y=100)


Zapisz = Button(root,text=f'{emoji.emojize(":floppy_disk:")} Download',font=('Helvetica', 8, 'bold'),width=22,command=pobierz,bg="lightseagreen")
Zapisz.pack()
Zapisz.place(x=480,y=250)


root.mainloop()