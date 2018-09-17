import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox
import pyodbc
import pandastable as ps
from tkinter import Text
import time
import os
import shutil



win=tk.Tk()

win.title("Data Validation Tool")

tabcontrol=ttk.Notebook(win)

tab1=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="DB CONNECTION")
tabcontrol.pack(expand=0,fill="both")

tab2=ttk.Frame(tabcontrol)
tabcontrol.add(tab2,text="COUNT & DATA")
tabcontrol.pack(expand=0,fill="both")

tab3=ttk.Frame(tabcontrol)
tabcontrol.add(tab3,text="SOURCELOG")
tabcontrol.pack(expand=0,fill="both")

tab4=ttk.Frame(tabcontrol)
tabcontrol.add(tab4,text="TESTING")
tabcontrol.pack(expand=0,fill="both")



# OnClick function to establish connection

def OnClick():
    s_details=a_textbox.get()
    connection=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};server='+a_textbox.get()+';database='+b_textbox.get()+';uid='+c_textbox.get()+';pwd='+d_textbox.get())
    button_connect.configure(text=" Connected to "+a_textbox.get())
    


def OnClear():
    a_textbox.delete(0,'end')
    b_textbox.delete(0,'end')
    e_textbox.delete(0,'end')
    c_textbox.delete(0,'end')
    d_textbox.delete(0,'end')
    button_connect.configure(text="Connect")
    

# adding db connecting details in tab1=DB CONNECTION

labelframe=ttk.LabelFrame(tab1,text="Database details")
labelframe.grid(column=0,row=7,sticky=tk.W)

# server label and text box
a_label=ttk.Label(labelframe,text="SERVER")
a_label.grid(column=0,row=1,sticky=tk.W)

Server_val=tk.StringVar()
a_textbox=ttk.Entry(labelframe,width=20,text=Server_val)
a_textbox.grid(column=1,row=1,sticky=tk.W)
a_textbox.focus()

# Package label and text box
b_label=ttk.Label(labelframe,text="Package_Name")
b_label.grid(column=0,row=2,sticky=tk.W)
DataBase_Val=tk.StringVar()
b_textbox=ttk.Entry(labelframe,width=20)
b_textbox.grid(column=1,row=2,sticky=tk.W)

# DataBase label and text box

e_label=ttk.Label(labelframe,text="DATASOURCE ID")
e_label.grid(column=0,row=3,sticky=tk.W)

database_val=tk.IntVar()
e_textbox=ttk.Entry(labelframe,width=20,text=database_val)
e_textbox.grid(column=1,row=3,sticky=tk.W)

# userid label and text box
c_label=ttk.Label(labelframe,text="UserID")
c_label.grid(column=0,row=4,sticky=tk.W)
UserID_val=tk.StringVar()
c_textbox=ttk.Entry(labelframe,width=20,text=UserID_val)
c_textbox.grid(column=1,row=4,sticky=tk.W)

#password label and textbox
d_label=ttk.Label(labelframe,text="Password")
d_label.grid(column=0,row=5,sticky=tk.W)
password_val=tk.StringVar()
d_textbox=ttk.Entry(labelframe,width=20,text=password_val)
d_textbox.grid(column=1,row=5,sticky=tk.W)


# button to establish connection

button_connect=ttk.Button(tab1,text="Connect",command=OnClick)
button_connect.grid(column=0,row=8)

# button to clear the contents

button_label=ttk.Label(tab1,text="Reset the Text Fields")
button_label.grid(column=1,row=16)

button_clear=ttk.Button(tab1,text="Clear",command=OnClear)
button_clear.grid(column=1,row=17,sticky=tk.S)

def msgbox():
    mBox.showinfo("ABOUT SOFTWARE","Author : Pruthvi Sankar\n Year : 2018")

about_button=ttk.Button(tab1,text="ABOUT",command=msgbox)
about_button.grid(column=10,row=0,sticky=tk.E)

# DETAILS FOR TAB4


