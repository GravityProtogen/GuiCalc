import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

#Função para saber se é numero ou ponto
def eNumouDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

#Função de Validação de Numero
def eNumeroValido(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid
