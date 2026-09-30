print("----------Tabuada----------")

n = int(input("Digite um numero para saber sua tabuada ate N x 10: "))

print("Aqui esta a tabuada de", n)

for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i:2d} = {resultado}")

print("-" * 15)
    