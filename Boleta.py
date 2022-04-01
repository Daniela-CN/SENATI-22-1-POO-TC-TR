from Worker import Worker


class Boleta(Worker): #Declaramos la clase Boleta, la cual deriva de la clase Worker
    
    def __init__(self, worker, category, exhours, mxt): #inicializamos el constructor con los atrivutos
        
        self.worker = worker
        self.category = category
        self.exhours = exhours
        self.mxt = mxt
  
    

    def calcularph(self): #creamos la función "calcularph", aquí calculamos el pago por hora del trabajador 

        if self.category == 'A': #Utilizamos la formula "PH" para relizar el cálculo 
            self.ph = round(self.sb / 240,2) #usamos la funcion round() y para redondear a solo 2 decimales
            
        elif self.category == 'B':
            self.ph = round(self.sb / 240,2)
            
        else:
            self.ph = round(self.sb / 240,2)

        return self.ph
    

    def calcularphx(self):#creamos la funcion "calcularphx", para calcular el pago por horas extras

        if self.category == 'A':
            self.phx = round(self.calcularph() * self.exhours, 2)
            
        elif self.category == 'B':
            self.phx = round(self.calcularph() * self.exhours, 2)
            
        else:
            self.phx = round(self.calcularph() * self.exhours, 2)
        
        return self.phx
    
    
    def descontarTar(self):#  Creamos la funcion descontarTar= Descontar Tardanza 
        
        self.dxt = round(((self.sb / 240) / 60) * self.mxt, 2)

        return self.dxt


    def calcularSN(self):#  Creamos la funcion calcularSN= calcular sueldo neto
        
        self.sueldon = round(self.sb - self.dxt + self.phx, 2)
        
        return self.sueldon

    


