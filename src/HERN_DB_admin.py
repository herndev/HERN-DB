#LocalDatabaseBETA V1.6
#By: Hernie Jabien
#Copyright @ Syntaxer 2019 all rights reserved.

import os
st = open("hern.py", "w+")
st.write("#ANY MODIFICATION OF THE FILE ARE STRICTLY PROHIBITED\n#DO NOT COPY ANY PARTS OF THIS FILE WITHOUT ANY PERMISSION TO THE DEVELOPER\n\nimport os\nnewpath1 = r'Database' \nnewpath2 = r'res' \nif not os.path.exists(newpath1):\n\tos.makedirs(newpath1)\nif not os.path.exists(newpath2):\n\tos.makedirs(newpath2)\n\tos.makedirs('res/config')\n\tos.makedirs('res/config/cache')\n\ttst = open('res/config/prio', 'w+')\n\ttst.write('')\n\ttst.close()\nfiles_in_db = os.listdir('Database')\ndef prio(Database):\n\tdata = open('res/config/prio', 'w+')\n\tdata.write('%s'%Database)\n\tdata.close()\n\ndef getprio():\n\tdata = open('res/config/prio', 'r+')\n\tdeta = data.read()\n\tdata.close()\n\treturn deta\ndef decrypt(stR, action=''):\n\tdic = {}\n\td = ''\n\ttempor = ''\n\tif action == 'cache':\n\t\tstR = stR.splitlines()\n\t\ttemp = stR[0].split()\n\t\tdic[temp.pop(0)] = temp\n\t\tstR.pop(0)\n\t\tfor i in stR:\n\t\t\ttempor = i.split()\n\t\t\tif len(tempor) > 1:\n\t\t\t\tfor x,j in enumerate(tempor):\n\t\t\t\t\tif x % 2:\n\t\t\t\t\t\tdic[d] = j\n\t\t\t\t\t\td = ''\n\t\t\t\t\telse:\n\t\t\t\t\t\td = j\n\t\t\telse:\n\t\t\t\tif len(tempor) > 0:\n\t\t\t\t\tdic[tempor[0]] = ''\n\telse:\n\t\tstR = stR.splitlines() \n\t\tfor i in stR:\n\t\t\ttemp = i.split()\n\t\t\tif len(temp) > 1:\n\t\t\t\ttempor = temp.pop(0)\n\t\t\t\tdic[tempor] = ' '.join(temp)\n\t\t\telse:\n\t\t\t\tif len(temp) > 0:\n\t\t\t\t\tdic[temp[0]] = ''\n\treturn dic\n\ndef encrypt(Dictionary, action=''):\n\ttemp = ''\n\tif type(Dictionary) == dict:\n\t\tif action == 'cache':\n\t\t\tfor i in Dictionary:\n\t\t\t\tif type(Dictionary[i]) == str:\n\t\t\t\t\ttemp += i + ' ' + Dictionary[i] + '\\n'\n\t\t\t\telse:\n\t\t\t\t\ttemp += i + ' ' + ' '.join(Dictionary[i]) + '\\n'\n\t\telse:\n\t\t\tfor i in Dictionary:\n\t\t\t\ttemp += i + ' ' + Dictionary[i] + '\\n'\n\t\treturn temp\n\telse:\n\t\treturn False\ndef check_database():\n\tif len(list_of_files) > 0:\n\t\treturn False\n\telse:\n\t\treturn True\n\ndef checkdb(Database):\n\tmpath = r'Database/' + Database\n\tif os.path.exists(mpath):\n\t\treturn True\n\telse:\n\t\treturn False\n\ndef checktb(Database,Table):\n\tmpath = r'Database/' + Database + '/' + Table\n\tif os.path.exists(mpath):\n\t\treturn True\n\telse:\n\t\treturn False\ndef raw_tree():\n\tmerger = ''\n\tstartpath = 'Database'\n\tfor root, dirs, files in os.walk(startpath):\n\t\tlevel = root.replace(startpath, '').count(os.sep)\n\t\tindent = ' ' * 4 * (level)\n\t\tmerger += '{}{}/'.format(indent, os.path.basename(root)) + '\\n'\n\t\tsubindent = ' ' * 4 * (level + 1)\n\t\tfor f in files:\n\t\t\tmerger += '{}{}'.format(subindent, f) + '\\n'\n\treturn merger\n\ndef raw_database():\n\tmpath = os.listdir('Database')\n\treturn mpath\n\ndef rawdb(Database):\n\tmpath = os.listdir('Database/%s'%Database)\n\treturn mpath\n\ndef rawtb(Database,Table):\n\tmpath = os.listdir('Database/%s/%s'%(Database,Table))\n\treturn mpath\ndef showall(Table):\n\tdb = getprio()\n\ttemp = {}\n\td = {}\n\tl = []\n\ttry:\n\t\tfor i in rawtb(db, Table):\n\t\t\tdata = open('Database/%s/%s/%s'%(db,Table,i), 'r+')\n\t\t\tdeta = data.read()\n\t\t\tdata.close()\n\t\t\td = decrypt(deta)\n\t\t\tif d != {}:\n\t\t\t\tl.append(d)\n\t\tif l == []:\n\t\t\treturn False\n\t\telse:\n\t\t\treturn l\n\texcept:\n\t\treturn False\ndef createdb(Database):\n\tif not checkdb(Database):\n\t\tos.makedirs('Database/%s'%Database)\n\t\tos.makedirs('res/config/cache/%s'%Database)\n\t\tprio(Database)\n\t\treturn True\n\telse:\n\t\tprio(Database)\n\t\treturn False\n\ndef createtb(Table, List):\n\tdb = getprio()\n\ttry:\n\t\tos.makedirs('Database/%s/%s'%(db,Table))\n\t\tdata = open('res/config/cache/%s/%s'%(db,Table), 'a')\n\t\tdata.write('%s %s\\ncount 10000000000'%(Table,' '.join(List)))\n\t\tdata.close()\n\t\treturn True\n\texcept:\n\t\treturn False\n\t\t\ndef connectdb(Database):\n\tif checkdb(Database):\n\t\tprio(Database)\n\treturn checkdb(Database)\n\t\n\ndef connecttb(Table):\n\tdb = getprio()\n\tif db is not '':\n\t\treturn checktb(db, Table)\n\telse:\n\t\treturn False\n\t\t\ndef tbreq(Table):\n\tdb = getprio()\n\tif db is not '':\n\t\tif checktb(db,Table):\n\t\t\tdata = open('res/config/cache/%s/%s'%(db,Table), 'r+')\n\t\t\tdeta = data.read()\n\t\t\tdata.close()\n\t\t\td = decrypt(deta)\n\t\t\tdata = d[Table].split()\n\t\t\treturn(data)\n\telse:\n\t\treturn False\ndef insertdata(Table, Dictionary):\n\tdb = getprio()\n\tpure_data = False\n\ttemp = ''\n\td = {}\n\ttry:\n\t\tdata = open('res/config/cache/%s/%s'%(db,Table), 'r+')\n\t\tdeta = data.read()\n\t\tdata.close()\n\t\td = decrypt(deta)\t\t\t\n\t\tfor i in Dictionary:\n\t\t\tif i in d[Table]:\n\t\t\t\ttemp += i + ' ' + Dictionary[i] + '\\n'\n\t\t\t\tpure_data = True\n\t\t\telse:\n\t\t\t\tpure_data = False\n\t\t\t\tbreak\n\t\tif pure_data:\n\t\t\tdata = open('Database/%s/%s/a%s'%(db,Table,d['count']), 'w+')\n\t\t\tdata.write('%s'%temp)\n\t\t\tdata.close()\t\t\n\t\t\td['count'] = str(int(d['count']) + 1)\n\t\t\td = encrypt(d, 'cache')\t\t\n\t\t\tdata = open('res/config/cache/%s/%s'%(db,Table), 'w+')\n\t\t\tdata.write('%s'%d)\n\t\t\tdata.close()\n\t\t\treturn True\n\t\telse:\n\t\t\treturn False\n\texcept:\n\t\treturn False\ndef selectdata(Table, Dictionary, List=[]):\n\tdb = getprio()\n\ttemp = {}\n\td = {}\n\tl = []\n\ttry:\n\t\tfor i in rawtb(db, Table):\n\t\t\tdata = open('Database/%s/%s/%s'%(db,Table,i), 'r+')\n\t\t\tdeta = data.read()\n\t\t\tdata.close()\n\t\t\td = decrypt(deta)\n\t\t\tfor j in Dictionary:\n\t\t\t\tif j in d.keys():\n\t\t\t\t\tif Dictionary[j] == d[j]:\n\t\t\t\t\t\ttemp = dict(d)\n\t\t\t\t\t\tif List != []:\n\t\t\t\t\t\t\tfor i in d:\n\t\t\t\t\t\t\t\tif i not in List:\n\t\t\t\t\t\t\t\t\ttemp.pop(i)\n\t\t\t\t\t\tl.append(temp)\n\t\t\t\t\t\t\t\t\t\t\n\t\tif l == []:\n\t\t\treturn False\n\t\telif len(l) == 1:\n\t\t\treturn l[0]\n\t\telse:\n\t\t\treturn l\n\texcept:\n\t\treturn False\ndef updatedata(Table, Dictionary1, Dictionary2):\n\tdb = getprio()\n\ttemp = {}\n\td = {}\n\ttry:\n\t\tfor i in rawtb(db, Table):\n\t\t\tdata = open('Database/%s/%s/%s'%(db,Table,i), 'r+')\n\t\t\tdeta = data.read()\n\t\t\tdata.close()\n\t\t\td = decrypt(deta)\n\t\t\tfor j in Dictionary1:\n\t\t\t\tif j in d.keys():\n\t\t\t\t\tif Dictionary1[j] == d[j]:\n\t\t\t\t\t\tfor x in Dictionary2:\n\t\t\t\t\t\t\td[x] = Dictionary2[x]\n\t\t\t\t\t\ttemp = encrypt(d)\n\t\t\t\t\t\tdata = open('Database/%s/%s/%s'%(db,Table,i), 'w+')\n\t\t\t\t\t\tdata.write('%s'%temp)\n\t\t\t\t\t\tdata.close()\t\n\t\t\t\t\t\treturn True\n\t\t\t\t\telse:\n\t\t\t\t\t\tbreak\n\t\treturn False\n\texcept:\n\t\treturn False\ndef deletedata(Table, Dictionary):\n\tdb = getprio()\n\ttemp = {}\n\td = {}\n\ttry:\n\t\tfor i in rawtb(db, Table):\n\t\t\tdata = open('Database/%s/%s/%s'%(db,Table,i), 'r+')\n\t\t\tdeta = data.read()\n\t\t\tdata.close()\n\t\t\td = decrypt(deta)\n\t\t\tfor j in Dictionary:\n\t\t\t\tif j in d.keys():\n\t\t\t\t\tif Dictionary[j] == d[j]:\n\t\t\t\t\t\tdata = open('Database/%s/%s/%s'%(db,Table,i), 'w+')\n\t\t\t\t\t\tdata.write('')\n\t\t\t\t\t\tdata.close()\t\n\t\t\t\t\t\tos.remove('Database/%s/%s/%s'%(db,Table,i))\n\t\t\t\t\t\treturn True\n\t\t\t\t\telse:\n\t\t\t\t\t\tbreak\n\t\treturn False\n\texcept:\n\t\treturn False")
st.close()
st = open("READ ME.txt", "w+")
st.write("HERN DB BETA V1.6\nby: Hernie Jabien\n\n- A local database module application for python language.\n\nFAQS:\n\tHow to install HERN DB?\n\t-----\n\t|\tAnswer: No need installation, all you need to do is to copy the executable file to\n\t|\t\t\tyour project's directory and import the 'hern.py' module file to you project.\n\t|\n\t|\tSyntax: import hern\n\t-----\n\tHow to use HERN DB?\n\t-----\n\t|\tAnswer: After successfully imported the module you can now use the module to perform\n\t|\t\t\tHERN DB functions or you can run the executable file 'HERN_DB_admin.exe' to\n\t|\t\t\tmanipulate Data (Go to HERN_DB_admin's Help page to avoid syntax errors).\n\t-----\n\n\nCopyright 2019 @ Hernie Jabien all rights reserved.")
st.close()
import hern
import random
import time, subprocess
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class UI(Tk):
    def __init__(self, *args, **kwargs):
	Tk.__init__(self, *args, **kwargs)
	
	#VARIABLES
	self.trash = ""
	self.btn = {}
	self.btnn = []
	self.window = None
	self.directory = [0,0]
	self.temp_db = ""
	self.temp_tb = ""
	self.temp_num = ""
	self.temp_id = ""
	self.temp_val = ""
	self.txt_banner = []
	self.vared2 = StringVar()
	self.vared3 = StringVar()
	self.vared4 = StringVar()
	
        
        #FONTS
	self.bnnr_font = font.Font(size=25, weight="bold")
        self.header_font = font.Font(size=13, weight="bold")
        self.btn_font = font.Font(size=10, weight="bold")
	
        #BANNER
	bnnr_frame = Frame(self, bg="#272727")
	bnnr_frame.pack(side=TOP, fill=BOTH, expand=True)
	self.bnnr_frame = Frame(bnnr_frame, bg="#272727")
	self.bnnr_frame.pack(side=TOP)
	for i in "HERN DB":
	    self.txt_banner.append(Label(self.bnnr_frame, font=self.bnnr_font,height=4,text=i, fg="White", bg="#272727"))
	    self.txt_banner[-1].pack(side=LEFT)
        
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
        txt11 = Button(self.tab11, text="REFRESH", font=self.header_font, command=self.Refresh)
        txt11.pack(fill=X)
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
	for i in ["Database  ","Table         ","Insert Data"]:
	    radio = Radiobutton(self.mframe22, text=i, variable = self.vared2, value=i)
	    radio.pack(side=TOP)
	self.vared2.set("Database  ")
	btn21 = Button(self.mframe22, text="Proceed", font=self.btn_font ,command=self.Create)
        btn21.pack()
	
        
        
        
        #TAB3
        tab33 = Frame(tab3)
        tab33.pack(expand=True,fill = BOTH)
        txt31 = Label(tab33, text="UPDATE\n\n", font=self.header_font)
        txt31.pack()
        self.mframe33 = Frame(tab33)
	self.mframe33.pack()
	for i in ["Update Data"]:
	    radio = Radiobutton(self.mframe33, text=i, variable = self.vared3, value=i)
	    radio.pack(side=TOP)
	self.vared3.set("Update Data")
	btn21 = Button(self.mframe33, text="Proceed", font=self.btn_font ,command=self.Update)
        btn21.pack()
        
        
        #TAB4
        tab44 = Frame(tab4)
        tab44.pack(expand=True,fill = BOTH)
        txt41 = Label(tab44, text="DELETE\n\n", font=self.header_font)
        txt41.pack()
        self.mframe44 = Frame(tab44)
	self.mframe44.pack()
	for i in ["Database  ","Table         ","Delete Data"]:
	    radio = Radiobutton(self.mframe44, text=i, variable = self.vared4, value=i)
	    radio.pack(side=TOP)
	self.vared4.set("Database  ")
	btn21 = Button(self.mframe44, text="Proceed", font=self.btn_font ,command=self.Delete)
        btn21.pack()
        
        #TAB5
        tab55 = Frame(tab5)
        tab55.pack(expand=True,fill = BOTH)
        txt51 = Label(tab55, text="HELP", font=self.header_font)
        txt51.pack(fill=X)
	self.txt55 = ScrolledText(tab55)
	self.txt55.pack(fill=BOTH, expand=True)
        self.txt55.insert(INSERT,"\n[ C.R.U.D. ]\n\n------------------- CREATE -------------------\n\ncreatedb('New database')\n-Create's a new database and serves as a connection if database already exist.\n\ncreatetb('New table',['entity1','entity2',..])\n-Create's new table to an existing database.\n\ninsertdata('Table', {'entity':'value',..})\n-Insert a new data to an existing table.\n\n-------------------- READ --------------------\n\n")
        self.txt55.insert(INSERT,"raw_tree()\n-Returns database directory tree.\n\nraw_database()\n-Returns list of databases.\n\nrawdb('Database')\n-Return's list of tables in the given database.\n\nshowall('Table')\n-Return's list of raw datas in the given table.\n\nselectdata('Table', {'entity':'value'})\n-Return's all the data that contained the given entity value.\n\n------------------- UPDATE -------------------\n\n")
        self.txt55.insert(INSERT,"updatedata('Table', {'entity':'value'}, {'entity':'value',..})\n-Updates data in the database uses the first dictionary parameter to locate the data and the second dictionary is the one that replaces the old data.\n\n------------------- DELETE -------------------\n\ndeletedata('Table', {'entity':'value'})\n-Delete's the data that contained the given entity value.\n\n\n[ EXTRA FUNCTIONS ]\n\n------------------- EXTRAS -------------------\n\n")
	self.txt55.insert(INSERT,"connectdb('Database')\n-Create's a connection to the database.\n\ntbreq('Table')\n-Return's a list of requirements of the given table.\n\ncheckdb('Database')\n-Check's the given database if exist.\n\nchecktb('Table')\n-Check's the given table if exist.\n\ncheck_database()\n-Check's if database is not empty.")


        #ABOUT
        tab66 = Frame(tab6)
        tab66.pack(expand=True,fill=BOTH)
        txt61 = Label(tab66, text="ABOUT", font=self.header_font)
        txt61.pack()
        txt62 = Label(tab66, text="\n\nHern DB is a local database for python \ndeveloped by Hernie Jabien\n\n\n Email me @:mobilehacker45@gmail.com\nContact me @:09264760564")
        txt62.pack()
	txt63 = Label(tab66, font=("Arial",8,"bold"), text="COPYRIGHT 2019 @ HERNIE JABIEN ALL RIGHTS RESERVED.")
        txt63.pack(side=BOTTOM, fill=X)
        
        #PACKING
        tab_control.pack(expand=1, fill='both')
        
	#ANIM
	self.Anim_banner()
	
	
    
    def Anim_banner(self):
	used = []
	col = ""
	color = ["orange", "red", "blue", "green", "yellow", "violet"]
	for i in range(7):
	    if i != 4:
		while True:
		    col = color[random.randint(0,5)]
		    if col not in used:
			used.append(col)
			self.txt_banner[i].configure(fg=col)
			break
			
    def opndialog(self, msg, tt, ikon):
	messagebox.showinfo(tt,msg,icon=ikon)

    
    #DATABASE FUNCTIONS-------------------------------------------------------------------
    def displaydata(self, action=[]):
	db = hern.raw_database()
	if action == []:
	    for i in hern.raw_database():
		self.lstbox11.insert(0, i)
	else:
	    try:
		hern.connectdb(action[0])
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
		for i in hern.showall(action[1]):
		    asd = []
		    for j in hern.tbreq(action[1]):
			asd.append(i[j])
		    alls.append(asd)
		tuples = alls
		index = iid = 0
		for row in tuples:
		    grids.insert("", index, iid, values=row)
		    index = iid = index + 1
		datax.mainloop()
	    except:
		self.trash = ""

    def Refresh(self):
	self.Anim_banner()
	self.lstbox11.delete(0, END)
	for i in hern.raw_database():
	    self.lstbox11.insert(0, i)
    def selected(self,event):
	self.Anim_banner()
	try:
	    
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
	except:
	    self.trash=""
    #END OF DATABASE FUNTIONS-------------------------------------------------------------
    
    def opnwindow(self, Func, Type, count=0):
	self.Anim_banner()
	try:
	    
	    lst=[]
	    self.window = Tk()
	    self.window.title(Func)
	    if Type == "db":
		txto1 = Label(self.window, text= Func + " Database:")
		txto1.pack()
		inpuT1 = Entry(self.window)
		inpuT1.pack()
		if Func == "Create":
		    btn1 = Button(self.window, text="Proceed", command=lambda:self.addDB(inpuT1.get()))
		    btn1.pack(fill=X,expand=True)
		elif Func == "Delete":
		    btn1 = Button(self.window, text="Proceed", command=lambda:self.delDB(inpuT1.get()))
		    btn1.pack(fill=X,expand=True)
	    elif Type == "tb":
		if Func == "Create":
		    if count == 0:
			txto11 = Label(self.window, text="Existing Database:")
			txto11.pack()
			inpuT11 = Entry(self.window)
			inpuT11.pack()
			txto12 = Label(self.window, text= Func + " Table:")
			txto12.pack()
			inpuT12 = Entry(self.window)
			inpuT12.pack()
			txto13 = Label(self.window, text="Number of Column:")
			txto13.pack()
			inpuT13 = Entry(self.window)
			inpuT13.pack()
			btn11 = Button(self.window, text="Proceed", command=lambda:self.Create(inpuT11.get(), inpuT12.get(), inpuT13.get(), 1))
			btn11.pack(fill=X,expand=True)
		    if count == 1:
			for i in range(int(self.temp_num)):
			    lst.append(Entry(self.window))
			    lst[-1].pack()
			btn1 = Button(self.window, text="Proceed", command=lambda:self.addTB(self.temp_db, self.temp_tb, [i.get() for i in lst]))
			btn1.pack(fill=X,expand=True)
		elif Func == "Delete":
		    txto11 = Label(self.window, text="Existing Database:")
		    txto11.pack()
		    inpuT11 = Entry(self.window)
		    inpuT11.pack()
		    txto12 = Label(self.window, text= Func + " Table:")
		    txto12.pack()
		    inpuT12 = Entry(self.window)
		    inpuT12.pack()
		    btn11 = Button(self.window, text="Proceed", command=lambda:self.delTB(inpuT11.get(), inpuT12.get()))
		    btn11.pack(fill=X,expand=True)
	    elif Type == "data":
		if Func == "Create":
		    if count == 0:
			txto11 = Label(self.window, text="Database:")
			txto11.grid(row=0,column=0, columnspan=2)
			inpuT11 = Entry(self.window, width=40)
			inpuT11.grid(row=1,column=0, columnspan=2)
			txto12 = Label(self.window, text="Table:")
			txto12.grid(row=2,column=0, columnspan=2)
			inpuT12 = Entry(self.window, width=40)
			inpuT12.grid(row=3,column=0, columnspan=2)
			btn11 = Button(self.window, text="Proceed", width=38, command=lambda:self.Create(inpuT11.get(), inpuT12.get(), "", 1))
			btn11.grid(row=6,column=0, columnspan=2)
		    elif count == 1:
			hern.connectdb(self.temp_db)
			for j,i in enumerate(hern.tbreq(self.temp_tb)):
			    txt11 = Label(self.window, text=i)
			    txt11.grid(row=j,column=0)
			    lst.append(Entry(self.window))
			    lst[-1].grid(row=j,column=1)
			btn1 = Button(self.window, text="Proceed", width=38, command=lambda:self.addD(self.temp_db, self.temp_tb, [i.get() for i in lst]))
			btn1.grid(row=6,column=0, columnspan=2)
		elif Func == "Update":
		     if count == 0:
			txto11 = Label(self.window, text="Database:")
			txto11.grid(row=0,column=0, columnspan=2)
			inpuT11 = Entry(self.window, width=40)
			inpuT11.grid(row=1,column=0, columnspan=2)
			txto12 = Label(self.window, text="Table:")
			txto12.grid(row=2,column=0, columnspan=2)
			inpuT12 = Entry(self.window, width=40)
			inpuT12.grid(row=3,column=0, columnspan=2)
			txto13 = Label(self.window, text="ID:")
			txto13.grid(row=4,column=0)
			inpuT13 = Entry(self.window)
			inpuT13.grid(row=5,column=0)
			txto14 = Label(self.window, text="Value:")
			txto14.grid(row=4,column=1)
			inpuT14 = Entry(self.window)
			inpuT14.grid(row=5,column=1)
			btn11 = Button(self.window, text="Proceed", width=38, command=lambda:self.Update(inpuT11.get(), inpuT12.get(), inpuT13.get(), inpuT14.get(), 1))
			btn11.grid(row=6,column=0, columnspan=2)
		     elif count == 1:
			hern.connectdb(self.temp_db)
			for j,i in enumerate(hern.tbreq(self.temp_tb)):
			    txt11 = Label(self.window, text=i)
			    txt11.grid(row=j,column=0)
			    lst.append(Entry(self.window))
			    lst[-1].grid(row=j,column=1)
			btn1 = Button(self.window, text="Proceed", width=38, command=lambda:self.upD(self.temp_db, self.temp_tb, [i.get() for i in lst]))
			btn1.grid(row=6,column=0, columnspan=2)
		elif Func == "Delete":
		    txto11 = Label(self.window, text="Database:")
		    txto11.grid(row=0,column=0, columnspan=2)
		    inpuT11 = Entry(self.window, width=40)
		    inpuT11.grid(row=1,column=0, columnspan=2)
		    txto12 = Label(self.window, text="Table:")
		    txto12.grid(row=2,column=0, columnspan=2)
		    inpuT12 = Entry(self.window, width=40)
		    inpuT12.grid(row=3,column=0, columnspan=2)
		    txto13 = Label(self.window, text="ID:")
		    txto13.grid(row=4,column=0)
		    inpuT13 = Entry(self.window)
		    inpuT13.grid(row=5,column=0)
		    txto14 = Label(self.window, text="Value:")
		    txto14.grid(row=4,column=1)
		    inpuT14 = Entry(self.window)
		    inpuT14.grid(row=5,column=1)
		    btn11 = Button(self.window, text="Proceed", width=38, command=lambda:self.delD(inpuT11.get(), inpuT12.get(), inpuT13.get(), inpuT14.get()))
		    btn11.grid(row=6,column=0, columnspan=2)
			
	    self.window.mainloop()
	except:
	    self.extwindow()
	    self.opndialog("Error !!","Opening window","warning")
	
    def extwindow(self):
	self.window.destroy()
    
    #CREATE FUNCTION----------------------------------------------------------------------
    def Create(self, var1="",var2="", var3="", count=0):
	self.temp_db = var1
	self.temp_tb = var2
	self.temp_num = var3
	if self.vared2.get() == "Database  ":
	    self.opnwindow("Create", "db")
	elif self.vared2.get() == "Table         ":
	    if count == 0:
		self.opnwindow("Create", "tb")
	    elif count == 1:
		self.extwindow()
		self.opnwindow("Create", "tb", count)
	elif self.vared2.get() == "Insert Data":
	    if count == 0:
		self.opnwindow("Create", "data")
	    elif count == 1:
		self.extwindow()
		self.opnwindow("Create", "data", count)
	
    def addDB(self, db):
	self.Anim_banner()
	try:
	    
	    hern.createdb(db)
	    self.extwindow()
	    self.opndialog("Database name "+db+" created successfully!","Create DB","info")
	except:
	    self.opndialog("Error !!","Create DB","warning")
    
    def addTB(self, db, tb, lst=[]):
	self.Anim_banner()
	try:
	    
	    hern.connectdb(db)
	    hern.createtb(tb,lst)
	    self.extwindow()
	    self.opndialog("Table name "+tb+" on "+db+" created successfully!","Create TB","info")
	except:
	    self.opndialog("Error !!","Create TB","warning")
    
    def addD(self, db, tb, lst=[]):
	self.Anim_banner()
	try:
	    dic={}
	    for j,i in enumerate(hern.tbreq(self.temp_tb)):
		dic[i] = lst[j]
	    hern.connectdb(db)
	    hern.insertdata(tb, dic)
	    self.extwindow()
	    self.opndialog("A new data on "+tb+" table inserted successfully!","Insert Data","info")
	except:
	    self.opndialog("Error !!","Insert data","warning")
	    
    #END OF CREATE FUNTIONS-------------------------------------------------------------
    
    #UPDATE FUNCTION--------------------------------------------------------------------
    def Update(self, var1="",var2="", var3="", var4="", count=0):
	self.temp_db = var1
	self.temp_tb = var2
	self.temp_id = var3
	self.temp_val = var4
	if self.vared3.get() == "Update Data":
	    if count == 0:
		self.opnwindow("Update", "data")
	    elif count == 1:
		self.extwindow()
		self.opnwindow("Update", "data", count)
	
    def upD(self, db, tb, lst=[]):
	self.Anim_banner()
	try:
	    dic1={}
	    dic2={}
	    for j,i in enumerate(hern.tbreq(self.temp_tb)):
		if lst[j] != "":
		    dic2[i] = lst[j]
	    hern.connectdb(db)
	    dic1[self.temp_id] = self.temp_val
	    hern.updatedata(tb,dic1, dic2)
	    self.extwindow()
	    self.opndialog("A data on "+tb+" table updated successfully!","Update Data","info")
	except:
	    self.opndialog("Error !!","Update data","warning")
	    
    #END OF UPDATE FUNTIONS-------------------------------------------------------------
    
    #DELETE FUNCTION--------------------------------------------------------------------
    def Delete(self, var1="",var2="", count=0):
	try:
	    self.temp_db = var1
	    self.temp_tb = var2
	    if self.vared4.get() == "Database  ":
		self.opnwindow("Delete", "db")
	    elif self.vared4.get() == "Table         ":
		self.opnwindow("Delete", "tb")
	    elif self.vared4.get() == "Delete Data":
		self.opnwindow("Delete", "data")
	except:
	    self.opndialog("Error !!","Delete","warning")
    
    def delDB(self, db):
	self.Anim_banner()
	try:
	    prior = ""
	    for i in hern.rawdb(db):
		for j in hern.rawtb(db,i):
		    hern.os.remove("Database/%s/%s/%s"%(db,i,j))
		hern.os.removedirs("Database/%s/%s"%(db,i))
		hern.os.remove("res/config/cache/%s/%s"%(db,i))
	    hern.os.removedirs("res/config/cache/%s"%db)
	    if hern.checkdb(db):
		hern.os.removedirs("Database/%s"%db)
	    if not hern.os.path.exists("Database"):
		hern.os.makedirs("Database")
	    prior = hern.getprio()
	    if prior == db:
		hern.prio("")
	    self.extwindow()
	    self.opndialog("Database name "+db+" deleted successfully!","Delete DB","info")
	except:
	    self.extwindow()
	    self.opndialog("Error !!","Delete DB","warning")
    
    def delTB(self, db, tb):
	self.Anim_banner()
	try:
	    for i in hern.rawtb(db,tb):
		hern.os.remove("Database/%s/%s/%s"%(db,tb,i))
	    hern.os.removedirs("Database/%s/%s"%(db,tb))
	    hern.os.remove("res/config/cache/%s/%s"%(db,tb))
	    if not hern.checkdb(db):
		hern.os.makedirs("Database/%s"%db)
	    self.extwindow()
	    self.opndialog("Table name "+tb+" on "+db+" deleted successfully!","Delete TB","info")
	except:
	    self.extwindow()
	    self.opndialog("Error !!","Delete TB","warning")
    
    def delD(self, db, tb, Id, Val):
	self.Anim_banner()
	try:
	    
	    if hern.checkdb(db) and hern.checktb(db,tb) and Id in hern.tbreq(tb):
		dic={}
		dic[Id] = Val
		hern.connectdb(db)
		hern.deletedata(tb, dic)
		self.extwindow()
		self.opndialog("A data on "+tb+" table deleted successfully!","Delete Data","info")
	    else:
		db="Asd"
		db += 2
	except:
	    self.extwindow()
	    self.opndialog("Error !!","Delete data","warning")
    #END OF DELETE FUNTIONS-------------------------------------------------------------
    
    
    
    
    #HELP FUNCTION----------------------------------------------------------------------
    
    
    #END OF HELP FUNCTIONS--------------------------------------------------------------


app = UI()
app.title("Hern DB")
app.geometry("400x500")
app.resizable(0,0)
app.mainloop()
