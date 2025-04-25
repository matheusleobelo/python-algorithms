# teste-1

caderno = dict()
caderno['maça'] = 0.65
caderno['leite'] = 1.49
caderno['abacate'] = 1.49

print(caderno)
print()

# teste-2

listaTelefonica = {}
listaTelefonica['Jenny'] = 8675309
listaTelefonica['emergencia'] = 911

print(listaTelefonica['Jenny'])
print()

# teste-3

votaram = {}

def verificarEleitor(nome):
    if votaram.get(nome):
        print('Já votou!!')
    else:
        votaram[nome] = True
        print('Pode votar')

verificarEleitor('Tom')
verificarEleitor('mike')
verificarEleitor('mike')