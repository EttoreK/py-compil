def simular_dfa(dfa, entrada):
    estado = dfa(['initial_state'])
    aceitar = False

    while len(entrada) > 0:
        c = entrada.pop(0)

        if c != dfa(['sigma']):
            
