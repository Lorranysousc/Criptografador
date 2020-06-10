texto = str(input('Insira um texto parar descriptografar: '))

descriptografando = texto.translate(str.maketrans('pz', 'zp')).translate(str.maketrans('eo', 'oe')).translate(
    str.maketrans('ln', 'nl')).translate(str.maketrans('ai', 'ia')).translate(str.maketrans('tr', 'rt'))
print(descriptografando)