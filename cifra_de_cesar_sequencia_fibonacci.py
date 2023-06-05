from time import sleep

def sequenciaDeFibonacci(n):
    sequenciaFibonacci = [0, 1]
    while len(sequenciaFibonacci) < n:
        proximoNumero = sequenciaFibonacci[-1] + sequenciaFibonacci[-2]
        sequenciaFibonacci.append(proximoNumero)
    return sequenciaFibonacci
    
def cifraDeCesar():
    mensagemCifrada = ''
    mensagem = str(input('Digite a mensagem que você deseja criptografar: '))
    sleep(1.5)
    print('Salvando a mensagem que você digitou, aguarde...')
    sleep(3.5)
    
    deslocarLetra = sequenciaDeFibonacci(len(mensagem))

    for i, letra in enumerate(mensagem):
        if letra.isalpha():
            if letra.isupper():
                codigo = ord(letra) - ord('A')
                codigoNovo = (codigo + deslocarLetra[i]) % 26
                caractereNovo = chr(codigoNovo + ord('A'))
                mensagemCifrada += caractereNovo
            else:
                codigo = ord(letra) - ord('a')
                codigoNovo = (codigo + deslocarLetra[i]) % 26
                caractereNovo = chr(codigoNovo + ord('a'))
                mensagemCifrada += caractereNovo
        else:
            mensagemCifrada += letra
    
    return mensagemCifrada

while True:
    print('Aguarde um momento...carregando informações.')
    sleep(2)
    mensagemCifrada = cifraDeCesar()
    print('Criptografando sua mensagem com base na Sequência de Fibonacci.')
    sleep(1.1)
    print('Aguarde um momento.')
    sleep(3.5)
    print('Mensagem Cifrada:', mensagemCifrada)
    sleep(2)

    resposta = input('Você deseja cifrar uma nova mensagem? Digite "s" ou "n": ')
    if resposta.lower() != 's':
        print('Obrigado!!')
        sleep(1)
        break
print('Fim!!')
