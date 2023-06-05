from time import sleep

def sequenciaDeFibonacci(n):
    sequenciaFibonacci = [0,1]
    while len(sequenciaFibonacci) < n:
        proximoNumero = sequenciaFibonacci[-1] + sequenciaFibonacci[-2]
        sequenciaFibonacci.append(proximoNumero)
    return sequenciaFibonacci
    
def cifraDeCesar():
    mensagemCifrada = ''
    mensagem = str(input('Digite a mensagem que voce deseja criptografar: '))
    sleep(1.5)
    print('Salvando a mensagem que você digitou, aguarde...')
    sleep(3.5)
    
    deslocarLetra = sequenciaDeFibonacci(len(mensagem))

    for i, letra in enumerate(mensagem):
        if letra.salpha():
            if letra.isupper():
                codigo = ord(letra) - ord('A')
                codigoNovo = (codigo + deslocarLetra[i]) % 26
                caractereNovo = chr(codigoNovo + ord('A'))
                mensagemCifrada += caractereNovo
            else:
                codigo = ord(letra) - ord('a')
                codigoNovo = chr(codigoNovo + ord('a'))
                mensagemCifrada += caractereNovo
        else:
            mensagemCifrada += letra
    
    return mensagemCifrada