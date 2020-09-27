from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
        def __init__(self,root):
            self.root=root
            self.root.title("Student management System")
            self.root.geometry("1350x700+0+0")
            
            title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Times New Roman",40,"bold"),bg="Green",fg="yellow")
            title.pack(side=TOP,fill=X)

            #======= All Variable==============
            self.Roll_No_var=StringVar()
            self.Name_var=StringVar()
            self.Gender_var=StringVar()
            self.Contact_var=StringVar()
            self.DOB_var=StringVar()
            self.Address_var=StringVar()
            self.Email_var=StringVar()
            self.Search_by=StringVar()
            self.Search_txt=StringVar()

#==============Manage Frame=================
            Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cyan")
            Manage_Frame.place(x=20,y=100,width=450,height=600)

            m_title=Label(Manage_Frame,text="Manage Students",bg="cyan",fg="Black",font=("times new roman",30 ,"bold"))
            m_title.grid(row=0,columnspan=2,pady=20)

            lbl_roll=Label(Manage_Frame,text="Roll No",bg="cyan",fg="Black",font=("times new roman",15 ,"bold"))
            lbl_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

            txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")

            lbl_name=Label(Manage_Frame,text="Name",bg="cyan",fg="Black",font=("times new roman",15 ,"bold"))
            lbl_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")

            txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_name.grid(row=2,column=1,pady=10,padx=10,sticky="w")

            lbl_Gender=Label(Manage_Frame,text="Gender",bg="cyan",fg="Black",font=("times new roman",15,"bold"))
            lbl_Gender.grid(row=3,column=0,pady=10,padx=10,sticky="w")

            combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",13,"bold"))
            combo_gender['values']=("Male","Female","Other ") 
            combo_gender.grid(row=3,column=1,padx=10,pady=10)
            
            lbl_Contact=Label(Manage_Frame,text="Contact",bg="cyan",fg="Black",font=("times new roman",15 ,"bold"))
            lbl_Contact.grid(row=4,column=0,pady=10,padx=10,sticky="w")

            txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Contact.grid(row=4,column=1,pady=10,padx=10,sticky="w")
            
            lbl_DOB=Label(Manage_Frame,text="DOB",bg="cyan",fg="Black",font=("times new roman",15,"bold"))
            lbl_DOB.grid(row=5,column=0,pady=10,padx=10,sticky="w")

            txt_DOB=Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_DOB.grid(row=5,column=1,pady=10,padx=10,sticky="w")

            lbl_Email=Label(Manage_Frame,text="Email",bg="cyan",fg="Black",font=("times new roman",15,"bold"))
            lbl_Email.grid(row=6,column=0,pady=10,padx=10,sticky="w")

            txt_Email=Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Email.grid(row=6,column=1,pady=10,padx=10,sticky="w")

            lbl_Address=Label(Manage_Frame,text="Address",bg="cyan",fg="Black",font=("times new roman",15,"bold"))
            lbl_Address.grid(row=7,column=0,pady=10,padx=10,sticky="w")

            self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
            self.txt_Address.grid(row=7,column=1,pady=10,padx=10,sticky="w")

