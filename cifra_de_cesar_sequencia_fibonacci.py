from time import sleep

def sequenciaDeFibonacci(n):
    sequenciaFibonacci = [0,1]
    while len(sequenciaFibonacci) < n:
        proximoNumero = sequenciaFibonacci[-1] + sequenciaFibonacci[-2]
        sequenciaFibonacci.append(proximoNumero)
    return sequenciaFibonacci
    

