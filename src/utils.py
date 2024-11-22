import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

#Função para saber se é numero ou ponto
def eNumouDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))
