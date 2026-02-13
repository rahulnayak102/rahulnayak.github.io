import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student managent system")

title_label = tk.Label(win,text="studnt management system", font = ("Arial", 30, "bold"), border=12, relief=tk.GROOVE, bg="lightgray")
title_label.pack(side= tk.TOP, fill=tk.X)

detail_Frame = tk.LabelFrame(win, text = "enter details ", font = ("Arial",20),bd=12,relief = tk.GROOVE, bg = "lightgray")
detail_Frame.place(x=20, y= 90, width = 420, height = 575)

data_Frame = tk.Frame(win, bd=12, bg="lightgray", relief=tk.GROOVE)
data_Frame.place(x=475, y=90, width=800,height=575)

rollno = tk.StringVar()
name_var = tk.StringVar()
class_var = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
fathersnm = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

search_by = tk.StringVar()

#
rollno_lbl = tk.Label(detail_Frame, text="Roll No", font=("Arial",15), bg="lightgray")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_Frame, text="Name", font=("Arial",15), bg="lightgray")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=name_var)
name_ent.grid(row=1, column=1, padx=2, pady=2)

class_lbl = tk.Label(detail_Frame, text="Class", font=("Arial",15), bg="lightgray")
class_lbl.grid(row=2, column=0, padx=2, pady=2)

class_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=name_var)
class_ent.grid(row=2, column=1, padx=2, pady=2)

selection_lbl = tk.Label(detail_Frame, text="Selection", font=("Arial",15), bg="lightgray")
selection_lbl.grid(row=3, column=0, padx=2, pady=2)

selection_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=section)
selection_ent.grid(row=3, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_Frame, text="Contact", font=("Arial",17), bg="lightgray")
contact_lbl.grid(row=4, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=contact)
contact_ent.grid(row=4, column=1, padx=2, pady=2)

fathersnm_lbl = tk.Label(detail_Frame, text="Father's Name", font=("Arial",15), bg="lightgray")
fathersnm_lbl.grid(row=5, column=0, padx=2, pady=2)

fathersnm_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=fathersnm)
fathersnm_ent.grid(row=5, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_Frame, text="address", font=("Arial",15), bg="lightgray")
address_lbl.grid(row=6, column=0, padx=2, pady=2)

address_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=address)
address_ent.grid(row=6, column=1, padx=2, pady=2)

#
gender_lbl = tk.Label(detail_Frame, text="Gender", font=("Arial",15), bg="lightgray")
gender_lbl.grid(row=7, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_Frame,font=("Arial",15),state="readonly",textvariable=gender)
gender_ent['values'] = ("Male", "Female", "Other")
gender_ent.grid(row=7, column=1, padx=2, pady=2)

dob_lbl = tk.Label(detail_Frame, text="D.O.B", font=("Arial",15), bg="lightgray")
dob_lbl.grid(row=8, column=0, padx=2, pady=2)

dob_ent = tk.Entry(detail_Frame, bd=7, font=("Arial",15),textvariable=dob)
dob_ent.grid(row=8, column=1, padx=2, pady=2)



btn_frame = tk.Frame(detail_Frame, bg="lightgray",bd=10,relief=tk.GROOVE)
btn_frame.place(x=18,y=390,width=340,height=120)

add_btn = tk.Button(btn_frame,bg="lightgray",text="Add",bd=7,font=("Arial",13),width=15)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="lightgray",text="Upadate",bd=7,font=("Arial",13),width=15)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgray",text="Delete",bd=7,font=("Arial",13),width=15)
delete_btn.grid(row=1,column =0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="lightgray",text="Clear",bd=7,font=("Arial",13),width=15)
clear_btn.grid(row=1,column=1,padx=3,pady=2)


search_frame = tk.Frame(data_Frame,bg="lightgray",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_frame,text="search",bg="lightgray",font=("Arial",14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in=ttk.Combobox(search_frame,font=("Arial",14),state="readonly",textvariable=search_by)
search_in['values'] = ("Name","Roll No","Contact", "Father's Name","Class","Section","D.O.B")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn=tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=14,bg="lightgray")
search_btn.grid(row=0,column=2,padx=12,pady=2)

showall_btn=tk.Button(search_frame,text="Showall",font=("Arial",13),bd=9,width=14,bg="lightgray")
showall_btn.grid(row=0,column=3,padx=12,pady=2)


main_frame = tk.Frame(data_Frame,bg="lightgray",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame,
                             columns=("Roll no.","Name","Class","Section","Contact","Father's name","Gender","D.O.B","Address"),
                             yscrollcommand=y_scroll.set,
                             xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)


student_table.heading("Roll no.",text="Roll no.")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="class")
student_table.heading("Section",text="Section")
student_table.heading("Contact",text="Contact")
student_table.heading("Father's name",text="Father's name")
student_table.heading("Gender",text="Gender")
student_table.heading("D.O.B",text="D.O.B")
student_table.heading("Address",text="Address")

student_table['show']= 'headings'

student_table.column("Roll no.",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("Contact",width=100)
student_table.column("Father's name",width=100)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)
student_table.column("Address",width=150)



student_table.pack(fill = tk.BOTH,expand=True)



win.mainloop()