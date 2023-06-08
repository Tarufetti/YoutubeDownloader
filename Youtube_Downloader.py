import customtkinter
from customtkinter import filedialog
from pytube import YouTube
from PIL import Image
from CTkMessagebox import CTkMessagebox
import os

root = customtkinter.CTk()
root.title('Youtube Downloader')
cwd = os.getcwd()
root.iconbitmap(f'{cwd}\\resources\\icono.ico')
root.geometry('400x450')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
customtkinter.set_appearance_mode('system')


def yt_download():
    url = entry.get()
    yt = YouTube(url)
    destination_path = destination_entry.get()
    if dropdown_options_clicked.get() == 'Audio/Video':
        stream = yt.streams.filter(progressive=True).order_by('resolution').desc()
        video = stream.first()
    elif dropdown_options_clicked.get() == 'Audio': #revisar el tema del formato
        stream = yt.streams.filter(only_audio=True).order_by('abr').desc()
        video = stream.first()
    elif dropdown_options_clicked.get() == 'Video': #revisar resolucion
        stream = yt.streams.filter(only_video=True).order_by('resolution').desc()
        video = stream.first()
    if destination_path == '':
        cwd = os.getcwd()
        if not os.path.isdir(f'{cwd}/Descargas'):
            os.mkdir(f'{cwd}/Descargas')
        video.download(f'{cwd}/Descargas')
    else:
        video.download(destination_path)
    CTkMessagebox(title='Youtube Downloader', icon = 'check', message = 'Descarga completa!', option_1 = 'OK', button_color='red')

def directory():
    my_dir = filedialog.askdirectory()
    destination_entry.configure(placeholder_text=my_dir)
    destination_entry.insert(0,my_dir)

frame = customtkinter.CTkFrame(master=root)
frame.grid(row=0, column=0,columnspan=2, pady=20, padx=60, sticky='nsew')
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

label1 = customtkinter.CTkLabel(master=frame, text='Youtube Downloader', font=('SF Pro Text Regular',24))
label1.grid(row=0, column=1,columnspan=4, pady=10,padx=10)
label1.place(relx=0.5,rely=0.1,anchor='center')

img = customtkinter.CTkImage(Image.open(f'{cwd}\\resources\\yo-logo-HD.png'),size=(87,61))
img_label = customtkinter.CTkLabel(master=frame,text='', image=img)
img_label.grid(row=1, column=1,columnspan=4, pady=10,padx=10,sticky='nsew')
img_label.place(relx=0.5,rely=0.3,anchor='center')

entry = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese URL', width=220, font=('SF Pro Text Regular',12))
entry.grid(row=2, column=1,columnspan=4, pady=10,padx=10,sticky='nsew')
entry.place(relx=0.5,rely=0.5,anchor='center')

destination_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese destino', width=140, font=('SF Pro Text Regular',12))
destination_entry.grid(row=3, column=1,columnspan=4, pady=10,padx=(35,1), sticky='w')
destination_entry.place(relx=0.4,rely=0.62,anchor='center')

directory_img = customtkinter.CTkImage(dark_image=Image.open(f'{cwd}\\resources\\directory.png'),size=(40,40))
destination_button = customtkinter.CTkButton(master=frame, width=0,height=0, text='', image=directory_img,fg_color='transparent',hover_color='#8B0000', command=directory)
destination_button.grid(row=3, column=1,columnspan=10, pady=5,padx=(1,30), sticky='e')
destination_button.place(relx=0.8,rely=0.62,anchor='center')

dropdown_options = ['Audio/Video', 'Video', 'Audio']
dropdown_options_clicked = customtkinter.StringVar()
dropdown_options_clicked.set(dropdown_options[0])
dropdown = customtkinter.CTkOptionMenu(master=frame,width=100, values=dropdown_options, variable=dropdown_options_clicked, fg_color='red', button_color='red', button_hover_color='#8B0000', font=('SF Pro Text',12))
dropdown.grid(row=4, column=1,columnspan=2, pady=10,padx=10,sticky='nsew')
dropdown.place(relx=0.5,rely=0.75,anchor='center')

button = customtkinter.CTkButton(master=frame, text='Descargar',fg_color='red', hover_color='#8B0000', width=100, font=('SF Pro Text Regular',12), command= yt_download)
button.grid(row=5, column=1,columnspan=2, pady=10,padx=10,sticky='nsew')
button.place(relx=0.5,rely=0.87,anchor='center')

label2 = customtkinter.CTkLabel(master=root, text='by Tarufetti 2023', font=("SF Pro Text Regular", 10))
label2.grid(row=8, column=0, pady=10,padx=10,sticky='nsew')

root.mainloop()