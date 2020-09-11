import csv
import json
import pandas as pd
import matplotlib.pyplot as plt
input_csv = r"c:\Users\dell ugwht\Desktop\Admission Enquiry (2020-21).csv"   #input file path


archfy=cefy=cofy=eefy=extcfy=mefy=pharmfy=meconstfy=phdcefy=archdsy=cedsy=codsy=eedsy=extcdsy=medsy=pharmdsy=meconstdsy=phdcedsy=0

mydata=pd.read_csv(input_csv)
courses=mydata["Choose your preferred Course (affiliated to Mumbai University)"]
addmission_year=mydata["Choose your preferred admission year."]

pref_course = []
adm_yr = []

for i in range(len(courses)):
    pref_course.append(courses[i])
    adm_yr.append(addmission_year[i])
    
data = []
for i in range(len(courses)):
    t = (pref_course[i], adm_yr[i])
    data.append(t)

fe=[]
dsy=[]

for x, y in data:
    if y == 'First year admission':
        fe.append(x)
    elif y == 'Direct second year admission':
        dsy.append(x)





dsy_count=[]
Barch=0
Bece=0
Beco=0
Beee=0
Beextc=0
Beme=0
Bpharm=0
Mecons=0
Phd=0

for course in dsy:
    if course=="Architecture (B. Arch)":
        Barch+=1 
    elif course=="B.E. in Civil Engineering":
        Bece+=1
    elif course=="B.E. in Computer Engineering":
        Beco+=1
    elif course=="B.E. in Electrical Engineering":
        Beee+=1
    elif course=="B.E. in Electronics and Telecommunication Engineering":
        Beextc+=1
    elif course=="B.E. in Mechanical Engineering":
        Beme+=1
    elif course=="Pharmacy (B. Pharm)":
        Bpharm+=1
    elif course=="M.E. in Construction Engineering and Management":
        Mecons+=1
    elif course=="Ph.D. in Civil Engineering":
        Phd+=1

dsy_count.append(Bece)
dsy_count.append(Phd)
dsy_count.append(Beco)
dsy_count.append(Beee)
dsy_count.append(Beextc)
dsy_count.append(Beme)
dsy_count.append(Barch)
dsy_count.append(Bpharm)
dsy_count.append(Mecons)

courses_offered=["B.E. in Civil Engineering","Ph.D. in Civil Engineering","B.E. in Computer Engineering","B.E. in Electrical Engineering","B.E. in Electronics and Telecommunication Engineering","B.E. in Mechanical Engineering","Architecture (B. Arch)","Pharmacy (B. Pharm)","M.E. in Construction Engineering and Management"]
p=courses_offered
print(dsy_count)
color=["bisque","turquoise","salmon","gold","lightblue","violet","palegreen","cyan","lightgreen"]
explode=[]
plt.title("Admission enquiry for Direct second year")
p, tx, autotexts = plt.pie(dsy_count,labels=p,colors=color, startangle=90, autopct='')
for i, a in enumerate(autotexts):
    a.set_text("{}".format(dsy_count[i]))

plt.axis('equal')
plt.legend(bbox_to_anchor=(0.25,0.25))
plt.show()





fe_count=[]
Barch=0
Bece=0
Beco=0
Beee=0
Beextc=0
Beme=0
Bpharm=0
Mecons=0
Phd=0

for course in fe:
    if course=="Architecture (B. Arch)":
        Barch+=1 
    elif course=="B.E. in Civil Engineering":
        Bece+=1
    elif course=="B.E. in Computer Engineering":
        Beco+=1
    elif course=="B.E. in Electrical Engineering":
        Beee+=1
    elif course=="B.E. in Electronics and Telecommunication Engineering":
        Beextc+=1
    elif course=="B.E. in Mechanical Engineering":
        Beme+=1
    elif course=="Pharmacy (B. Pharm)":
        Bpharm+=1
    elif course=="M.E. in Construction Engineering and Management":
        Mecons+=1
    elif course=="Ph.D. in Civil Engineering":
        Phd+=1

fe_count.append(Bece)
fe_count.append(Phd)
fe_count.append(Beco)
fe_count.append(Beee)
fe_count.append(Beextc)
fe_count.append(Beme)
fe_count.append(Barch)
fe_count.append(Bpharm)
fe_count.append(Mecons)

courses_offered=["B.E. in Civil Engineering","Ph.D. in Civil Engineering","B.E. in Computer Engineering","B.E. in Electrical Engineering","B.E. in Electronics and Telecommunication Engineering","B.E. in Mechanical Engineering","Architecture (B. Arch)","Pharmacy (B. Pharm)","M.E. in Construction Engineering and Management"]
p=courses_offered
print(fe_count)
color=["bisque","turquoise","salmon","gold","lightblue","violet","palegreen","cyan","lightgreen"]
explode=[]
plt.title("Admission enquiry for First year")
p, tx, autotexts = plt.pie(fe_count,labels=p,colors=color,autopct='')
for i, a in enumerate(autotexts):
    a.set_text("{}".format(fe_count[i]))

plt.axis('equal')
plt.legend(bbox_to_anchor=(0.25,0.25))
plt.show()