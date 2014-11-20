"""
Software distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license. This allows you to adapt, copy, distribute and transmit the work while crediting the author of the original work and sharing under the same or similar license.
Full legal text of this license can be found on http://creativecommons.org/licenses/by-sa/3.0/legalcode
"""

class Table():

    def __init__(self, id):
        self.lexems = {}
        self.exists = True
        self.id = id

    def delete(self):
        """This function marks this table as deleted"""

        self.exists = False
        return True

    def exist(self):
        """Checks if this table is deleted or not"""

        return self.exists

    def add(self, lex):
        """Adds lex to this table.
        Returns the position of the lex if everything went OK."""

        if not lex in self.lexems:
            self.lexems[lex] = []
            return self.getPos(lex)
        else:
            return self.getPos(lex)

    def setType(self, lex, tipo, tipo_dev, n_args, args):
        """Sets the type of lex.
        Returns True if everything went OK. Otherwise, returns False"""

        if lex in self.lexems:
            self.lexems[lex] = []
            self.lexems[lex].append(tipo)
            if tipo_dev != None:
                self.lexems[lex].append(tipo_dev)
                self.lexems[lex].append(n_args)
                self.lexems[lex].append(args)
            return True
        else:
            return False

    def getType(self, lex):
        "Returns the type of lex"

        return self.lexems[lex]

    def contains(self, lex):
        "Checks if lex is in the table or not"

        return lex in self.lexems

    def write(self, path):
        "Writes the contents of this table to the file pointed to by path"

        if self.exist():
            f = open(path, 'a')
            f.write('--------------------| Tabla' + str(self.id) + ' |--------------------\n')
            f.write('----------------------------------------------------\n')
            for e in self.lexems.keys():
                f.write('\t' + str(e))
                if self.lexems[e] != '':
                    for i in self.lexems[e]:
                        f.write(' (' + str(i) + ')')
                f.write('\n')
            f.write('\n\n\n')
            f.close()
            return True
        else:
            return False

    def getPos(self, lex):
        "returns the ID of lex or False if lex is not in this table"

        i = 0
        for e in self.lexems.keys():
            if e == lex:
                break
            else:
                i = i + 1
        return False if i == len(self.lexems) else i
