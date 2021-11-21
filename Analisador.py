import re


class Analisador:
    # Linha do token
    lin_num = 1

    def tokenize(self, code):
        rules = [
            ('MAIN', r'main'),
            ('INT', r'int'),
            ('FLOAT', r'float'),
            ('IF', r'if'),
            ('ELSE', r'else'),
            ('WHILE', r'while'),
            ('LER', r'read'),
            ('PRINT', r'print'),
            ('EPARENTESES', r'\('),
            ('DPARENTESES', r'\)'),
            ('ECOLCHETE', r'\{'),
            ('DCOLCHETE', r'\}'),
            ('VIRGULA', r','),
            ('PVIRGULA', r';'),
            ('DUPLOIGUAL', r'=='),
            ('DIFE', r'!='),
            ('MENORQUE', r'<='),
            ('MAIORQUE', r'>='),
            ('OU', r'\|\|'),
            ('E', r'&&'),
            ('IGUAL', r'\='),
            ('MENOR', r'<'),
            ('MAIOR', r'>'),
            ('MAIS', r'\+'),
            ('MENOS', r'-'),
            ('MULTIPL', r'\*'),
            ('DIVIS', r'\/'),
            ('ID', r'[a-zA-Z]\w*'),
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),
            ('INTEGER_CONST', r'\d(\d)*'),
            ('NOVALINHA', r'\n'),
            ('PASSA', r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]
        #Separa o lexema com o respectivo token
        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        inicio = 0

        # Saida
        token = []
        lex = []
        linha = []
        coluna = []

        # Acha o lexema do token
        '''Retorna um iterador produzindo objetos correspondência sobre todas
        as correspondências não sobrepostas para o padrão pattern de ER na string'''
        for s in re.finditer(tokens_join, code):
            tipo = s.lastgroup
            lexeme = s.group(tipo)

            if tipo == 'NOVALINHA':
                inicio = s.end()
                self.lin_num += 1
            elif tipo == 'PASSA':
                continue
            elif tipo == 'MISMATCH':
                raise RuntimeError('%r unexpected on line %d' % (lexeme, self.lin_num))
            else:
                col = s.start() - inicio
                coluna.append(col)
                token.append(tipo)
                lex.append(lexeme)
                linha.append(self.lin_num)
                # To print information about a Token
                print('Token = {0}, Lexema = \'{1}\', Linha = {2}, Coluna = {3}'.format(tipo, lexeme,
                                                                                      self.lin_num, col))

        return token, lex, linha, coluna
