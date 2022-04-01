from Worker import Worker
from Boleta import Boleta
from colorama import *


def principal():
      print(f"""
                  ----------------------------- 
                  |  RAZON SOCIAL:  FERROTEK  |
                  ----------------------------- 
          
      INGRESAR DATOS:
      """)
      #Entrada
      
      worker= str(input("TRABAJADOR :  ").upper())# la funcion upper sirve para que el contenido se convierta en mayúscula
      
      
      while True: #se usa el bucle "WHILE" para que el programa pregunte hasta que se ingrese un dato valido
            try:
                  category= str(input("CATEGORÍA (A, B o C) :  ").upper())
                  if category == 'A' or category == 'B' or category == 'C':
                        break 
                  else:
                        print(Fore.CYAN,'EL CARÁCTER INGRESADO NO PERTENECE A LAS CATEGORÍAS ESTABLECIDAS',Fore.RESET)
            except:
                  print(Fore.CYAN,'EL CARÁCTER INGRESADO NO PERTENECE A LAS CATEGORÍAS ESTABLECIDAS',Fore.RESET)
      
      while True:
            try:
                  exhours= int(input("HORAS EXTRAS :  "))
                  break  # Si introduce el dato correcto, se detiene el "while" con "break"
            except ValueError:
                  print(Fore.CYAN,"DATO INVALIDO",Fore.RESET)
      while True:
            try:
                  mxt= int(input("TARDANZAS (minutos) :  "))
                  break  # Si introduce el dato correcto, se detiene el "while" con "break"# Si no da error, corto el while con break
            except ValueError:
                  print(Fore.CYAN,"DATO INVALIDO",Fore.RESET)
        
      #Boloque principal
      worker1 = Worker(worker, category, exhours, mxt)
      boleta1 = Boleta(worker, category, exhours, mxt)

     #Salida
      print(f"""----------------------------------------------------------------            
            
----------------------------------------------------------------
                        BOLETA DE PAGO          
      
            NOMBRE:                   {boleta1.worker}
      
            CATEGORÍA:                {boleta1.category}
      
            SUELDO BÁSICO:            S/.{boleta1.fijarSB()}
      
            DESCUENTO POR TARDANZA:   S/.{boleta1.descontarTar()}
      
            PAGO POR HORAS EXTRAS:    S/.{boleta1.calcularphx()}
      
            SUELDO NETO:              S/.{boleta1.calcularSN()}
                  
            
            {worker1.verificacion()}
----------------------------------------------------------------
""")

datos1=principal()



while True: #Este bucle pregunta si es que se quiere continuar calculando el sueldo de otro trabajador y si no, simplemente se cierra
      msg=str(input("Desea continuar (SI | NO): ")).upper()
      if msg=='SI':
            print("----------------------------------------------------------------")
            datos2=principal()
      if msg=='NO':
            print()
            print('----------------- SALIO EXITOSAMENTE DEL PROGRAMA -----------------')
            break