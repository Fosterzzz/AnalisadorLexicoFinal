from Load import Load
from Analisador import Analisador

if __name__ == '__main__':
    load = Load()
    analisador = Analisador()

    token = []
    lexeme = []
    linha = []
    coluna = []

    for i in load.load_buffer():
        t, lex, lin, col = analisador.tokenize(i)
        token += t
        lexeme += lex
        linha += lin
        coluna += col

    print('\nRecognize Tokens: ', token)

