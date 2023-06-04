
'''Código do modelo Cifra de César
   Usuário escolhe a quantidade de deslocamento das letras.
'''

from time import sleep

def cifraDeCesar():
        
    mensagemCifrada = ''
    mensagem = str(input('Digite a mesangem que você deseja criptografar: '))
    sleep(1.5)
    print('Salvando informações, aguarde....')
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

    return mensagem, mensagemCifrada

def reverterMensagem(mensagem):
    mensagemRevertida = mensagem[::-1]
    return mensagemRevertida

while True:
    print('Aguarde um momento...carrengando informaçoes')
    sleep(2)
    mensagemDigitadaPeloUsuario, mensagemCifrada = cifraDeCesar()
    print('Criptografando sua mensagem...')
    sleep(1.5)
    print('Aguarde um momento...')
    sleep(3)
    print('Mensagem Cifrada:', mensagemCifrada)
    sleep(2)

    resposta = input('Você deseja cifrar uma nova mensagem? Digite "s" ou "n", por favor.')
    if resposta.lower() != 's':
        desejaMensagem = input('Você deseja reverter a última mensagem digitada? Digite "s" ou "n", por favor.')
        if desejaMensagem == 's':
            mensagemRevertida = reverterMensagem(mensagemCifrada)
            print('Revertendo a mensagem...')
            sleep(1.5)
            print('Mensagem Revertida: ',mensagemRevertida )
            print('Mensagem Original:', mensagemDigitadaPeloUsuario)
        print('Obrigado!!')
        sleep(1)
        break
print('Fim!!!')