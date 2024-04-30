# Programa que converte números inteiros para binários, o programa fará uma senha

import random
p = input("Digite uma palavra (4 letras minúsculas):")

ord0 = ord(p[0])
ord1 = ord(p[1])
ord2 = ord(p[2])
ord3 = ord(p[3])
#print(ord0, ord1, ord2, ord3)

rnum = random.randint(1, 10)
rbin = bin(rnum)
bir = rbin[2:]

print("Suas opções de senha são:")
print(ord0, ord1, bir, p[2] + p[3])
print(p[0] + p[1], bir, ord2, ord3)