def OnClick1():
    path_dest=r'D:\Testing Documents'
    fold=path_dest +"\\" + CR_textbox.get()
    new_fold=fold
    os.mkdir(new_fold)
    folder_path=os.path.abspath(new_fold)
    path_var.set(folder_path)
    if ((value_TC.get()==1) and (value_TP.get()==1) and (value_TS.get()==1)):
        path_src="D:\\Testing Documents\\General Testing Documents\\CIS_MCA_Test_Case.xlsx"
        shutil.copy(path_src,new_fold)
        path_src_1="D:\\Testing Documents\\General Testing Documents\\CIS_MCA_Test_Plan.docx"
        shutil.copy(path_src_1,new_fold)
        path_src_2="D:\\Testing Documents\\General Testing Documents\\CIS_MCA_Test_Summary_Report.xlsx"
        shutil.copy(path_src_2,new_fold)
    elif((value_TC.get()==1) and (value_TP.get()==0) and (value_TS.get()==0)):
         path_src="D:\\Testing Documents\\General Testing Documents\\CIS_MCA_Test_Case.xlsx"
         shutil.copy(path_src,new_fold)
    elif((value_TC.get()==0) and (value_TP.get()==1)and (value_TS.get()==0)):
         path_src_1="D:\\Testing Documents\\General Testing Documents\\CIS_MCA_Test_Plan.docx"
         shutil.copy(path_src_1,new_fold)
    elif((value_TC.get()==0) and (value_TP.get()==0)):
        mBox.showinfo(title="Testing Artifacts",message="None of the documents to be created are selected")     
        


def OnClick4():
    CR_textbox.delete(0,'end')
    path_var.set(" ")
    #TC_CHK.deselect()
    #TP_CHK.deselect()
    #TSR_CHK.deselect()


def OnClick3():
    new_fold=path_textbox.get()+"\\"
    fold_path_1=os.chdir(new_fold)
    fold_path=os.listdir(fold_path_1)
    k=CR_textbox.get()+'_Test_Plan.docx'
    l=CR_textbox.get()+'_Test_Summary_Report.xlsx'
    m=CR_textbox.get()+'_Test_Case.xlsx'
    for file in os.listdir(new_fold):
        mBox.showinfo(title="Folder",message="{}".format(file))
        if "Plan" in file:
            os.rename(file,k)
        elif "Summary" in file:
            os.rename(file,l)
        elif "Case" in file:
            os.rename(file,m)

tab4_labelframe=tk.LabelFrame(tab4,text="Testing Artifacts")
tab4_labelframe.grid(column=0,row=10,sticky=tk.W)

tab4_CRlabel=tk.Label(tab4_labelframe,text="CR NAME")
tab4_CRlabel.grid(column=0,row=0,sticky=tk.W)

value_CR=tk.StringVar()
CR_textbox=ttk.Entry(tab4_labelframe,width=30,text=value_CR)
CR_textbox.grid(column=1,row=0,sticky=tk.W)

tab4_path=ttk.Label(tab4_labelframe,text="PATH")
tab4_path.grid(column=0,row=1,sticky=tk.W)

path_var=tk.StringVar()
path_textbox=ttk.Entry(tab4_labelframe,width=30,text=path_var,state='disabled')
path_textbox.grid(column=1,row=1,sticky=tk.W)


tab4_label=ttk.Label(tab4_labelframe,text="GENERATE TEST SCRIPTS")
tab4_label.grid(column=0,row=4)


value_TC=tk.BooleanVar()
TC_CHK=tk.Checkbutton(tab4_labelframe,text="TEST CASE",variable=value_TC,state='disabled')
TC_CHK.select()
TC_CHK.grid(column=0,row=5,sticky=tk.W)

value_TP=tk.BooleanVar()
TP_CHK=tk.Checkbutton(tab4_labelframe,text="TEST PLAN",variable=value_TP,state='disabled')
TP_CHK.select()
TP_CHK.grid(column=0,row=6,sticky=tk.W)

value_TS=tk.BooleanVar()
TSR_CHK=tk.Checkbutton(tab4_labelframe,text="TEST Summary Report",variable=value_TS,state='disabled')
TSR_CHK.select()
TSR_CHK.grid(column=0,row=7,sticky=tk.W)

Create_label=ttk.Label(tab4_labelframe,text="Click to Generate the  Test Documents")
Create_label.grid(column=0,row=8,sticky=tk.W)

Gen_Butn=ttk.Button(tab4_labelframe,text="Click",command=OnClick1)
Gen_Butn.grid(column=1,row=8,sticky=tk.W)

Change_label=ttk.Label(tab4_labelframe,text="Click to rename the files")
Change_label.grid(column=0,row=9,sticky=tk.W)

Gen_Butn_1=ttk.Button(tab4_labelframe,text="Click",command=OnClick3)
Gen_Butn_1.grid(column=1,row=9,sticky=tk.W)

Reset_Label_tab4=ttk.Label(tab4_labelframe,text="Reset the Text Fields")
Reset_Label_tab4.grid(column=0,row=11,sticky=tk.W)

