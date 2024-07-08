import random

num = random.randint(1,10)
resp = int(input("Digite um número entre 1 e 10"))

if resp == num:
    print("Você acertou, parabéns!")
else:
    print("Não foi dessa vez, tente novamente!")
    print("O número era {}".format(num))
