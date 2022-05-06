def simular_dfa(dfa, entrada):
    estado = dfa(['initial_state'])
    aceitar = False

    while len(entrada) > 0:
        c = entrada.pop(0)

        if c not in dfa(['sigma']):
            print("ERRO! ERRO! ERRO!\nO símbolo ", c, "não pertence ao alfabeto do autômato!")
            entrada.insert(0,c)
            break
        if estado not in dfa(['states']):
            print('O estado', estado,
                'não pertence ao conjunto de estados do autômato!')
            break
        
        estado = estado[c]