Reset_Button_tab4=ttk.Button(tab4_labelframe,text="Clear",command=OnClick4)
Reset_Button_tab4.grid(column=1,row=11,sticky=tk.W)

# DETAILS FOR TAB 2
def OnClick():
    connection=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};server='+a_textbox.get()+';database='+b_textbox.get()+';uid='+c_textbox.get()+';pwd='+d_textbox.get())
    Query_1=Query1_textbox.get(1.0,'end')
    Query_2=Query2_textbox.get(1.0,'end')
    Query_3=Query3_textbox.get(1.0,'end')
    Stage_Query=pd.read_sql(Query_1,connection)
    Stage_Query_count=Stage_Query.iloc[0]
    ODS_Query=pd.read_sql(Query_2,connection)
    ODS_Query_count=ODS_Query.iloc[0]
    delete_Query=pd.read_sql(Query_3,connection)
    Delete_Query_Count=delete_Query.iloc[0]
    SCount.set(int(Stage_Query_count[0]))
    OCount.set(int(ODS_Query_count[0]))
    DCount.set(int(Delete_Query_Count[0]))
    

def OnClick1():
    connection=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};server='+a_textbox.get()+';database='+b_textbox.get()+';uid='+c_textbox.get()+';pwd='+d_textbox.get())
    Query_D1=Query_Data_1.get(1.0,'end')
    Query_D2=Query_Data_2.get(1.0,'end')
    Q1=pd.read_sql(Query_D1,connection)
    Q2=pd.read_sql(Query_D2,connection)
    Q1.columns=Q2.columns
    for i in Q1.columns:
        Column_List.insert('insert',i)
        Column_List.insert('insert',"\n")
l1=list()
def OnMerge():
    global l1
    connection=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};server='+a_textbox.get()+';database='+b_textbox.get()+';uid='+c_textbox.get()+';pwd='+d_textbox.get())
    Query_D1=Query_Data_1.get(1.0,'end')
    Query_D2=Query_Data_2.get(1.0,'end')
    Q1=pd.read_sql(Query_D1,connection)
    Q2=pd.read_sql(Query_D2,connection)
    Q1.columns=Q2.columns
    for i in Q1.columns:
        l1.append(i)    
    data_001=pd.merge(Q1,Q2,on=l1,how="outer",indicator=True)
    with open("D:\\Test_Results.txt",'w') as file:
        file.write("outer Join Results")
        file.write("\n")
        file.write("{}".format(data_001.values))
        file.close()
    data_R=data_001[data_001._merge=="right_only"]
    with open("D:\\Test_Results.txt",'a+') as file:
        file.write("\n")
        file.write("Right Only")
        file.write("+++++++++++++++++++++++++")
        file.write("\n")
        file.write("{}".format(data_R.values))
        file.close()
    data_L=data_001[data_001._merge=="left_only"]
    with open("D:\\Test_Results.txt",'a+') as file:
        file.write("\n")
        file.write("Left Only")
        file.write("+++++++++++++++++++++++++")
        file.write("\n")
        file.write("{}".format(data_L.values))
        file.close()
    p_value.set("D:\\Test_Results.txt")
    
    
        
    
    


def OnClear1():
    Query1_textbox.delete(1.0,'end')
    Query2_textbox.delete(1.0,'end')
    Query3_textbox.delete(1.0,'end')
    Stage_Count_textbox.delete(0,'end')
    ODS_Count_textbox.delete(0,'end')
    Delete_Count_textbox.delete(0,'end')
    Query_Data_1.delete(1.0,'end')
    Query_Data_2.delete(1.0,'end')



tab2_labelframe=ttk.LabelFrame(tab2,text="COUNT AND DATA VALIDATION")
tab2_labelframe.grid(column=0,row=10,sticky=tk.W)

query1_label=ttk.Label(tab2_labelframe,text="SQuery_1")
query1_label.grid(column=0,row=1,sticky=tk.W)

scrollH=10
scrollW=20
Query1_textbox=scrolledtext.ScrolledText(tab2_labelframe,width=scrollW,height=scrollH,wrap=tk.WORD)
Query1_textbox.grid(column=1,row=1)

query2_label=ttk.Label(tab2_labelframe,text="OQuery_2")
query2_label.grid(column=3,row=1,sticky=tk.W)

Query2_textbox=scrolledtext.ScrolledText(tab2_labelframe,width=scrollW,height=scrollH,wrap=tk.WORD)
Query2_textbox.grid(column=4,row=1,sticky=tk.W)

