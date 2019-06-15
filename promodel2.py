import random
print('--------------------------------------------------------')
print('--------WELCOME TO HOMEOPATHIC EXPERT SYSTEM---------- |')
print('enter which category do you want diagnosis             |')
print('1.children(from 1-12 years)                            |')
print('2.adults(from 13-40 years)                             |')
print('3.old people(40+)                                      |')
print('--------------------------------------------------------')
b=[]
while(1):
    a=int(input())
    c=0
    print('enter the name of the patient')
    name=input()
    while(1):
        if(name.isalpha()==True):
            break
        else:
            print('enter a valid name')
            name=input()
    print('enter the age of the patient in years')
    age=int(input())
    while(1):
        if(age<=100):
            break
        else:
            print('enter valid age')
            age=int(input())
    if(a==1):
       print('------------------------------welcome to children care unit----------------------------------------')
       print('YOU HAVE TO ANSWER A FEW QUESTIONS WITH YES or NO')
       chi=['hyper active','bed wetting','cold','growth deficiency','fever','calcium deficiency','constipation']
       #med=['KINDIVAL','ENUKIND','NISIKIND','ANEKIND','ECHINACEA ANGUSTIFOLIA 1X','CALCIOKIND','TUSSIKIND']
       diag={'hyper active':'KINDIVAL','bed wetting':'ENUKIND','cold':'NISIKIND','growth deficiency':'ANEKIND','fever':'ECHINACEA ANGUSTIFOLIA 1X','calcium deficiency':'CALCIOKIND','constipation':'TUSSIKIND'}
       f = open('questions.txt','r')
       fcontents = f.read()
       a1=list(fcontents.split('\n'))
       for i in range(10):
            question = a1[random. randrange(17)]
            print(question)
            ans=input()
            while(1):
                if(ans.lower()=='yes' or ans.lower()=='no'):
                    break
                else:
                    print('please enter a valid answer')
                    print(question)
                    ans=input()
            if(ans.lower()=='yes'):
                c=c+1
       symptoms1=random.choice(chi)
       medicine1=diag[symptoms1]
       symptoms2=random.choice(chi)
       medicine2=diag[symptoms2]
       f=open("patients.txt","a")
       f.write("patient details\n")
       f.write("name: %s\r\n"%name)
       f.write("age: %d\r\n"%age)
       f.write("category: children\n")
       f.write("symptoms: %s\r\n"%symptoms1)
       f.write("medicines: %s\r\n"%medicine1)
       if(age<6):
          f.write("dosage: 200mg\n")
       else:
          f.write("dosage: 500mg\n")
       f.close()
       if(c==0):
           print('you just gave all response with "no" hope you carefully read the questions and gave it')
           print('if you responded properly then its all right')
       elif(c>=6):
            print('no need to worry just a small amount of medicines are reqired')
            print('the disease symptoms your child having is ',symptoms1,symptoms2)
            print('the medicine your child having is',medicine1,medicine2)
       else:
           print(' if you gave all the right answers then you dont need to worry your child is all right')
           print('but be careful and take the preventive measures')
       break
    elif(a==2):
        print('----------------------------------WELCOME TO ADULT CARE UNIT---------------------------------------------------')
        print('YOU HAVE TO ANSWER A FEW QUESTIONS WITH YES or NO')
        chi=['fever','tonsilities','vomitings','cold','cough','head ache','Cholesterol','diabetes','diarreah','acidity','travel sickness','dysentry']
       # med=['ACONITUM PENTARKAN','MUNOSTIM','ALPHA-TONS','ALPHA-LIV','ALPHA-WD','NUSIKIND','TUSSIKIND','bi-combination no-1','alpha-ms','alpha-acid','kolikind','kindigest','alpha-liv','natrum muriaticum','Aconitum Pentarkan']
        diag={'fever':'ACONITUM PENTARKAN','tonsilities':'MUNOSTIM','vomitings':'ALPHA-TONS','cough':'ALPHA-LIV','head ache':'NUSIKIND','Cholesterol':'bi-combination no-1','diabetes':'alpha-ms','diarreah':'kindigest','travel sickness':'Aconitum Pentarkan','dysentry':'kolikind','acidity':'alpha-acid'}
        f = open('questions.txt','r')
        fcontents = f.read()
        a1=list(fcontents.split('\n'))
        for i in range(10):
            question = a1[random. randrange(18,41)]
            print(question)
            ans=input()
            while(1):
                if(ans.lower()=='yes' or ans.lower()=='no'):
                    break
                else:
                    print('please enter either yes or no')
                    print(question)
                    ans=input()
            if(ans.lower()=='yes'):
                c=c+1
        symptoms1=random.choice(chi)
        medicine1=diag[symptoms1]
        symptoms2=random.choice(chi)
        medicine2=diag[symptoms2]
        f=open("patients.txt","a")
        f.write("patient details\n")
        f.write("name: %s\r\n"%name)
        f.write("age: %d\r\n"%age)
        f.write("category: adult\n")
        f.write("symptoms: %s\r\n"%symptoms1)
        f.write("medicines: %s\r\n"%medicine1)
        f.write("dosage: 650mg\n")
        f.close()
        if(c==0):
           print('you just gave all response with "no" hope you carefully read the questions and gave it')
           print('if you responded properly then its all right')
        elif(c>=5):
            print('no need to worry just a small amount of medicines are reqired')
            print('the disease symptoms your child having is ',symptoms1,symptoms2)
            print('the medicine your child having is',medicine1,medicine2)
        else:
           print(' if you gave all the right answers then you dont need to worry you are all right')
           print('but be careful and take the preventive measures')
        break
    elif(a==3):
        print('----------------------------------WELCOME TO OLDAGE CARE UNIT---------------------------------------------------')
        print('YOU HAVE TO ANSWER A FEW QUESTIONS WITH YES or NO')
        chi=['cramps','muscular pain','rheamatic pain','bone problems','body ache','head ache','joints','inflamation','diabetes','osteorthritis','spasms','diarreah','acidiy','vomitings','colic','naseau','motion sickness','loss of apetite','travel sickness','constipation','dysentry','cough','irratating cough','breathlessness','nasal congestion']
        med=['MAGNESIUM PHOSPHORICUM','Alpha-MP','ALPHA-TONS','ALPHA-LIV','ALPHA-WD','Calcarea phosphorica','TOPI ARNICA CREAM','bi-combination no-8','Topi MP Gel','Topi Heal Cream','Kali phosphoricum','Aconitum Pentarkan','Glycyrrhiza glabra 1X','alpha-cc']
        f = open('questions.txt','r')
        fcontents = f.read()
        a1=list(fcontents.split('\n'))
        for i in range(10):
            question = a1[random. randrange(18,45)]
            print(question)
            ans=input()
            while(1):
                if(ans.lower()=='yes' or ans.lower()=='no'):
                    break
                else:
                    print('please enter a valid answer')
                    print(question)
                    ans=input()
            if(ans.lower()=='yes'):
                c=c+1
        symptoms1=random.choice(chi)
        medicine1=random.choice(med)
        symptoms2=random.choice(chi)
        medicine2=random.choice(med)
        f=open("patients.txt","a")
        f.write("patient details\n")
        f.write("name: %s\r\n"%name)
        f.write("age: %d\r\n"%age)
        f.write("category: adult\n")
        f.write("symptoms: %s\r\n"%symptoms1)
        f.write("medicines: %s\r\n"%medicine1)
        f.write("dosage: 650mg\n")
        f.close()        
        
        if(c<=4):
            print('no need to worry just a small amount of medicines are reqired')
            print('the diseases you are having is ',symptoms1,symptoms2)
            print('the medicine you should take is',medicine1,medicine2)
        else:
            print("you need to concentrate on more on your  health")
            print('the diseases you are having is ',symptoms1,symptoms2)
            print('the medicine you should take is',medicine1,medicine2)
        
        break
    
   
         
    else:
        print('please enter a valid option')
