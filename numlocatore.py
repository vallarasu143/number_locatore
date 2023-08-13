##NUMBER LOCATORE
##created by arasu
## module phonenumbers and pytz use in GUI (graphical user interface) with tkinter module


from tkinter import*
root=Tk()
root.resizable(0,0)
root.geometry("500x410")
root.title("NUMBER LOCATORE")

code=StringVar()  #assign entry_1 textvariable

num=StringVar()     #assign entry_2 textvariable

code2=StringVar() #assign entry_3

num2=StringVar() #assign entry_4

code3=StringVar()

num3=StringVar()

code4=StringVar()

code5=StringVar()

class main():
    def country(self):
        import phonenumbers   #install phonenumbers moudule
        a=str(code.get())      #get entry_1 value
        b=str(num.get())        #get entry_2 value
        self.c=(a+b)           #add country code and number =+91 + 8954423407
        from phonenumbers import geocoder
        ch=phonenumbers.parse(self.c,"CH")
        self.k=(geocoder.description_for_number(ch,"en"))
    
        

    def service(self):   #get network function  
        main.country(self)  ##called method inside cuntry(self)
        import phonenumbers
        from phonenumbers import carrier  
        ser=phonenumbers.parse(self.c,"RO")
        e=(carrier.name_for_number(ser,"en"))
        
        code2.set(self.k)  
        num2.set(e)

    def timezone(self):     #get timezone function
        main.service(self)
        
        import phonenumbers
        from phonenumbers import timezone
        time=phonenumbers.parse(self.c)
        self.zone=(timezone.time_zones_for_number(time))
        
        code3.set(self.zone)
        

    def number_valid(self): ##number vaild function
        main.timezone(self)
        import phonenumbers
        valid=phonenumbers.parse(self.c)
        nv=(phonenumbers.is_valid_number(valid))
        
        num3.set(nv)
    def number_possible(self):  ##number possible function
        main.number_valid(self)
        import phonenumbers
        possible=phonenumbers.parse(self.c)
        np=(phonenumbers.is_possible_number(possible))
        code4.set(np)

    def current_time(self):         ### convert timezone to correct time function
        main.number_possible(self)
        from datetime import datetime
        from pytz import timezone     ## want timezone convert correct time use "pytz" module and import timezone
        fmt="%Y-%m-%d %H:%M:%S %Z%z"
        time_zone=self.zone
        for x in time_zone:
            now_time=datetime.now(timezone(x))
            code5.set(now_time)
        
        
        
        
        
obj=main()



label_1=Label(root,text="Enter code:")
label_1.grid(row=0,column=0)
ent=Entry(root,width=30,textvariable=code).grid(row=0,column=1)

label_2=Label(root,text="Enter number:")
label_2.grid(row=1,column=0)
mdt=Entry(root,width=30,textvariable=num).grid(row=1,column=1)

label_3=Label(root,text="The country is:").grid(row=4,column=0)
label_4=Label(root,text="The Network is:").grid(row=5,column=0)
e1=Entry(root,width=30,textvariable=code2).grid(row=4,column=1)
e2=Entry(root,width=30,textvariable=num2).grid(row=5,column=1)

label_5=Label(root,text="Time zone:").grid(row=6,column=0)
label_6=Label(root,text="Number valid:").grid(row=7,column=0)
label_7=Label(root,text="Number possible:").grid(row=8,column=0)
label_8=Label(root,text="Current datetime:").grid(row=9,column=0)


e3=Entry(root,width=30,textvariable=code3).grid(row=6,column=1)
e4=Entry(root,width=30,textvariable=num3).grid(row=7,column=1)
e5=Entry(root,width=30,textvariable=code4).grid(row=8,column=1)
e6=Entry(root,width=30,textvariable=code5).grid(row=9,column=1)





frame=Frame(root,width=125,height=50,highlightbackground="black",
            highlightthickness=2,).grid(row=2,column=0)

enter_button=Button(frame,text="ENTER",width=10,command=lambda:obj.current_time()).grid(row=2,column=0,padx=0)
root.mainloop()