query3_label=ttk.Label(tab2_labelframe,text="DQuery_3")
query3_label.grid(column=5,row=1,sticky=tk.W)

Query3_textbox=scrolledtext.ScrolledText(tab2_labelframe,width=scrollW,height=scrollH,wrap=tk.WORD)
Query3_textbox.grid(column=6,row=1)

Count_Label=ttk.Label(tab2_labelframe,text="Click to Verify Count")
Count_Label.grid(column=0,row=2,sticky=tk.W)

Count_butn=ttk.Button(tab2_labelframe,text="Click",command=OnClick)
Count_butn.grid(column=1,row=2,sticky=tk.W)

Stage_Count_Label=ttk.Label(tab2_labelframe,text="Count in Stage")
Stage_Count_Label.grid(column=0,row=3,sticky=tk.W)

SCount=tk.IntVar()
Stage_Count_textbox=tk.Entry(tab2_labelframe,text=SCount)
Stage_Count_textbox.grid(column=1,row=3,sticky=tk.W)

ODS_Count_Label=ttk.Label(tab2_labelframe,text="Count in ODS")
ODS_Count_Label.grid(column=0,row=4,sticky=tk.W)

OCount=tk.IntVar()
ODS_Count_textbox=ttk.Entry(tab2_labelframe,text=OCount)
ODS_Count_textbox.grid(column=1,row=4,sticky=tk.W)

Delete_Count_Label=ttk.Label(tab2_labelframe,text="Count of Del Statement")
Delete_Count_Label.grid(column=3,row=4,sticky=tk.W)

DCount=tk.IntVar()
Delete_Count_textbox=ttk.Entry(tab2_labelframe,text=DCount)
Delete_Count_textbox.grid(column=4,row=4,sticky=tk.W)

Query_Data_1_label=ttk.Label(tab2_labelframe,text="Query_D1")
Query_Data_1_label.grid(column=0,row=5,sticky=tk.W)

Query_Data_1=scrolledtext.ScrolledText(tab2_labelframe,width=scrollW,height=scrollH,wrap=tk.WORD)
Query_Data_1.grid(column=1,row=5,sticky=tk.W)

Query_Data_2_label=ttk.Label(tab2_labelframe,text="Query_D2")
Query_Data_2_label.grid(column=3,row=5,sticky=tk.W)

Query_Data_2=scrolledtext.ScrolledText(tab2_labelframe,width=scrollW,height=scrollH,wrap=tk.WORD)
Query_Data_2.grid(column=4,row=5,sticky=tk.W)

Column_List_Label=ttk.Label(tab2_labelframe,text="Columns to use")
Column_List_Label.grid(column=5,row=5,sticky=tk.W)

Column_List=scrolledtext.ScrolledText(tab2_labelframe,width=scrollW,height=scrollH,wrap=tk.WORD)
Column_List.grid(column=6,row=5,sticky=tk.W)

Merge_Button=ttk.Button(tab2_labelframe,text="Run Merge Query",command=OnMerge)
Merge_Button.grid(column=5,row=6,sticky=tk.W)

Path_results=ttk.Label(tab2_labelframe,text="Results stored Location")
Path_results.grid(column=6,row=6,sticky=tk.W)

p_value=tk.StringVar()
Path_results_box=ttk.Entry(tab2_labelframe,width=30,text=p_value,state='disabled')
Path_results_box.grid(column=7,row=6,sticky=tk.W)
                            

Data_Label=ttk.Label(tab2_labelframe,text="Click to verify the Data")
Data_Label.grid(column=0,row=7,sticky=tk.W)


Data_btn=ttk.Button(tab2_labelframe,text="Click",command=OnClick1)
Data_btn.grid(column=1,row=7,sticky=tk.W)


# Clear button to reset the fields

clear_label_01=ttk.Label(tab2_labelframe,text="Reset the Text fields")
clear_label_01.grid(column=0,row=15)

clear_button1=ttk.Button(tab2_labelframe,text="Clear",command=OnClear1)
clear_button1.grid(column=1,row=15,sticky=tk.W)


# Details of Tab 3

def OnClick3():
    connection=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};server='+a_textbox.get()+';database='+b_textbox.get()+';uid='+c_textbox.get()+';pwd='+d_textbox.get())
    Query_1=sourcelog_query.get(1.0,'end')
    cur=pd.read_sql(Query_1,connection)
    for i in cur.iloc[0]:
        output_scrollbox.insert('insert',i)
        output_scrollbox.insert('insert',"\n")

def OnClick4():
    time_details=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(Epoch_txtbox.get())))
    Date_var.set(time_details)

