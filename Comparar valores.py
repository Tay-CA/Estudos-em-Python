#Sistematização
#Função é comparar os valores A e B

while True:
    A = int(input('Digite o valor de A:'))
    B = int(input('Digite o valor de B:'))  
    if A > B:
    #Se A for maior que B
        continue
    elif A==B:
    #Senão se A for igual a B
        print (A, 'e', B,'Valores de A e B iguais!')
        continue
    else:
    #Senão
        print(A, 'e', B)
        break
print('Valor de B maior que valor de A, fim do algoritmo')

#Caso seja executado no prompt de comando, descomentar a linha de código abaixo para que não feche automaticamente.
#input('Aperte enter para finalizar!')

