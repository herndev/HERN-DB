import hern
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

class UI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
	
	#VARIABLES
	
	self.btn = {}
	self.btnn = []
	self.window_c = None
	self.window_u = None
	self.window_d = None
	self.directory = [0,0]
	self.vared2 = StringVar()
	self.vared3 = StringVar()
	self.vared4 = StringVar()
	self.choices = ["Database  ","Table         ","Insert Data"]
	
        
        #FONTS
        self.header_font = font.Font(size=13, weight="bold")
        self.btn_font = font.Font(size=10, weight="bold")
	
        #BANNER
        bnnr = PhotoImage(file="res/img/banner.gif")
        txt_banner = Label(self,text="", bg="Orange", image=bnnr)
        txt_banner.pack(side=TOP, fill=X, expand=True)
        
        #CONTROL
        tab_control = ttk.Notebook(self)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)
        tab4 = ttk.Frame(tab_control)
        tab5 = ttk.Frame(tab_control)
        tab6 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Database')
        tab_control.add(tab2, text='Create')
        tab_control.add(tab3, text='Update')
        tab_control.add(tab4, text='Delete')
        tab_control.add(tab5, text='Help')
        tab_control.add(tab6, text='About')
        
        
        #TAB1
        self.tab11 = Frame(tab1)
        self.tab11.pack(expand=True,fill = BOTH)
        txt11 = Label(self.tab11, text="DATABASE", font=self.header_font)
        txt11.pack()
	self.scrollbar11 = Scrollbar(self.tab11)
	self.scrollbar11.pack(side=RIGHT, fill=Y)
	self.lstbox11 = Listbox(self.tab11, height=20, yscrollcommand=self.scrollbar11.set)
	self.lstbox11.bind('<Double-1>',self.selected)
	self.lstbox11.pack(fill=BOTH, expand=True)
	self.scrollbar11.config(command=self.lstbox11.yview)
	self.displaydata()
        
        
        
        #TAB2
        tab22 = Frame(tab2)
        tab22.pack(expand=True,fill = BOTH)
        txt21 = Label(tab22, text="CREATE\n\n", font=self.header_font)
        txt21.pack()
	self.mframe22 = Frame(tab22)
	self.mframe22.pack()
	for i in self.choices:
	    radio = Radiobutton(self.mframe22, text=i, variable = self.vared2, value=i)
	    radio.pack(side=TOP)
	self.vared2.set("Database  ")
	btn21 = Button(self.mframe22, text="Proceed", font=self.btn_font, command=self.Create)
        btn21.pack()
	
        
        
        
        #TAB3
        tab33 = Frame(tab3)
        tab33.pack(expand=True,fill = BOTH)
        txt31 = Label(tab33, text="UPDATE", font=self.header_font)
        txt31.pack()
        
        
        
        #TAB4
        tab44 = Frame(tab4)
        tab44.pack(expand=True,fill = BOTH)
        txt41 = Label(tab44, text="DELETE", font=self.header_font)
        txt41.pack()
        
        
        #TAB5
        tab55 = Frame(tab5)
        tab55.pack(expand=True,fill = BOTH)
        txt51 = Label(tab55, text="HELP", font=self.header_font)
        txt51.pack()
        
        
        
        #ABOUT
        tab66 = Frame(tab6)
        tab66.pack(expand=True,fill=BOTH)
        txt61 = Label(tab66, text="ABOUT", font=self.header_font)
        txt61.pack()
        txt62 = Label(tab66, text="\n\nHern DB is a local database for python \ndeveloped by Hernie Jabien\n\n\n Email me @:mobilehacker45@gmail.com\nContact me @:09264760564")
        txt62.pack()
        
        #PACKING
        tab_control.pack(expand=1, fill='both')
        
        #BIN  IMG
        txt_banner.image = bnnr
    
    #DATABASE FUNCTIONS-------------------------------------------------------------------
    def displaydata(self, action=[]):
	db = hern.raw_database()
	if action == []:
	    for i in hern.raw_database():
		self.lstbox11.insert(0, i)
	else:
	    datax = Tk()
	    datax.title(action[-1])
	    mframe = Frame(datax)
	    mframe.pack(fill=BOTH, expand=True)
	    tframe = Frame(mframe)
	    tframe.pack(side=TOP, fill=X)
	    dframe = Frame(mframe)
	    dframe.pack(fill=BOTH, expand=True)
	    txt = Label(tframe, text="Database: %s\nTable: %s"%(action[0],action[1]))
	    txt.pack(side=LEFT)
	    grids = ttk.Treeview(dframe, show = "headings")
	    grids.grid(columnspan=2)
	    grids["columns"] = hern.tbreq(action[-1])
	    for i in hern.tbreq(action[-1]):
		grids.heading(i, text=i)
	    alls=[]
	    for i in hern.showall("haroharo"):
		asd = []
		for j in hern.tbreq("haroharo"):
		    asd.append(i[j])
		alls.append(asd)
	    tuples = alls
	    index = iid = 0
	    for row in tuples:
		grids.insert("", index, iid, values=row)
		index = iid = index + 1
	    datax.mainloop()
    def selected(self,event):
	index = self.lstbox11.curselection()
	label = self.lstbox11.get(index)
	if hern.checkdb(label):
	    self.lstbox11.delete(0, END)
	    for i in hern.raw_database():
		if i == label:
		    self.directory[0]=str(label) 
		    for j in hern.rawdb(i):
			self.lstbox11.insert(0, "  \__ " + j)
		self.lstbox11.insert(0, i)
	else:
	    self.directory[1]=str(label.split()[-1])
	    self.displaydata(self.directory)
    #END OF DATABASE FUNTIONS-------------------------------------------------------------
    
    
    #CREATE FUNCTIONS---------------------------------------------------------------------
    def Create(self):
	window = Tk()
	mframe = Frame(window)
	mframe.pack(fill=BOTH, expand=True)
	if self.vared2.get() == "Database  ":
	    window.title("Create Database")
	    txto1 = Label(mframe, text="Create New Database:")
	    txto1.pack()
	    inpuT1 = Entry(mframe)
	    inpuT1.pack()
	    btn1 = Button(mframe, text="Proceed", command=lambda:self.subCreate(inpuT1.get()))
	    btn1.pack(fill=X,expand=True)
	elif self.vared2.get() == "Table         ":
	    window.title("Create Table")
	    txto11 = Label(mframe, text="Existing Database:")
	    txto11.pack()
	    inpuT11 = Entry(mframe)
	    inpuT11.pack()
	    txto12 = Label(mframe, text="New Table:")
	    txto12.pack()
	    inpuT12 = Entry(mframe)
	    inpuT12.pack()
	    txto13 = Label(mframe, text="Number of Column:")
	    txto13.pack()
	    inpuT13 = Entry(mframe)
	    inpuT13.pack()
	    btn11 = Button(mframe, text="Proceed", command=lambda:self.subCreate(inpuT11.get(), inpuT12.get(), inpuT13.get()))
	    btn11.pack(fill=X,expand=True)
	elif self.vared2.get() == "Insert Data":
	    window.title("Create Table")
	    txto11 = Label(mframe, text="Database:")
	    txto11.grid(row=0,column=0, columnspan=2)
	    inpuT11 = Entry(mframe, width=40)
	    inpuT11.grid(row=1,column=0, columnspan=2)
	    txto12 = Label(mframe, text="Table:")
	    txto12.grid(row=2,column=0, columnspan=2)
	    inpuT12 = Entry(mframe, width=40)
	    inpuT12.grid(row=3,column=0, columnspan=2)
	    txto13 = Label(mframe, text="ID:")
	    txto13.grid(row=4,column=0)
	    inpuT13 = Entry(mframe)
	    inpuT13.grid(row=5,column=0)
	    txto14 = Label(mframe, text="Value:")
	    txto14.grid(row=4,column=1)
	    inpuT14 = Entry(mframe)
	    inpuT14.grid(row=5,column=1)
	    btn11 = Button(mframe, text="Proceed", width=38, command=lambda:self.subCreate(inpuT11.get(), inpuT12.get(), inpuT13.get(), inpuT14.get()))
	    btn11.grid(row=6,column=0, columnspan=2)
	window.mainloop()
	
	
    def subCreate(self, val1="", val2="", val3="", val4=""):
	lst = []
	tb_req = []
	self.window_c = Tk()
	mframe = Frame(self.window_c)
	mframe.pack(fill=BOTH, expand=True)
	if self.vared2.get() == "Database  ":
	    self.window_c.title("Create Database")
	    if val1 != "":
		hern.createdb(val1)
		txto1 = Label(mframe, text="New database created\nSuccessfuly!")
		txto1.pack()
	    else:
		txto1 = Label(mframe, text="Database can't be empty name!")
		txto1.pack()
	    btn1 = Button(mframe, text="OK", command=window.destroy)
	    btn1.pack(fill=X,expand=True)
	elif self.vared2.get() == "Table         ":
	    if val1 != "" and val2 != "" and val3 != "":
		for i in range(int(val3)):
		    lst.append(Entry(mframe))
		    lst[-1].pack()
		btn1 = Button(mframe, text="Proceed", command=lambda:self.subsubCreate(val1, val2,[i.get() for i in lst]))
		btn1.pack(fill=X,expand=True)
	    else:
		txto1 = Label(mframe, text="Fill everything!")
		txto1.pack()
	elif self.vared2.get() == "Insert Data":
	    if val3 != "" and val4 != "" and hern.checkdb(val1) and hern.checktb(val2):
		hern.connectdb(val1)
		tb_req = hern.tbreq(val2)
		for i in tb_req:
		    txt = Label(mframe, text=i + ":")
		    lst.append(Entry(mframe))
		    lst[-1].pack()
		btn1 = Button(mframe, text="Proceed", command=lambda:self.subsubCreate(val1, val2, [i.get() for i in lst], val3, val4))
		btn1.pack(fill=X,expand=True)
	    else:
		self.popuP("Error")
		self.exitC()
	self.window_c.mainloop()
    def subsubCreate(self, val1, val2, lst=[], val3="", val4=""):
	if self.vared2.get() == "Table         ":
	    if "" not in lst:
		print(lst)
		self.window_c.destroy()
	    else:
		self.popuP("Error")
    def popuP(self, msg, num=0):
	if num == 0:
	    messagebox.showerror(title="ERROR", message=msg, icon="warning")
	else:
	    messagebox.showinfo(title="SUCCESS", message=msg, icon="info")
    def exitC(self):
	self.window_c.destroy()

app = UI()
app.title("Hern DB")
app.geometry("400x500")
app.mainloop()
