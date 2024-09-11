#official
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter 
import segno
from PIL import ImageTk,Image
import datetime
import qrcode as QR
import csv

class MultiPageApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Container to hold all the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to store different pages
        self.frames = {}

        # Create and add pages to the dictionary
        for PageClass in (Page1, Page2, Page3, Page4):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial page
        self.show_page("Page1")

    def show_page(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="sky blue")
        
        label = tk.Label(self, text="Welcome to QR code Generator",font=('Times New Roman', 20, 'bold'),bg='sky blue')
        label.place(relx=0.5,y=300,anchor=CENTER)     

        button = customtkinter.CTkButton(self, text="Continue", font=('Arial', 15), height=35, corner_radius=20, fg_color=('#5293BB'), command=lambda: controller.show_page("Page2"))
        button.place(relx=0.5,y=350,anchor=CENTER)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="sky blue")

        label1 = Label(self, text="Enter URL of the website: ",font=('Times New Roman', 20),bg="sky blue") 
        label1.place(relx=0.5,y=130, anchor=CENTER)
        
        label2 = Label(self, text="",font=('Times New Roman', 30)) 
        #label2.place(x=10,y=40)

        self.entry_var = tk.StringVar()
        self.entry_var.set("Enter website URL")
        self.entry = tk.Entry(self,width=40,font='Arial 10',textvariable=self.entry_var, fg="grey")
        self.entry.place(relx=0.5,y=160,anchor=CENTER)
        self.entry.bind("<FocusIn>", self.clear_prompt)
        
        def display():
            global url
            global name
            global timestamp
            var=self.entry.get()
            label2.configure(text=var)
            url=str(var)
            name=url[4:-4]+".png"
            qr = segno.make(url)
            qr.save(name)
            time=str(datetime.datetime.now())
            timestamp=time[:-10]
            
            self.canvas=Canvas(self,width=150,height=150,bg='sky blue')
            self.canvas.pack(pady=250,anchor=CENTER)
            img_path=name
            self.img=PhotoImage(file=img_path)
            self.img_item=self.canvas.create_image(75,75,anchor=CENTER,image=self.img)

            
        button1 = customtkinter.CTkButton(self, text="Generate QR code",font=('Arial', 15),height=35, corner_radius=15, fg_color=('#3776A1'),command=display)
        button1.place(relx=0.5,y=210,anchor=CENTER)

        button2 = customtkinter.CTkButton(self, text="Customize",font=('Arial', 15),height=35, corner_radius=15, fg_color=('#3776A1'),command=lambda: controller.show_page("Page3"))
        button2.place(x=270,y=450)

        button3 = customtkinter.CTkButton(self, text="Display previous",font=('Arial', 15),height=35, corner_radius=15, fg_color=('#3776A1'), command=lambda: controller.show_page("Page4"))
        button3.place(x=440, y=450)

    def clear_prompt(self, event):
        if self.entry_var.get() == "Enter website URL":
            self.entry_var.set("")
            self.entry.config(fg="black")

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg='sky blue')

        global url
        global name
        
        customlabel=Label(self, text='Customization',font=('Times New Roman',20),bg='sky blue')
        sizelabel = Label(self, text="enter size:",font=('Times New Roman', 15),bg='sky blue') 
        colorlabel = Label(self, text="enter color:",font=('Times New Roman', 15),bg='sky blue') 
        logolabel=Label(self, text="enter png name:",font=('Times New Roman', 15),bg='sky blue')
        errorlabel=Label(self, text="",font=('Times New Roman', 15),bg='sky blue')

        
        self.entrysize_var = tk.StringVar()
        self.entrysize_var.set("Enter size")
        self.entrysize = tk.Entry(self,font='Arial 10',textvariable=self.entrysize_var, fg="grey",width=25)
        self.entrysize.bind("<FocusIn>", self.clear_promptsize)

        self.entrycolor_var = tk.StringVar()
        self.entrycolor_var.set("Enter color")
        self.entrycolor = tk.Entry(self,font='Arial 10', textvariable=self.entrycolor_var, fg="grey",width=25)
        self.entrycolor.bind("<FocusIn>", self.clear_promptcolor)
        
        self.entrypng_var = tk.StringVar()
        self.entrypng_var.set("Enter logo path")
        self.entrypng = tk.Entry(self,font='Arial 10', textvariable=self.entrypng_var, fg="grey",width=25)
        self.entrypng.bind("<FocusIn>", self.clear_promptpng)
        
        def customise():
            global url
            global name
            global timestamp

            size=int(self.entrysize.get())
            color=str(self.entrycolor.get())
            logo=str(self.entrypng.get())


            
            '''try:
                global size
                size=int(self.entrysize.get())
            except:
                size=10
                errorlabel.configure(text="enter a number")
                errorlabel.place(x=375,y=500)

            try:
                global color
                color=str(self.entrycolor.get())
            except KeyError:
                errorlabel.configure(text="color does not exist")
                errorlabel.place(x=375,y=500)
            except ValueError:
                errorlabel.configure(text="color does not exist")
                errorlabel.place(x=375,y=500)

            try:
                global logo
                logo=str(self.entrypng.get())
            except FileNotFoundError:
                errorlabel.configure(text="path does not exist")
                errorlabel.place(x=375,y=500)'''



            if color=="Enter color":
                color="white"

            qrcode = segno.make(url)
            qrcode.save(name,scale=size,light=color)


            if logo=="Enter logo path":
                pass
            else:
                logolink = str(self.entrypng.get())
                logo = Image.open(logolink)
                basewidth = 100
                wpercent = (basewidth/float(logo.size[0]))
                hsize = int((float(logo.size[1])*float(wpercent)))
                logo = logo.resize((basewidth, hsize), Image.LANCZOS)
                QRcode = QR.QRCode(error_correction=QR.constants.ERROR_CORRECT_H)
                QRcode.add_data(url)
                QRcode.make()
                QRimg = QRcode.make_image(fill_color="black", back_color=color).convert('RGB')
                pos = ((QRimg.size[0] - logo.size[0]) // 2,
                       (QRimg.size[1] - logo.size[1]) // 2)
                QRimg.paste(logo, pos)
                QRimg.save(name)
            
            new_window = tk.Toplevel(self)
            new_window.title("QR Code")
            self.canv=Canvas(new_window,width=500,height=500)
            self.canv.pack()
            img_path=name
            self.img=PhotoImage(file=img_path)
            self.img_item=self.canv.create_image(50,50,anchor=NW,image=self.img)

            saveQR([url, size, color, timestamp])

        def saveQR(data, saveLocn="csvfile.csv"):
            with open(saveLocn, "a+", newline = '') as fh: #Appends row to the CSV file
                fh.seek(0, 0)
                rw = csv.reader(fh)
                fh.seek(0, 2)
                if data not in rw:
                    rw = csv.writer(fh)
                    rw.writerow(data)

        button1 = customtkinter.CTkButton(self, text="Regenerate QR Code",font=('Arial', 15), command=customise, height=35, corner_radius=15, fg_color='#3776A1')
        
        #button2 = tk.Button(self, text="Customize", command=lambda: controller.show_page("Page3"))

        backButton = customtkinter.CTkButton(self, text="Go back",font=('Arial', 15),height=35, corner_radius=20, fg_color=('#5293BB'), command=lambda: controller.show_page("Page2"))
        
        customlabel.place(relx=0.5, y=150, anchor=CENTER)
        sizelabel.place(x=250, y=200)
        colorlabel.place(x=250, y=250)
        logolabel.place(x=250, y=300)
        self.entrysize.place(x=390, y=205)
        self.entrycolor.place(x=390, y=255)
        self.entrypng.place(x=390, y=305)
        button1.place(relx=0.5, y=400, anchor=CENTER)
        backButton.place(x=50, y=550)

    def clear_promptsize(self, event):
        if self.entrysize_var.get() == "Enter size":
            self.entrysize_var.set("")
            self.entrysize.config(fg="black")
    def clear_promptcolor(self, event):
        if self.entrycolor_var.get() == "Enter color":
            self.entrycolor_var.set("")
            self.entrycolor.config(fg="black")
    def clear_promptpng(self, event):
        if self.entrypng_var.get() == "Enter logo path":
            self.entrypng_var.set("")
            self.entrypng.config(fg="black")

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg='sky blue')
        
        self.parent = parent
        self.populate()

    def viewHistory(saveLocn="csvfile.csv"):
        with open("csvfile.csv", "r", newline = '') as fh:
            rd = csv.reader(fh)
            return tuple(rd)

    def populate(self):
        def deleteQR(j, saveLocn="csvfile.csv"):
            lst = []
            with open(saveLocn, "r", newline= '') as fh:
                rw = csv.reader(fh)
                rw = list(rw)
                rw.pop(0)

            with open(saveLocn, "w", newline = '') as fh:
                wr = csv.writer(fh)
                #wr.writerows(lst)
                wr.writerows(rw)
                fh.close()

            self.populate()

        for widget in self.grid_slaves():
            widget.grid_forget()
        #Create header for grid
        j= 0
        fields = ["URL","Size","Color","Timestamp"]
        for i in fields:
            header = tk.Label(self, text=i,font=('Times New Roman', 18 ),bg='sky blue')
            header.grid(row = 1, column=j, pady = 20, padx= 40)
            j+=1

        #Populate the grid with information from csvfile
        info = self.viewHistory()
        j=2
        for i in info:
            for k in range(len(i)):
                field = tk.Label(self, text=i[k],font=('Times New Roman', 15),bg='sky blue')
                field.grid(row = j, column= k, pady = 4, padx = 4)
            deleteBtn = customtkinter.CTkButton(self, text="Delete",font=('Arial', 15), height=35, corner_radius=15, fg_color='#3776A1', command=lambda: deleteQR(j))
            deleteBtn.grid(row = j, column= 5, pady = 4, padx = 50)
            j+=1

        backButton = customtkinter.CTkButton(self, text="Go back",font=('Arial', 15),height=35, corner_radius=20, fg_color=('#5293BB'), command=lambda: self.controller.show_page("Page2"))
        #backButton.grid(row = 0, column = 0, padx= 10, pady= 20)
        backButton.place(x=40,y=550)
        
        refrButton = customtkinter.CTkButton(self, text="Refresh",font=('Arial', 15),height=35, corner_radius=20, fg_color=('#5293BB'), command=lambda: self.populate())
        refrButton.grid(row=0, column=5, padx=20, pady=50)
        #refrButton.place(x=425,y=100)
        
if __name__ == "__main__":
    app = MultiPageApp()
    app.geometry("850x650")
    app.title("QR Code Generator")
    app.mainloop()
