from cuentaBancaria import CuentaBancaria

class Usuario:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.cuenta = CuentaBancaria(tasa_interes=0.15,balance=0)

	def _metodo_ejemplo(self):
		pass

	def hacer_deposito(self, monto):
		self.cuenta.deposito(monto)
		return self

	def mostrar_balance_usuario(self):
		self.cuenta.mostrar_info_cuenta()
		#print(f"{self.name} tiene actualmente en su cuenta $ {self.cuenta.balance}")
		return self

	def transferir_dinero(self, otro_usuario, cantidad):
		self.hacer_retiro(cantidad)
		otro_usuario.hacer_deposito(cantidad)
		return self