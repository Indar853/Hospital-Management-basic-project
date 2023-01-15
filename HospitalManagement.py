'''

created on Wed,24 Dec,2022  09:29 PM
@Developer : Indar Kumar
@GitHub ID : https://github.com/Indar853

'''


import pandas as pd
import matplotlib.pyplot as plt

intro_menu = """
    ========================================
    **************************************
    *---  HOSPITAL MANAGEMENT SYSTEM  ---*
    **************************************
    
    
    Data Analysis:
        1.  Reading doctor file without index.
        2.  Adding new doctor detail.
        3.  Reading doctor file with new coloumn names.
        4.  Sort doctor details by name.
        5.  Readimg patient file without index.
        6.  Deleting a coloumn from patient table.
        7.  Display patient names.
        8.  Display all bills.
        9.  Display total bills.
        10. Increasing doctor visit charge by 500.
        11. Display records of workers.
        12. Display highest salary being paid.
        13. Saving workers file after increasing salary by 500.
        
    
    Data Visualization:
        14. Line plot.
        15. Bar plot.
        16. Chart plot
        
    ========================================
    """


def menu():
	print(intro_menu)

menu()


def no_index():
	print("Display doctor details without index.")
	df = pd.read_csv("Doctor.csv",index_col=0)
	print("without index")
	print(df)
	
def new_doctor():
	print('Adding new doctor in file doctor')
	df=pd.read_csv("Doctor.csv")
	df.loc[len(df)]=[105,'Dr. Geeta',50,'Surgery',9899065266]
	print(df)

def new_colnam():
	print('Display details of Doctors with new names')
	df=pd.read_csv('Doctor.csv',skiprows=1,names=['DoctorID','DoctorName','DoctorAge','DoctorDepartment','DoctorPhone'])
	print(df)

def sort_doctor():
	print('sorting Doctors names and details Ascending order')
	df=pd.read_csv('Doctor.csv',index_col=0)
	df=df.sort_values('d_name')
	print(df)

def patient():
	df=pd.read_csv("Patient.csv",index_col=0)
	print('Patient detail without index')
	print(df)

def delete_col():
	print("delete coloumn Age from Patient table")
	df=pd.read_csv("Patient.csv")
	print(df)
	print()
	print()
	del df['p_age']
	print(df)

def patient_name():
	print('show patient list')
	df=pd.read_csv("Patient.csv",usecols=['p_name'])
	print(df)

def bill():
	print('Display details of bill')
	df=pd.read_csv("hbill.csv",index_col=0)
	print('without index')
	print(df)

def total_bill():
	print("To display total bill")
	df=pd.read_csv("hbill.csv",)
	print(df)
	print()
	df1=df['drvisit']+df['medicines']+df['room']
	print(df1)

def fee_inc():
	print('previous doctor fee')
	df=pd.read_csv("hbill.csv",index_col=0)
	print(df)
	print()
	print('increase doctor fee by Rs. 500')
	print()
	df['drvisit']+=500
	print(df)

def worker():
	print('show records of workers')
	df=pd.read_csv("Worker.csv",index_col=0)
	print(df)

def maxsal():
	df=pd.read_csv("Worker.csv")
	print('highest salary')
	print(df.salary.max())

def saveworker():
	print('To increase salary and save ')
	df=pd.read_csv("Worker.csv",index_col=0)
	print(df)
	print()
	print('increase salary by Rs. 500')
	print()
	df=df['salary']+500
	print()
	df.to_csv("Worker.csv")
	print(df)
	df=pd.read_csv("Worker.csv")
	print(df)

################################

def line_plot():
	print('line plot')
	df=pd.read_csv("hbill.csv")
	print(df)
	x1=df['medicines']
	y1=df['room']
	plt.xlabel('medicienes')
	plt.ylabel('room')
	plt.plot(x1,y1,color='r',linewidth=5,marker='o',markerfacecolor='blue')
	plt.title('charges of Medicines and Room records')
	plt.show()

def bar_plot():
	print('bar plot')
	df=pd.read_csv("hbill.csv")
	print(df)
	x1=df['medicines']
	y1=df['room']

	plt.xlabel('medicines',fontsize=14,color="r")
	plt.ylabel('room',fontsize=14,color="r")
	plt.title('Paid for Medicines and Room ',fontsize=14,color="blue")
	plt.xticks(fontsize=14,rotation=30)
	plt.bar(x1,y1,width=40,facecolor='r',edgecolor='green')
	plt.show()

def pie_plot():
	print('pie plot')
	df=pd.read_csv("hbill.csv")
	print(df)
	plt.title(" Charges on room, Medicines, Dr. visit on the items")
	z=eval(input("enter charges of Room, Medicines, Dr. visit in sq bracket : "))
	items=['medicines','room','DrVisit']
	expl=[0,0,0.2]
	plt.pie(z,colors=['red','green','blue'],labels=items,explode=expl,autopct="%5.1f%%")
	plt.show()

choice=""
choice=int(input('Enter your choice number: '))
if choice==1:
	no_index()
elif choice==2:
    new_doctor()
elif choice==3:
	new_colnam()
elif choice==4:
    sort_doctor()
elif choice==5:
    patient()
elif choice==6:
	delete_col()
elif choice==7:
    patient_name()
elif choice==8:
    bill()
elif choice==9:
	total_bill()
elif choice==10:
    fee_inc()
elif choice==11:
    worker()
elif choice==12:
	maxsal()
elif choice==13:
	saveworker()
elif choice==14:
    line_plot()
elif choice==15:
    bar_plot()
elif choice==16:
	pie_plot()
else:
	print('invalid value.')