#==============Button Frame============== 
            btn_Frame=Frame(Manage_Frame,bg="cyan")
            btn_Frame.place(x=15,y=530,width=420)

            Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
            Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
            Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
            Clearbtn=Button(btn_Frame,text="Clear ",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

            
#==============Manage Frame=================
 
            Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cyan")
            Detail_Frame.place(x=500,y=100,width=1000,height=600)

            lbl_Search=Label(Detail_Frame,text="Search_By",width=10,bg="cyan",fg="Black",font=("times new roman",20,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=10,sticky="w")

            combo_search=ttk.Combobox(Detail_Frame,textvariable=self.Search_by,font=("times new roman",13,"bold"),state='readonly')
            combo_search['values']=("Roll_No","Name","Contact") 
            combo_search.grid(row=0,column=1,padx=10,pady=10)
            
            txt_Search=Entry(Detail_Frame,textvariable=self.Search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=10,sticky="w")

            searchbtn=Button(Detail_Frame,text="Search",command=self.Search_data ,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
            showallbtn=Button(Detail_Frame,text="Showall",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
#==========Table Frame===============

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="cyan")
            Table_Frame.place(x=10,y=70,width=900,height=500)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
            self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll No","Name","Gender","Contact","DOB","Email","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Student_table.xview)
            scroll_y.config(command=self.Student_table.yview)
            self.Student_table.heading("Roll No",text="Roll No")
            self.Student_table.heading("Name",text="Name")
            self.Student_table.heading("Gender",text="Gender")
            self.Student_table.heading("Contact",text="Contact")
            self.Student_table.heading("DOB",text="D.O.B") 
            self.Student_table.heading("Email",text="Email")
            self.Student_table.heading("Address",text="Address")
            self.Student_table['show']='headings'
            self.Student_table.column("Roll No",width=120)
            self.Student_table.column("Name",width=120)
            self.Student_table.column("Gender",width=120)
            self.Student_table.column("Contact",width=120)
            self.Student_table.column("DOB",width=120)
            self.Student_table.column("Email",width=120)
            self.Student_table.column("Address",width=200)

            self.Student_table.pack(fill=BOTH,expand=1)
            self.Student_table.bind("<ButtonRelease>",self.get_cursor)
            self.fetch_data()
        def add_students(self):
            if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.Email_var.get()=="":

                    messagebox.showerror("Error","All fields are required")
            else:        
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
           
                con.cursor().execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.Name_var.get(),
                                                                            self.Gender_var.get(),
                                                                            self.Contact_var.get(),
                                                                            self.DOB_var.get(),
                                                                            self.Email_var.get(),
                                                                            self.txt_Address.get('1.0',END),
                                                                             ))

            con.commit()
            self.fetch_data()
            self.clear() 
            con.close()        
            messagebox.showinfo("Success","Recoed has been Inserted")
        def fetch_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
            cur=con.cursor()
            cur.execute("select * from Students")
            rows=cur.fetchall()
            if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                            self.Student_table.insert('',END,values=row)
                    con.commit()
            con.close()      
        def clear(self):
            self.Roll_No_var.set("")   
            self.Name_var.set("")
            self.Gender_var.set("")
            self.Contact_var.set("")
            self.DOB_var.set("")
            self.Email_var.set("")
            self.txt_Address.delete("1.0",END)                                               

        def get_cursor(self,ev):
            cursor_row=self.Student_table.focus()
            contents=self.Student_table.item(cursor_row)
            row=contents['values']
            self.Roll_No_var.set(row[0])   
            self.Name_var.set(row[1])
            self.Gender_var.set(row[2])
            self.Contact_var.set(row[3])
            self.DOB_var.set(row[4])
            self.Email_var.set(row[5])
            self.txt_Address.delete("1.0",END)
            self.txt_Address.insert(END,row[6]) 

        def update_data(self):    
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
           
            con.cursor().execute("update students set Name=%s,Gender=%s,Contact=%s,DOB=%s,Email=%s,Address=%s where Roll_no=%s",(
                                                                            self.Name_var.get(),
                                                                            self.Gender_var.get(),
                                                                            self.Contact_var.get(),
                                                                            self.DOB_var.get(),
                                                                            self.Email_var.get(),
                                                                            self.txt_Address.get('1.0',END),
                                                                            self.Roll_No_var.get()
                                                                             ))

            con.commit()
            self.fetch_data()
            self.clear() 
            con.close()     
            
        def delete_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
            cur=con.cursor()
            cur.execute("delete from Students where Roll_No=%s",self.Roll_No_var.get())
            con.commit()
            con.close()      
            self.fetch_data()
            self.clear() 

        def Search_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
            cur=con.cursor()
            cur.execute("select * from Students where "+str(self.Search_by.get())+" LIKE '%"+str(self.Search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                            self.Student_table.insert('',END,values=row)
                    con.commit()
            con.close()          
           
root=Tk() 
ob=Student(root)
root.mainloop() 