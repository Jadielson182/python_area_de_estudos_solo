def funcao(numero):
    
    for num in range(1, numero +1):
        cont = 1
        while True:
            print(num, end=' ')
            if cont == num:
                break
            cont += 1
        print()



funcao(9)

# def funcao(numero):
#     for num in range(numero):
#         num +=1
#         print(str(num) * num)



# funcao(6)