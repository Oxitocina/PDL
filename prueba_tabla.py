#!/usr/bin/env python3

from SymTable import *

tabla_sym = SymTable()
tabla = tabla_sym.newTable()
lex1 = tabla_sym.add(tabla, "culo")
print(tabla_sym.addType(tabla, "culo", "string"))
lex1 = tabla_sym.add(tabla, "func")
print(tabla_sym.addType(tabla, "func", "function", "string", 2, ["int","int"]))
tabla_sym.writeTable("./tabla")
