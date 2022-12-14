import pandas as pd
print("\n--------------------------------\n")
doctor={
	"d_id":[107,102,110,106],
	"d_name":["Dr. Bajaj","Dr. Kumar","Dr. Preeti","Dr. Goel"],
	"d_age":[56,29,34,48],
	"Department":["Gastro","Neuro","Oncology","Skin"],
	"d_phone":[7569473697,7569365689,6857983500,8529468570]
}
d_df=pd.DataFrame(doctor)
print(d_df)
print("\n--------------------------------\n")
worker={
	"w_id":[301,302,303],
	"w_name":["Ram kumar","Meera devi","Lakhan"],
	"post":["Ward Boy","Nurse","Sweeper"],
	"mobile":[9856745947,8567459376,9786479640],
	"salary":[28000,30000,12000]
}
w_df=pd.DataFrame(worker)
print(w_df)
print("\n--------------------------------\n")
patient={
	"p_id":[201,202],
	"p_name":["Mr. Jain","Mrs. Neetu"],
	"p_age":[49,57],
	"Diesease":["Skin","Stomach tumour"],
	"p_phone":[8756984534,7567458734]
}
p_df=pd.DataFrame(patient)
print(p_df)
print("\n--------------------------------\n")
bills={
	"p_id":[201,202],
	"p_name":["Mr. Jain","Mrs. Neetu"],
	"p_age":[49,57],
	"drvisit":[3000,2000],
	"medicines":[3600,2300],
	"room":[5000,2000]
}
hb_df=pd.DataFrame(bills)
print(hb_df)
print("\n--------------------------------\n")

#==============-to-CSV-==============
d_df.to_csv("Dotor.csv",index=False)
w_df.to_csv("Worker.csv",index=False)
p_df.to_csv("Patient.csv",index=False)
hb_df.to_csv("hbill.csv",index=False)
print("\n\n------------\nall dataframe have successfully converted to csv.\n------------")