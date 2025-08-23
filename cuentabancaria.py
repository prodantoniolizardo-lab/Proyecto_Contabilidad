fecha_actual = '22/8/2025'
class cuentabancaria:
    def __init__ (self,Titular, saldo=0,) :
        self.Titular = Titular
        self.saldo = saldo
        self.historial = []
    def depositar (self, cantidad): #self siempre va primero, cantidad va segundo porque sera la variable que recibira el monto a sumarsele.
        if cantidad > 0: 
            self.saldo = self.saldo + cantidad 
            nueva_transaccion = Transaccion (cantidad, "deposito", fecha_actual)
            self.historial.append(nueva_transaccion)
            
        else:
            print ('Error deposito deposito debe ser mayor a 0')
            
        
    def retiro (self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad: #tambien podria ser if cantidad > 0 and self.saldo >= cantidad: asi se elimina una linea
                self.saldo = self.saldo - cantidad
                nueva_transaccion = Transaccion(cantidad, "retiro",fecha_actual)
                self.historial.append(nueva_transaccion)
            else:
                print ('no tiene balance suficiente')
                
    def mostrar_saldo (self):
        print (f'el saldo de su cuenta es {self.saldo}')
    
    def mostrar_historial (self):
        print ('---historial de transacciones')
        if not self.historial:
            print ('no hay transas registradas')
        else:
            for Transaccion in self.historial:
                print (f'tipo de transa es {Transaccion.tipo} el monto es {Transaccion.monto} fecha {Transaccion.fecha}')
                
        

class Transaccion:
    def __init__(self, monto, tipo, fecha):
        self.monto = monto
        self.tipo = tipo 
        self.fecha = fecha


cuenta_titular = cuentabancaria ('KikitoGuzman', 1000)
cuentasinsaldodeortiz = cuentabancaria ('ortiz')

cuentasinsaldodeortiz.depositar(10000)
cuentasinsaldodeortiz.mostrar_historial()
cuentasinsaldodeortiz.mostrar_saldo()


#cuenta_titular.depositar(0)
#cuenta_titular.retiro(5000)
#cuenta_titular.mostrar_saldo()
#cuentasinsaldodeortiz.retiro(5000)
#cuentasinsaldodeortiz.mostrar_saldo()
#print (f' el nombre del titular es {cuenta_titular.Titular}, el saldo de la cuenta es {cuenta_titular.saldo} ')
#print (f'el nombre del titular es {cuentasinsaldodeortiz.Titular}, el saldo de la cuenta es {cuentasinsaldodeortiz.saldo} '
#transaccion_1 = transacciones(2000,"deposito","14/08/2025")
#transaccion_2 = transacciones(500,"retiro","34/08/2025")