def OnClick5():
    connection=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};server='+a_textbox.get()+';database='+b_textbox.get()+';uid='+c_textbox.get()+';pwd='+d_textbox.get())
    Query_2=Last_Modified_Date_Query.get(1.0,'end')
    res=pd.read_sql(Query_2,connection)
    for i in res.iloc[0]:
        output_scrollbox_1.insert('insert',i)
        output_scrollbox_1.insert('insert',"\n")
    


def AllClear():
    sourcelog_query.delete(1.0,'end')
    Epoch_txtbox.delete(0,'end')
    Epoch_date_textbox.delete(0,'end')
    output_scrollbox.delete(1.0,'end')
    output_scrollbox_1.delete(1.0,'end')
    Last_Modified_Date_Query.delete(1.0,'end')

    
    
    
tab3_labelframe=ttk.LabelFrame(tab3,text="SourceLog table details")
tab3_labelframe.grid(column=0,row=15,sticky=tk.W)

scrollH=20
scrollW=30

sourcelog_label=ttk.Label(tab3_labelframe,text="Sourcelog table Query")
sourcelog_label.grid(column=0,row=0,sticky=tk.W)

sourcelog_query=scrolledtext.ScrolledText(tab3_labelframe,width=scrollH,height=scrollH,wrap=tk.WORD)
sourcelog_query.grid(column=1,row=0,sticky=tk.W)


Epoch_label=ttk.Label(tab3_labelframe,text="Enter the Epoch date value")
Epoch_label.grid(column=0,row=1,sticky=tk.W)

Epoch_Val=tk.IntVar()
Epoch_txtbox=ttk.Entry(tab3_labelframe,width=15,text=Epoch_Val)
Epoch_txtbox.grid(column=1,row=1,sticky=tk.W)

run_Query=ttk.Label(tab3_labelframe,text="Click to run the query")
run_Query.grid(column=0,row=2,sticky=tk.W)

Epoch_label=ttk.Label(tab3_labelframe,text="Click to convert the epoch date to normal date")
Epoch_label.grid(column=0,row=3,sticky=tk.W)


Date_btn=ttk.Button(tab3_labelframe,text="Click",command=OnClick3)
Date_btn.grid(column=1,row=2,sticky=tk.W)

Date_btn=ttk.Button(tab3_labelframe,text="Click",command=OnClick4)
Date_btn.grid(column=1,row=3,sticky=tk.W)

Epoch_Normal_Date_label=ttk.Label(tab3_labelframe,text="Converted Date Value")
Epoch_Normal_Date_label.grid(column=0,row=4,sticky=tk.W)

Date_var=tk.StringVar()
Epoch_date_textbox=ttk.Entry(tab3_labelframe,width=15,textvariable=Date_var)
Epoch_date_textbox.grid(column=1,row=4,sticky=tk.W)

Reset_Label_Tab3=ttk.Label(tab3_labelframe,text="Reset to clear the fields")
Reset_Label_Tab3.grid(column=0,row=8,sticky=tk.W)

Reset_Button_Tab3=ttk.Button(tab3_labelframe,text="Clear",command=AllClear)
Reset_Button_Tab3.grid(column=1,row=8,sticky=tk.W)

output_label=ttk.Label(tab3_labelframe,text="Query Output")
output_label.grid(column=3,row=0,sticky=tk.W)


output_scrollbox=Text(tab3_labelframe,width=100,height=20)
output_scrollbox.grid(column=4,row=0,sticky=tk.W)

Last_Modified_Date_Label=ttk.Label(tab3_labelframe,text="Query to Check last modified date value")
Last_Modified_Date_Label.grid(column=0,row=6,sticky=tk.W)

Last_Modified_Date_Query=scrolledtext.ScrolledText(tab3_labelframe,width=scrollW,height=scrollH,wrap=tk.WORD)
Last_Modified_Date_Query.grid(column=1,row=6,sticky=tk.W)

output_label=ttk.Label(tab3_labelframe,text="Query Output")
output_label.grid(column=3,row=6,sticky=tk.W)

output_scrollbox_1=Text(tab3_labelframe,width=10,height=10)
output_scrollbox_1.grid(column=4,row=6,sticky=tk.W)

run_Query=ttk.Label(tab3_labelframe,text="Click to run the query")
run_Query.grid(column=0,row=7,sticky=tk.W)

Date_btn=ttk.Button(tab3_labelframe,text="Click",command=OnClick5)
Date_btn.grid(column=1,row=7,sticky=tk.W)




win.mainloop()

