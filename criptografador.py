texto = str(input('Insira um texto aqui: '))

criptografar = texto.translate(str.maketrans('zp', 'pz')).translate(str.maketrans('oe', 'eo')).translate(
    str.maketrans('nl', 'ln')).translate(str.maketrans('ia', 'ai')).translate(str.maketrans('rt', 'tr'))
print(criptografar)