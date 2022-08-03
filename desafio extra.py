tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número: ", tabuada)
for valor in range(1,11,1):
    print("{0} x {1} = {2}".format(str(tabuada), str(valor), str((tabuada * valor))))
    #add modificação para teste de branch
    #print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))