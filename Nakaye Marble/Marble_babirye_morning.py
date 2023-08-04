# Create a receipt praogram with GUI interface,
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os ,sys
import tempfile

class Store:
    def __init__(self , window):
        self.win = window
        
        self.categories=["Apples","Grapes","Mangoes","Pears"]
        
        self.Apples=["Apples1","Apples2","Apples3","Apples4"]
        self.Grapes=["Grapes1","Grapes2","Grapes3","Grapes4"]
        self.Mangoes=["Mangoes1","Mangoes2","Mangoes3","Mangoes4"]
        self.Pears=["Pears1","Pears2","Pears3","Pears4"]
        
        self.cname=StringVar()
        self.cmob =StringVar()
        self.cbill =StringVar()
        
        self.price =IntVar()
        self.qty =IntVar()
        
        self.tlist =[]
        
        
        
        self.win.geometry("1550x800+0+0")
        space =""
        self.win.title(space*200+"PC Store")
        heading = Label(self.win,text ="Welcome to Marble Store",background="blue",fg="white",font=("Goudy Stout",15))
        heading.pack(fill=X, ipady=10)
        
        main_frame = Frame(self.win,background ="white")
        main_frame.pack(fill="both",expand=1)
        
        customer_frame =LabelFrame(main_frame, pady=10,height=100,background="white",text="Customer Details",font=("Elephant",15))
        customer_frame.place(x=0,y=0,width=1550)
        
        form_frame =LabelFrame(main_frame,height=500, pady =100 ,padx=60 ,width=550 ,background="pink",text=" Product Details",font=("Elephant",15))
        form_frame.place(x=0,y=100) 
        
        table_frame =LabelFrame(main_frame,height=500, width=500 ,background="white",text="Bill Details",font=("Elephant",15))
        table_frame.place(x= 550,y=100) 
        
        button_frame =LabelFrame(main_frame,height=100, width=1550 ,background="orange",text=" Click Here",font=("Elephant",15))
        button_frame.place(x=0,y=500)
         
        # Customer details
        Customer_Name_1b1 =Label(customer_frame,text="Enter Customer Name",font=("times new roman",15))
        Customer_Name_1b1.place(x=10, y=0,width=200)
        Customer_Name_txt =Entry(customer_frame,font =("times new roman",15),textvariable= self.cname)
        Customer_Name_txt.place(x=250,y=0)
        
        Customer_Mob_1b1 =Label(customer_frame,text="Enter Mob Number",font=("times new roman",15))
        Customer_Mob_1b1.place(x=500, y=0,width=200)
        Customer_Mob_txt =Entry(customer_frame,font =("times new roman",15),textvariable=self.cmob)
        Customer_Mob_txt.place(x=750,y=0)
        
        Customer_Billno_1b1 =Label(customer_frame,text="Enter Billno",font=("times new roman",15))
        Customer_Billno_1b1.place(x=1000, y=0,width=200)
        Customer_Billno_txt =Entry(customer_frame,font =("times new roman",15),textvariable=self.cbill)
        Customer_Billno_txt.place(x=1250,y=0)
        
        # Product Details
        Product_Cat =Label(form_frame,text="Category",font=("times new roman",15))
        Product_Cat.place(x=20,y=0,width =120)
        self.categories.insert(0,"Select Category")
        self.Product_Cat_List =ttk.Combobox(form_frame,font=("times new roman",15),values =self.categories)
        self.Product_Cat_List.current(0)
        self.Product_Cat_List.place(x=170,y=0,width=200)
        
        self.Product_Cat_List.bind('<<ComboboxSelected>>',self.cat)
        
        Product_Sub=Label(form_frame,text=" Sub Category",font=("times new roman",15))
        Product_Sub.place(x=20,y=50,width =120)
        self.Product_Sub_List =ttk.Combobox(form_frame,font=("times new roman",15))
        self.Product_Sub_List.place(x=170,y=50,width=200)
        
        Product_Rate_1b1=Label(form_frame,text="Rate",font=("times new roman",15))
        Product_Rate_1b1.place(x=20,y=100,width =120)
        Product_Rate_txt =Entry(form_frame, text="Rate" ,font=("times new roman",15),textvariable=self.price)
        Product_Rate_txt.place(x=170,y=100,width=200)
        
        Product_Qty_1b1=Label(form_frame,text="Quantity",font=("times new roman",15))
        Product_Qty_1b1.place(x=20,y=150,width =120)
        Product_Qty_txt =Entry(form_frame, text="Rate" ,font=("times new roman",15),textvariable=self.qty)
        Product_Qty_txt.place(x=170,y=150,width=200)
        
        # Billing Area
        scrolly=Scrollbar(table_frame,orient=VERTICAL)
        self.billarea =Text(table_frame,yscrollcommand= scrolly.set,font=("times new roman,",15),fg="blue")
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.billarea.yview)
        self.billarea.pack(fill=BOTH,expand=1)
        
        self.Add_Item_Btn=Button(button_frame,text="Add Item",font=("times new roman",15), command=self.addItem)
        self.Add_Item_Btn.place(x=50,y=0,width=200)

        self.Calc_Item_Btn=Button(button_frame,text="Calculate bill",font=("times new roman",15), command= self.makereceipt)
        self.Calc_Item_Btn.place(x=300,y=0,width=200)
        
        self.Save_Bill_Btn=Button(button_frame,text="Save Bill",font=("times new roman",15),command=self.save_bill)
        self.Save_Bill_Btn.place(x=550,y=0,width=200)
        
        self.Print_Btn=Button(button_frame,text="Print",font=("times new roman",15),command= self.print_bill)
        self.Print_Btn.place(x=800,y=0,width=200)
        
        
        self.heading()
        
        
        
    def cat(self,e=''):
        if self.Product_Cat_List.get()=="Apples":
            self.Product_Sub_List.config(values=self.Apples)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Grapes":
            self.Product_Sub_List.config(values=self.Grapes)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Mangoes":
            self.Product_Sub_List.config(values=self.Mangoes)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Pears":
            self.Product_Sub_List.config(values=self.Pears) 
            self.Product_Sub_List.current(0)
            
                   
    def addItem(self):
        if self.Product_Cat_List.get()=="Select Category":
            messagebox.showinfo("info","please select categories")       
        elif self.price.get()==0:
            messagebox.showinfo("info","please enter price") 
        elif self.qty.get()==0:
            messagebox.showinfo("info","please enter quantity")                 
        else:
            r=self.price.get()
            q=self.qty.get() 
            t=r*q
            self.tlist.append(t)
            print(self.tlist)
            self.billarea.insert(END, f'\n {self.Product_Sub_List.get()}\t \t{r} \t{q} \t {t}')     
     
    def makereceipt(self):
        if len(self.cname.get())==0 and len(self.c.mob.get())==0 and len(self.cbill.get())==0:
            messagebox.showinfo("info","please enter customer detail")  
        elif self.Product_Cat_List.get()=="Select Category":
            messagebox.showinfo("info","please select categories")
        elif self.price.get()==0:
            messagebox.showinfo("info","please enter prices") 
        elif self.qty.get()==0:
            messagebox.showinfo("info","please enter quantity")                            
        else:
            space=""
            total =sum(self.tlist)
            self.billarea.insert(3.16,self.cname.get())
            self.billarea.insert(4.20,self.cmob.get())
            self.billarea.insert(5.20,self.cbill.get())
            self.billarea.insert(END,"\n +++++++++++++++++++++++++++++++++")
            self.billarea.insert(END,f'\n Total={space*50}  {total}')     
            self.billarea.insert(END,f'\n CGST={space*50}  {total*0.025}')
            self.billarea.insert(END,f'\n SGST={space*50}  {total*0.025}')     
            self.billarea.insert(END,f'\n Bill={space*50}  {total+{total*0.05}}')     
            
    def save_bill(self):
        opt=messagebox.askyesno("Bill", "Do you want to save")  
        if opt== True:
            self.bill_data=self.billarea.get(1.0,END)
            fh=open("bill/"+self.cbill.get()+".txt",'w')
            fh.write(self.bill_data)
            fh.close()
    def print_bill(self):
        q =self.billarea.get(1.0,'end-1c')        
        filename =tempfile.mktemp('.txt')   
        open(filename,'w').write(q) 
        os.startfile(filename,"print")     
                      
    def heading(self): 
        self.billarea.delete(1.0,END) 
        self.billarea.insert(END,"\t\t\t\tMarble Store")
        self.billarea.insert(END,"\n\t-----------------------")  
        self.billarea.insert(END,f'\n Customer Name\t')
        self.billarea.insert(END,f'\n Mobile No\t')  
        self.billarea.insert(END,f'\n Bill No \t')
        self.billarea.insert(END,f'\n Product name \t Price \t Quantity \t\t Total')
        
        
        
        
if __name__ == '__main__':
    win =Tk()
    app = Store(win)
    win.mainloop()
    