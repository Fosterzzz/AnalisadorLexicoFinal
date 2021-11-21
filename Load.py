class Load:
    def load_buffer(self):
        arq = open('codigo.c', 'r')
        texto = arq.readline()

        buffer = []
        cont = 1

        while texto != "":
            buffer.append(texto)
            texto = arq.readline()
            cont += 1

            if cont == 10 or texto == '':
                # Return a full buffer
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reset the buffer
                buffer = []

        arq.close()
