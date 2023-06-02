
'''Código do modelo Cifra de César
   Usuário escolhe a quantidade de deslocamento das letras.
'''

from time import sleep

def cidraDeCesar():
        
    mensagemCifrada = ''
    mensagem = str(input('Escreva a mesangem que deseja criptografar: '))
    sleep(1.5)
    print('Salvando informações, aguarde um momento por favor...')
    sleep(3.5)
    deslocarLetra = int(input('O deslocamento da letra será em quantas posições, '
                    'informe em números inteiros, por favor: '))
    sleep(1)
    print('Salvando deslocamento...aguarde mais um momento')
    sleep(1.5)
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

    return mensagemCifrada
print('Aguarde um momento...carrengando informaçoes')
sleep(2)
mensagemCifrada = cidraDeCesar()
print('Salvando mensagem digitada')
sleep(1.5)
print('Aguarde um momento...')
sleep(3)
print('Mensagem Cifrada:', mensagemCifrada)
print('Fim!!!')


