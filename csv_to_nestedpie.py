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


for x, y in data:
    if (x == 'Architecture (B. Arch)' and y== 'First year admission'):
        archfy+=1
    elif (x == 'Architecture (B. Arch)' and y== 'Direct second year admission'):
        archdsy+=1
    elif (x == 'B.E. in Civil Engineering' and y == 'First year admission'):
        cefy+=1
    elif (x == 'B.E. in Civil Engineering' and y == 'Direct second year admission'):
        cedsy+=1
    elif (x == 'B.E. in Computer Engineering' and y == 'First year admission'):
        cofy+=1
    elif (x == 'B.E. in Computer Engineering' and y == 'Direct second year admission'):
        codsy+=1
    elif (x == 'B.E. in Electrical Engineering' and y == 'First year admission'):
        eefy+=1
    elif (x == 'B.E. in Electrical Engineering' and y == 'Direct second year admission'):
        eedsy+=1
    elif (x == 'B.E. in Electronics and Telecommunication Engineering' and y == 'First year admission'):
        extcfy+=1
    elif (x == 'B.E. in Electronics and Telecommunication Engineering' and y == 'Direct second year admission'):
        extcdsy+=1
    elif (x == 'B.E. in Mechanical Engineering' and y == 'First year admission' ):
        mefy+=1
    elif (x == 'B.E. in Mechanical Engineering' and y == 'Direct second year admission' ):
        medsy+=1
    elif (x == 'Pharmacy (B. Pharm)' and y == 'First year admission' ):
        pharmfy+=1
    elif (x == 'Pharmacy (B. Pharm)' and y == 'Direct second year admission' ):
        pharmdsy+=1
    elif (x == 'M.E. in Construction Engineering and Management' and y == 'First year admission'):
        meconstfy+=1
    elif (x == 'M.E. in Construction Engineering and Management' and y == 'Direct second year admission' ):
        meconstdsy+=1
    elif (x == 'Ph.D. in Civil Engineering' and y == 'First year admission' ):
        phdcefy+=1
    elif (x == 'Ph.D. in Civil Engineering' and y == 'Direct second year admission' ):
        phdcedsy+=1
       

mydata=pd.read_csv(input_csv)
courses=mydata["Choose your preferred Course (affiliated to Mumbai University)"]
addmission_year=mydata["Choose your preferred admission year."]

chosen_count=[]
Barch=0
Bece=0
Beco=0
Beee=0
Beextc=0
Beme=0
Bpharm=0
Mecons=0
Phd=0
cnt=[]
for course in courses:
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
    



chosen_count.append(Bece)
chosen_count.append(Phd)
chosen_count.append(Beco)
chosen_count.append(Beee)
chosen_count.append(Beextc)
chosen_count.append(Beme)
chosen_count.append(Barch)
chosen_count.append(Bpharm)
chosen_count.append(Mecons)

#plotting piechart
courses_offered=["B.E. in Civil Engineering","Ph.D. in Civil Engineering","B.E. in Computer Engineering","B.E. in Electrical Engineering","B.E. in Electronics and Telecommunication Engineering","B.E. in Mechanical Engineering","Architecture (B. Arch)","Pharmacy (B. Pharm)","M.E. in Construction Engineering and Management"]

labels = courses_offered
sizes = chosen_count
labels_sub = ["CE-FY", "CE-DSY", "CO-FY", "CO-DSY", "EE-FY", "EE-DSY", "EXTC-FY", "EXTC-DSY", "ME-FY", "ME-DSY", "Arc-FY", "Arc-DSY", "Pha-FY", "Pha-DSY"]
sizes_sub=[cefy, cedsy, cofy, codsy, eefy, eedsy, extcfy, extcdsy, mefy, medsy, archfy, archdsy, pharmfy, pharmdsy]

color=["bisque","salmon","gold","turquoise","lightgreen","violet","palegreen","cyan","lightblue"]
color_sub=['#f9e2b9','#f4e9ce','#F0E68C','#e1ad21', '#48d1cc','#15f4ee', '#84fa84','#a8e4a0', '#FFB6C1','#F08080','#cffecc','#6bcd6e','#a8dbf5','#50d9ff']


# labels_sub = ["CE-FY", "CE-DSY", "PhD-CE-FY", "PhD-CE-DSY", "CO-FY", "CO-DSY", "EE-FY", "EE-DSY", "EXTC-FY", "EXTC-DSY", "ME-FY", "ME-DSY", "Arc-FY", "Arc-DSY", "Pha-FY", "Pha-DSY", "MECon-fy", "MECon-DSY"]
# sizes_sub=[cefy, cedsy, phdcefy, phdcedsy, cofy, codsy, eefy, eedsy, extcfy, extcdsy, mefy, medsy, archfy, archdsy, pharmfy, pharmdsy, meconstfy, meconstdsy]

# color=["bisque","gold","salmon","turquoise","lightblue","violet","palegreen","cyan","lightgreen"]
# color_sub=['#606782','#6960EC','#6CC417','#FFCBA4', '#6960EC','#C8B560', '#54C571','#A9AA5F', '#6160AB','#614051','#357EC7','#F9FAAF','#C24641','#BAFAAF', '#9CB071','#827B60', '#368BC1','#FAAFBA', '#3BB9FF']



bigger = plt.pie(sizes, labels=labels, colors=color, startangle=90, frame=True, autopct='%d')
smaller = plt.pie(sizes_sub, labels=labels_sub, colors=color_sub, radius=0.7, startangle=90, labeldistance=0.7, autopct='%d')

centre_circle = plt.Circle((0, 0), 0.4, color='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.legend(bbox_to_anchor=(1,1))
plt.title("Admission 2020-21")
plt.axis('equal')
plt.tight_layout()

plt.show()
