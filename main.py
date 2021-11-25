def taisnsturis():
  a= int(input("ievadi taisnstūra platumu m:"))
  b= int(input("ievadi taisnstūra garumu m:"))
  if a==b:
    S=a*b
    print("tas ir kvadrāts un tā laukums ir",S,"metri")
  else:
    S= a*b
    print("Taisnstūra laukums ir", S,"metri")
def kvadrats():
  a= int(input("ievadi kvardāta malas garumu metros:"))
  S=a*a
  print("kvadrāta lukums ir",S,"metri")
def rinkis():
  r=int(input("ievadi riņķa rādiusu metros:"))
  R2=r*r
  S=3.14*R2
  print("Riņķa laukums ir",S,"metri")




print("Lai aprēķināu laukumu nepieciešamai tev figūrai lūdzu nospied burtu kurš tai atbilst")
print("T - ja figūra kaurai vēlies aprēķināt laukumu ir trijstūris")
print("Tr - ja figūra kaurai vēlies aprēķināt laukumu ir trapece")
print("P - ja figūra kaurai vēlies aprēķināt laukumu ir paralelograms")
print("Ta - ja figūra kaurai vēlies aprēķināt laukumu ir taisnstūris")
print("K - ja figūra kaurai vēlies aprēķināt laukumu ir kvadrāts")
print("R - ja figūra kaurai vēlies aprēķināt laukumu ir riņķis")

x= input()
if x == "Ta":
  taisnsturis()


  
elif x== "K":
  kvadrats()
elif x=="R":
  rinkis()
else:
  print("Ievadītā vērtība neatbilst prasītajām un uzdevumu izpildīt nav iespējams")
   