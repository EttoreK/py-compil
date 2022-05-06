with open('m.dfa') as dfa_file:
    dfa_data = dfa_file.read()
print(dfa_data)
dfa = eval(dfa_data)
# Para conferir o conteúdo
print(dfa['initial_state'])
print(dfa['states'])
print(dfa['delta'])
print(dfa['delta'][(1,'1')])