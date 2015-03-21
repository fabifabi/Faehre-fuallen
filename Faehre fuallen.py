#improts
import sys
import os

#Strategie unabhaengige Funktionen
def einlesen(datei):
     try:
          datei = open(datei)
     except:
          print("Die datei ",datei," konnte nicht gefunden werden")
          os.system("pause")
     #Lesen und Schlissen der Datei
     Autos = datei.read()
     datei.close()
     
     #Umwandelsn in float
     try:
         floats = [float(x) for x in Autos.split(' ')]
     except:
         print("Die Laengen müssen durch Leerzeichen getrent sien!")
         os.system("pause")
     return(floats)

#Strategie A
def strategiea(autos) :
     p =0.00
     p2=0.00
     p3=0.00
     auto = 0
     wert =len(autos)
     while auto < wert:
          a = autos[auto] + 0.30
          if a < 6:
              #Bahn 1
              p = p + a
              if p < 20:
                  auto += 1
                  print("Bahn 1 Auto", auto)
                  continue
              else:
                  #Ausweichen auf Bahn 2
                  p = p - a
                  p2 = p2 + a
                  if p2 < 20:
                      auto += 1
                      print("Bahn 2 Auto", auto)
                      continue
                  else:
                      #Ausweichen auf Bahn 3
                      p2 = p2 - a
                      p3 = p3 + a
                      if p3 < 20:
                          auto += 1
                          print("Bahn 3 Auto", auto)
                          continue
                      else:
                          #Faehre voll
                          break
          #Autos die Laeger als 6 sind
          if a > 6:
                #Bahn 2
                p2 = p2 + a
                if p2 < 20:
                    auto += 1
                    print("Bahn 2 Auto", auto)
                    continue
                else:
                    #Bahn 2
                    p2 =p2 - a
                    p3 = p3 + a
                    if p3 < 20:
                        auto +=1
                        print("Bahn 3 Auto", auto)
                        continue
                    else:
                        #Faehre voll
                        break
     os.system("pause")

     
#Strategie B

def strategieb(autos) :
     p    = 0.00
     p2   = 0.00
     p3   = 0.00
     auto = 0
     wert = len(autos)
     while auto < wert:
         
         #Bahn 1
         a = autos[auto] + 0.30
         p = p + a
         if p < 20.0:
             auto += 1
             i = 0
             print("Bahn 1 Auto", auto)
         else:
            p = p - a
            i += 1

         #Bahn 2   
         a = autos[auto] + 0.30
         p2 = p2 + a
         if p2 < 20.0:
             auto += 1
             i = 0
             print("Bahn 2 Auto", auto)
         else:
             p2 = p2 - a
             i += 1

         #Bahn 3    
         a = autos[auto] + 0.30
         p3 = p3 + a
         if p3 < 20.0:
             auto += 1
             i = 0
             print("Bahn 3 Auto", auto)
         else:
             p3 = p3 - a
             i += 1

         #Faehre Voll?    
         if i>=3:
             i = 0
             break
             
     os.system("pause")
     

#Start

print("Name der Datei")
name = input()
autosy = einlesen(name)
print(autosy)
print("Strategie waehlen A oder B")
x = input()

     
if x == "A":
    strategiea(autosy)
if x == "a":
    strategiea(autosy)
if x == "B":
    strategieb(autosy)
if x == "b":
    strategieb(autosy)
