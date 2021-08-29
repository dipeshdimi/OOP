
print("\n\n\n")
print("---------------------------------------++ WELCOME TO XYZ BLOOD DONATION BLOOD SERVICES ++-----------------------------------------")
print("\n                                                 This Is A Login Portal\n\n")
print("Please follow the given instructions in order to log in")
print("\nFOR ADMIN LOGIN: PRESS 1")
print("FOR USER LOGIN : PRESS 2")
q=int(input())

class donor:
  x=0 #for counting no. of donors
  def __init__(self,name,age,sex,blood_group,platelets_count,wbc_count,rbc_count):
    self.name=name
    self.age=age
    self.sex=sex
    self.blood_group=blood_group
    self.platelets_count=platelets_count
    self.wbc_count=wbc_count
    self.rbc_count=rbc_count
    donor.x+=1

donor_1=donor('ALOK',20,'MALE','A+',200234,34768,54678)
donor_2=donor('AMIT',44,'MALE','AB-',203456,36758,56780)
donor_3=donor('ANSHIKA',34,'FEMALE','O+',345670,45678,36987)
donor_4=donor('SUJATA',29,'FEMALE','B-',354678,67547,45691)
donor_5=donor('SUMIT',31,'MALE','A+',321432,56543,56764)
donor_6=donor('REKHA',33,'FEMALE','A-',265439,45654,65478) 
donor_7=donor('RAMIT',48,'MALE','A+',234188,45678,65785)
donor_8=donor('RAJESH',24,'MALE','A+',267554,45694,56543)
donor_9=donor('RAKESH',25,'MALE','AB+',265354,46614,52743)
donor_10=donor('SHANKAR',52,'MALE','A+',267462,45204,56783) 


def blood_banks():
  print("\n\nFollowing blood banks are avalable near you: ")
  print("\n\n1. Jeevan Jyoti Blood Bank")
  print("\n2. Indra Diagonostic Centre & Blood Bank")
  print("\n3. AMA Blood Bank")
  print("\n4. ML Nehru Blood Bank")
  print("\n5. Indra Blood Bank")
  print("\n6. City Hospital and Blood Bank")


def rare_blood_groups():
  print("\nDonors with rare blood groups and their details are listed below: ")
  print("\nNAME       AGE         SEX           BLOOD_GROUP\n")
  print("AMIT       44         MALE           AB-\n")
  print("ANSHIKA    34         FEMALE         O+\n")
  print("SUJATA     29         FEMALE         B-\n")
  print("RAKESH     25         MALE           AB+\n")

if q==1:
  print("\n\n-------------------- Welcome Admin ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  if w=='sudeepto':
    b=input("\nUsername found!\n\n Please enter your password: ")  
    b.lower()
    if b=='password':
      print("\nSigned In successfully!")
      print("\n\n-------------Hello Admin Welcome back-----------------")
      print("\n\nTell me what you want to know")
      print("\n1. Details of the Donors")       #Only admins can know the details of the donors
      print("\n2. Details of the Blood Banks")
      print("\n3. Details of the donors with rare blood groups")
      a=int(input("\n\nEnter a choice from the above: "))
      if a==1:
        l1=[donor_1,donor_2,donor_3,donor_4,donor_5,donor_6,donor_7,donor_8,donor_9,donor_10]
        for f in l1:
          print("\n")
          print(f.__dict__)
      elif a==2:
        blood_banks()
      elif a==3:
        rare_blood_groups()
      else:
        print("\nInvalid Choice!")
    else:
      print("\nPassword doesn't match!")
  
  else:
    print("\nAdmin not found. Please enter the correct Username")

elif q==2:
  print("\n\n-------------------- Welcome User ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  if w=='rohit' or 'rohan' or 'suraj' or 'chetan' or 'anamika':
    b=input("\nUsername found!\n\n Please enter your password: ")  
    b.lower()
    if b=='password':
      print("\nSigned In successfully!")
      print("\n\n-------------Hello User Welcome back-----------------")
      print("\n\nTell me what you want to know")
      print("\n1. Number of the Donors available")  #Users can only know the number of donors available and not their details
      print("\n2. Details of the Blood Banks")
      print("\n3. Details of the donors with rare blood groups")
      a=int(input("\n\nEnter a choice from the above: "))
      if a==1:
        print("\nTotal number of Donors avalable is: ",donor.x) #donor.x for counting the number of donors
      elif a==2:
        blood_banks()
      elif a==3:
        rare_blood_groups()
      else:
        print("\nInvalid Choice!")
    else:
      print("\nPassword doesn't match!")
  
  else:
    print("\nUser not found. Please enter the correct Username")

else:
  print("\nWrong Choice! Please enter from the above choice only")