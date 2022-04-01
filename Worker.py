
class Worker: #Declaramos la clase worker= Trabajador

    def __init__(self, worker, category, exhours, mxt): #se inicializa el constructor con los atributos

        self.worker = worker
        self.category = category
        self.exhours = exhours
        self.mxt = mxt
    
    
    def fijarSB(self): # creamos la funcion "fijarSB", para identicar el tipo de sueldo básico dependiendo de su categoría

        if self.category == 'A':
            self.sb = 3000
            
        elif self.category == 'B':
            self.sb = 2500
            
        else:
            self.sb = 2000
            
        return self.sb # retornar resultado a la función    
        
        
    def verificacion(self): #Declaramos la función "vereficacion"

        if self.category == 'A' or self.category == 'B' or self.category == 'C':
            self.msg = "LOS DATOS FUERON INGRESADOS CORRECTAMENTE"
            
        else:
            self.msg = "LOS DATOS NO FUERON INGRESADOS CORRECTAMENTE"

        return self.msg # retornar resultado a la función
            
    