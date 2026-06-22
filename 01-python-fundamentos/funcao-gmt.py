# DESENVOLVER UMA FUNCAO PARA O CALCULO DA GLICOSE MATURADA TOTAL (GMT)
# GMT = PESO * ALTURA / (IGLICEMICO**2)
# PESO: Kg
# ALTURA: cm
# IGLICEMICO: entre 10 e 300

def calcularGMT(peso,altura,iglicemico):
    if (10>iglicemico) or (iglicemico>300):
        return -1
    GMT = peso * altura / (iglicemico**2)
    return GMT
 
peso = float(input("DIGITAR PESO:"))
altura = float(input("DIGITAR ALTURA:"))
iglice = float(input("DIGITAR INDICE GLICEMICO:"))
IGMT = calcularGMT(peso, altura, iglice)
print("\nVALOR DO GMT:", IGMT)