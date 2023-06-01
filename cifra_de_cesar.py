from time import sleep
mensagemCifrada = ''
mensagem = str(input('Escreva a mesangem que deseja criptografar: '))
deslocarLetra = int(input('O deslocamento da letra será em quantas posições, '
                'informe em números inteiros, por favor: '))
for letra in mensagem:
    if letra.isalpha():        
        if letra.isupper():
            codigo = ord(letra) - ord('A')
            codigoNovo = (codigo + deslocarLetra) % 26
            caractereNovo = chr(codigoNovo + ord('A'))
            mensagemCifrada += caractereNovo
        else:
            codigo = ord(letra) - ord('a')
            codigoNovo = (codigo + deslocarLetra) % 26
            caractereNovo = chr(codigoNovo + ord('a'))
            mensagemCifrada += caractereNovo
    else:
        mensagemCifrada += letra

print('Fim!!!')

