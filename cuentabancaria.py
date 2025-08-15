class cuentabancaria:
    def __init__ (self,Titular, saldo=0) :
        self.Titular = Titular
        self.saldo = saldo
    def depositar (self, cantidad): #self siempre va primero, cantidad va segundo porque sera la variable que recibira el monto a sumarsele.
        self.saldo = self.saldo + cantidad
    def retiro (self, cantidad):
        self.saldo = self.saldo - cantidad
    def mostrar_saldo (self):
        print (f'el saldo de su cuenta es {self.saldo}')
        

        
cuenta_titular = cuentabancaria ('KikitoGuzman', 1000)
cuentasinsaldodeortiz = cuentabancaria ('ortiz')

cuenta_titular.depositar(500)
cuenta_titular.mostrar_saldo()
cuentasinsaldodeortiz.retiro(500)
cuentasinsaldodeortiz.mostrar_saldo()
#print (f' el nombre del titular es {cuenta_titular.Titular}, el saldo de la cuenta es {cuenta_titular.saldo} ')
#print (f'el nombre del titular es {cuentasinsaldodeortiz.Titular}, el saldo de la cuenta es {cuentasinsaldodeortiz.saldo} '