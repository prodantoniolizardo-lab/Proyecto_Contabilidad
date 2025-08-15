class cuentabancaria:
    def __init__ (self,Titular, saldo=0) :
        self.Titular = Titular
        self.saldo = saldo
    def depositar (self, cantidad): #self siempre va primero, cantidad va segundo porque sera la variable que recibira el monto a sumarsele.
        if cantidad > 0: 
            self.saldo = self.saldo + cantidad
        else:
            print ('Error deposito deposito debe ser mayor a 0')
    def retiro (self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo = self.saldo - cantidad
            else:
                print ('no tiene balance suficiente')
    def mostrar_saldo (self):
        print (f'el saldo de su cuenta es {self.saldo}')
        

        
cuenta_titular = cuentabancaria ('KikitoGuzman', 1000)
cuentasinsaldodeortiz = cuentabancaria ('ortiz')

cuenta_titular.depositar(0)
cuenta_titular.retiro(5000)
cuenta_titular.mostrar_saldo()
cuentasinsaldodeortiz.retiro(5000)
cuentasinsaldodeortiz.mostrar_saldo()
#print (f' el nombre del titular es {cuenta_titular.Titular}, el saldo de la cuenta es {cuenta_titular.saldo} ')
#print (f'el nombre del titular es {cuentasinsaldodeortiz.Titular}, el saldo de la cuenta es {cuentasinsaldodeortiz.saldo} '