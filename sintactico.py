#! /usr/bin/python3
from lexico import *
from sys import exit

class Sintactico():
	
	def __init__(self, archivo):
		
		self.lexico = Lexico(archivo)
		self.token = self.lexico.sig_Token()
		self.parser = open("parser", "w")
		self.parser.write("Descendente ")
		self.firsts = {"D":["var", "if", "do", "while", "id", "document.write", "prompt", "return"], 
						"Z": ["eos"], "F":["function"], "S":["id","document.write", "prompt", "return"],
						"E": ["LParent","entero", "id", "true", "false"], "E'": ["LParent","entero", "id", "true", "false"],
						"G": ["LParent","entero", "id", "true", "false"], "T": ["LParent","entero", "id", "true", "false"],
						"U": ["LParent","entero", "id", "true", "false"], "V": ["LParent","entero", "id", "true", "false"]}
		self.follows = {"D": ["eos"], "X": ["eos", "OpCond:"], "E": ["RParent", "Coma"],
						"Z'": ["var", "if", "do", "while", "id", "document.write", "prompt", "return", "eos", "function", "LBrace", "RBrace"]}
	
	def P(self):
		self.token_clave()
		if self.token[0] in self.firsts["D"] or self.token[0] in self.firsts["Z"]:
			self.D()
			self.Z()
			self.P()
		elif self.token[0] in self.first["F"]:
			self.F()
			self.Z()
			self.P()
		# Falta EOF
		
		else:
			self.error()
		self.parser.write("1 ")
		
	def F(self):
		self.equiparar("function")
		self.equiparar("id")
		self.equiparar("LParent")
		self.E()
		self.equiparar("RParent")
		self.Z()
		self.equiparar("LBrace")
		self.Z()
		self.C()
		self.Z()
		self.equiparar("RBrace")
		self.parser.write("2 ")
	
	def D(self):
		if self.token[0] == "var":
			self.equiparar("var")
			self.equiparar("id")
		elif self.token[0] == "if":
			self.equiparar("if")
			self.equiparar("LParent")
			self.E()
			self.equiparar("RParent")
			self.S()
		elif self.token[0] == "do":
			self.equiparar("do")
			self.Z()
			self.equiparar("LBrace")
			self.Z()
			self.C()
			self.Z()
			self.equiparar("RBrace")
			self.equiparar("while")
			self.equiparar("LParent")
			self.E()
			self.equiparar("RParent")
		elif self.token[0] == "while":
			self.equiparar("while")
			self.equiparar("LParent")
			self.E()
			self.equiparar("RParent")
			self.Z()
			self.equiparar("LBrace")
			self.Z()
			self.C()
			self.Z()
			self.equiparar("RBrace")
		elif self.token[0] in self.firsts["S"]:
			self.S()
		elif self.token[0] in self.follows["D"]:
			pass
		else:
			self.error()
		self.parser.write("3 ")
			
	def S(self):
		if self.token[0] == "id":
			self.equiparar("id")
			self.Sp
		elif self.token[0] == "document.write":
			self.equiparar("document.write")
			self.equiparar("LParent")
			self.E()
			self.equiparar("RParent")
		elif self.token[0] == "prompt":
			self.equiparar("prompt")
			self.equiparar("LParent")
			self.equiparar("id")
			self.equiparar("RParent")
		elif self.token[0] == "return":
			self.equiparar("return")
			self.X()
		else:
			self.error()
		self.parser.write("4 ")
			
	def Sp(self):
		if self.token[0] == "OpAsig":
			self.equiparar("OpAsig")
			self.E()
		elif self.token[0] == "LParent":
			self.equiparar("LParent")
			self.L()
			self.equiparar("RParent")
		else:
			self.error()
		self.parser.write("5 ")
			
	def C(self):
		if self.token[0] in self.firsts["D"] or self.first["Z"]:
			self.D()
			self.Z()
			self.C()
		elif self.token[0] in self.follows["C"]:
			pass
		else:
			self.error()
		self.parser.write("6 ")
		
	def Z(self):
		self.equiparar("eos")
		self.Zp()
		self.parser.write("7 ")
		
	def Zp(self):
		if self.token[0] == "eos":
			self.equiparar("eos")
			self.Zp()
		elif self.token[0] in self.follows["Z'"]:
			pass
		else:
			self.error()
		self.parser.write("8 ")
		
	def X(self):
		if self.token[0] in firsts["E"]:
			self.E()
		elif self.token[0] in follows["X"]:
			pass
		else:
			self.error()
		self.parser.write("9 ")
		
	def L(self):
		if self.token[0] in self.firsts["E"]:
			self.E()
			self.Q()
		elif self.token[0] in self.follows["L"]:
			pass
		else:
			self.error()
		self.parser.write("10 ")
		
	def Q(self):
		if self.token[0] == "coma":
			self.equiparar("coma")
			self.E()
			self.Q()
		elif self.token[0] in self.follows["Q"]:
			pass
		else:
			self.error()
		self.parser.write("11 ")
		
	def A(self):
		if self.token[0] == "id":
			self.equiparar("id")
			self.R()
		elif self.token[0] in self.follows["A"]:
			pass
		else:
			self.error()
		self.parser.write("12 ")
			
	def R(self):
		if self.token[0] == "coma":
			self.equiparar("coma")
			self.equiparar("id")
			self.R()
		elif self.token[0] in self.follows["R"]:
			pass
		else:
			self.error()
		self.parser.write("13 ")
			
	def E(self):
		if self.token[0] in self.firsts["E'"]:
			self.Ep()
		else:
			self.error()
		self.parser.write("14 ")
		
	def Ep(self):
		if self.token[0] in self.firsts["E"]:
			self.E()
			self.equiparar("OpCond?")
			self.S()
			self.equiparar("OpCond:")
			self.S()
		elif self.token[0] in self.firsts["G"]:
			self.G()
		else:
			self.error()
		self.parser.write("15 ")
	
	def G(self):
		if self.token[0] in self.firsts["T"]:
			self.T()
			self.Gp()
		else:
			self.error()
		self.parser.write("16 ")
	
	def Gp(self):
		if self.token[0] == "&":
			self.equiparar("&")
			self.equiparar("&")
			self.T()
			self.Gp()
		elif self.token[0] in self.follows["Gp"]:
			pass
		else:
			self.error()
		self.parser.write("17 ")
	
	def T(self):
		if self.token[0] in self.firsts["U"]:
			self.U()
			self.Tp()
		else:
			self.error()
		self.parser.write("18 ")
		
	def Tp(self):
		if self.token[0] == "OpRelac":
			self.equiparar("OpRelac")
			self.U()
			self.Tp
		elif self.token[0] in self.follows["Tp"]:
			pass
		else:
			self.error()
		self.parser.write("19 ")
		
	def U(self):
		if self.token[0] in self.firsts["V"]:
			self.V()
			self.Up()
		else:
			self.error()
		self.parser.write("20 ")
		
	def Up(self):
		if self.token[0] == "OpArit":
			self.equiparar("OpArit")
			self.V()
			self.Up()
		elif self.token[0] in self.follows["Up"]:
			pass
		else:
			self.error()
		self.parser.write("21 ")
		
	def V(self):
		if self.token[0] == "LParent":
			self.equiparar("LParent")
			self.E()
			self.equiparar("RParent")
		elif self.token[0] == "id":
			self.equiparar("id")
			self.Vp()
		elif self.token[0] == "entero":
			self.equiparar("entero")
		elif self.token[0] == "true":
			self.equiparar("true")
		elif self.token[0] == "false":
			self.equiparar("false")
		else:
			self.error()
		self.parser.write("22 ")
	
	def Vp(self):
		if self.token[0] == "LParent":
			self.equiparar("LParent")
			self.L()
			self.equiparar("RParent")
		elif self.token[0] in self.follows["Vp"]:
			pass
		else:
			self.error()
		self.parser.write("23 ")
			
	def token_clave(self):
		if self.token[0] == "PClave":
			for word, code in self.lexico.tabla_clave.items():
				if code == self.token[1]:
					self.token = (word, None)
					break
	def equiparar(self, token_esperado):
		if self.token[0] == token_esperado:
			self.token = self.lexico.sig_Token()
			self.token_clave()
		else:
			self.error()
			
	def error(self):
		print("Token no esperado: " + self.token[0])
		exit(1)
		
