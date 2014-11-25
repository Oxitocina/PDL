#!/usr/bin/env python3

from SymTable import *
from sys import exit

class Lexico():
	
	def __init__(self, archivo):
		self.archivo = open(archivo, 'r')
		self.tabla_clave = {"var":0, "function":1, "return":2,
							"document.write":3, "prompt":4, "true":5,
							"false":6, "if":7, "do":8, "while":9}
		self.tabla_sym = SymTable()
		self.tabla_activa = self.tabla_sym.newTable()
		self.lexema = ""
		self.char_leido = self.archivo.read(1)
		
	def leer_siguiente(self):
		self.char_leido = self.archivo.read(1)
		if not self.char_leido:
			return False
		else:
			return True
	
	def sig_Token(self):
		
			
		
		while self.char_leido.isspace() and self.char_leido != '\n': #Tratamiento de espacios.
			self.char_leido = self.archivo.read(1)
		
		if self.char_leido == '/': #Tratamiento de comentarios.
			self.leer_siguiente()
			if self.char_leido != '/':
				self.error(1)
			else:
				while self.archivo.read(1) != '\n':
					pass
				self.char_leido = '\n'
			
		if self.char_leido == '(':
			self.leer_siguiente()
			return self.gen_Token("LParent")
		elif self.char_leido == ')':
			self.leer_siguiente()
			return self.gen_Token("RParent")
		elif self.char_leido == '{':
			self.leer_siguiente()
			return self.gen_Token("LBrace")
		elif self.char_leido == '}':
			self.leer_siguiente()
			return self.gen_Token("RBrace")
		elif self.char_leido == '\n':
			self.leer_siguiente()
			return self.gen_Token("eos")
		elif self.char_leido == ',':
			self.leer_siguiente()
			return self.gen_Token("Coma")
		elif self.char_leido == '+':
			self.leer_siguiente()
			return self.gen_Token("OpArit")
		elif self.char_leido == '>':
			self.leer_siguiente()
			return self.gen_Token("OpRelac")
		elif self.char_leido == '&':
			self.leer_siguiente()
			if self.char_leido == '&':
				self.leer_siguiente()
				return self.gen_Token("OpLogic")
			else:
				self.error(1)
		elif self.char_leido == '?':
			self.leer_siguiente()
			return self.gen_Token("OpCond?")
		elif self.char_leido == ':':
			self.leer_siguiente()
			return self.gen_Token("OpCond:")
		elif self.char_leido == '=':
			self.leer_siguiente()
			return self.gen_Token("OpAsig")
		elif self.char_leido.isnumeric() or self.char_leido == '-':
			self.lexema = self.char_leido
			return self.estado_digito() 
		elif self.char_leido.isalpha():
			self.lexema = self.char_leido
			return self.estado_letra()
		else:
			self.error(1)
		
		
	def estado_digito(self):
		self.leer_siguiente()
		while self.char_leido.isnumeric():
			self.lexema += self.char_leido
			self.leer_siguiente()
		if self.lexema != '-' and int(self.lexema) <= 32767 and int(self.lexema) >= -32767:
			return self.gen_Token("entero", int(self.lexema))
		else:
			self.error(2)
			
	def estado_letra(self):
		
		self.leer_siguiente()
		especial = False
		
		while self.char_leido.isnumeric() or self.char_leido.isalpha() or self.char_leido == '_' or self.char_leido == '.':
			if self.char_leido == '.':
				especial = True
			self.lexema += self.char_leido
			self.leer_siguiente()
		if especial and not lexema == 'document.write':
			self.error(3)
		if self.lexema in self.tabla_clave:
			return self.gen_Token("PClave", self.tabla_clave[self.lexema])
		else:
			if not self.tabla_sym.existsEntry(self.tabla_activa, self.lexema):
				self.tabla_sym.add(self.tabla_activa, self.lexema)
			return self.gen_Token("id", self.tabla_sym.searchPos(self.tabla_activa, self.lexema))
			
	def gen_Token(self, param1, param2 = None):
		return (param1, param2)
	def error(self, código):
		if código == 1:
			print("Caracter no soportado: " + self.char_leido)
			exit(1)
		elif código == 2:
			print("Número no soportado: " + self.lexema)
			exit(2)
		elif codigo == 3:
			print("Caracter . no soportado, unicamente en document.write()")
			exit(3)
		
		
