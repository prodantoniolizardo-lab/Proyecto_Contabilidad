class cuentabancaria:
    def __init__ (self,Titular, saldo=0):
        self.Titular = Titular
        self.saldo = saldo
        
cuenta_titular = cuentabancaria ('KikitoGuzman', 1000)
cuentasinsaldodeortiz = cuentabancaria ('ortiz')
print (f' el nombre del titular es {cuenta_titular.Titular}, el saldo de la cuenta es {cuenta_titular.saldo} ')
print (f'el nombre del titular es {cuentasinsaldodeortiz.Titular}, el saldo de la cuenta es {cuentasinsaldodeortiz.saldo} ')
